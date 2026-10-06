#!/usr/bin/env python3
"""Collect public YouTube metadata and captions, never the video media.

Requires yt-dlp on PATH. Raw sources stay in --work-dir; the output is a
sanitized catalog without signed media URLs, cookies, or copied transcripts.
"""
import argparse
import datetime as dt
import json
import re
from pathlib import Path
import subprocess


def run(command, log_path):
    with log_path.open('a') as log:
        return subprocess.run(command, stdout=log, stderr=log).returncode


def leaves(node):
    if node.get('entries') is not None:
        for entry in node['entries']:
            if entry:
                yield from leaves(entry)
    elif node.get('id'):
        yield node


def normalize_caption(path):
    events = json.loads(path.read_text()).get('events', [])
    result = []
    for event in events:
        text = ''.join(part.get('utf8', '') for part in event.get('segs', [])).strip()
        if text:
            result.append({'start_seconds': event.get('tStartMs', 0) / 1000,
                           'text': text})
    return result


def normalize_browser_export(path):
    result = []
    for line in path.read_text().splitlines():
        match = re.match(r'^\[(\d+(?::\d+){1,2})\]\s*(.*)', line)
        if not match:
            continue
        seconds = 0
        for number in match[1].split(':'):
            seconds = seconds * 60 + int(number)
        if match[2].strip():
            result.append({'start_seconds': seconds, 'text': match[2].strip()})
    return result


def catalog(work):
    channel = json.loads((work / 'channel.json').read_text())
    unique = {row['id']: row for row in leaves(channel)}
    rows = []
    for video_id, flat in unique.items():
        info = work / 'metadata' / f'{video_id}.info.json'
        detail = json.loads(info.read_text()) if info.exists() else {}
        browser_meta = work / 'browser-exports' / f'{video_id}.metadata.json'
        browser_detail = json.loads(browser_meta.read_text()) if browser_meta.exists() else {}
        metadata = {**flat, **browser_detail, **detail}
        captions = sorted((work / 'metadata').glob(f'{video_id}.*.json3'))
        original = [p for p in captions if '.en-orig.' in p.name]
        caption = (original or captions or [None])[0]
        normalized = normalize_caption(caption) if caption else []
        browser_export = work / 'browser-exports' / f'{video_id}.txt'
        if not caption and browser_export.exists():
            normalized = normalize_browser_export(browser_export)
        if caption or normalized:
            (work / 'captions').mkdir(exist_ok=True)
            (work / 'captions' / f'{video_id}.json').write_text(
                json.dumps(normalized, ensure_ascii=False, indent=2))
        rows.append({
            'id': video_id,
            'url': f'https://www.youtube.com/watch?v={video_id}',
            'title': metadata.get('title'),
            'upload_date': metadata.get('upload_date'),
            'duration_seconds': metadata.get('duration'),
            'view_count_at_collection': metadata.get('view_count'),
            'metadata_status': 'retrieved' if detail else 'browser_visible_metadata' if browser_detail else 'flat_listing_only',
            'caption_status': ('retrieved' if caption else 'retrieved_browser' if normalized else
                               'not_available' if detail and not detail.get('subtitles') and
                               not detail.get('automatic_captions') else 'not_retrieved'),
            'caption_language': caption.name[len(video_id) + 1:-6] if caption else 'en' if normalized else None,
            'caption_source': 'yt-dlp' if caption else 'browser_transcript_export' if normalized else None,
            'caption_segments': len(normalized),
            'caption_last_start_seconds': normalized[-1]['start_seconds'] if normalized else None,
            'content_review_status': 'not_reviewed_by_this_script',
        })
    return {'channel_url': channel.get('webpage_url'), 'channel_id': channel.get('id'),
            'channel_title': channel.get('title'),
            'catalog_generated_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
            'scope': 'Public uploads returned by yt-dlp; excludes private, deleted, and unlisted videos not exposed by the channel.',
            'count': len(rows), 'videos': rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--channel', default='https://www.youtube.com/@return3116')
    parser.add_argument('--work-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--catalog-only', action='store_true', help='Use already collected local data; no network requests.')
    parser.add_argument('--limit', type=int, help='Bound metadata retrieval for a smoke test; catalog still contains the full channel listing.')
    args = parser.parse_args()
    work = args.work_dir.resolve()
    work.mkdir(parents=True, exist_ok=True)
    (work / 'metadata').mkdir(exist_ok=True)
    log = work / 'collection.log'
    if not args.catalog_only:
        with (work / 'channel.new.json').open('w') as out, log.open('a') as err:
            status = subprocess.run(['yt-dlp', '--flat-playlist', '--dump-single-json',
                                     '--skip-download', args.channel], stdout=out, stderr=err).returncode
        if status:
            raise SystemExit(f'Channel listing failed; inspect {log}')
        json.loads((work / 'channel.new.json').read_text())
        (work / 'channel.new.json').replace(work / 'channel.json')
        channel = json.loads((work / 'channel.json').read_text())
        entries = list({row['id']: row for row in leaves(channel)}.values())
        if args.limit is not None:
            if args.limit < 1:
                parser.error('--limit must be positive')
            entries = entries[:args.limit]
        for row in entries:
            video_id = row['id']
            # Metadata completes after caption attempts. Resume only when an
            # English track was retrieved or no captions exist at all.
            existing = work / 'metadata' / f'{video_id}.info.json'
            if existing.exists():
                old = json.loads(existing.read_text())
                have_caption = bool(list((work / 'metadata').glob(f'{video_id}.*.json3')))
                if have_caption or (not old.get('subtitles') and not old.get('automatic_captions')):
                    continue
            run(['yt-dlp', '--skip-download', '--write-info-json', '--write-subs',
                 '--write-auto-subs', '--sub-langs', 'en-orig,en', '--sub-format', 'json3',
                 '--ignore-errors', '--sleep-requests', '1', '--retries', '2',
                 '--socket-timeout', '20', '--no-progress',
                 '-o', str(work / 'metadata' / '%(id)s.%(ext)s'),
                 f'https://www.youtube.com/watch?v={video_id}'], log)
    data = catalog(work)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    statuses = {}
    for row in data['videos']:
        statuses[row['caption_status']] = statuses.get(row['caption_status'], 0) + 1
    print(json.dumps({'videos': data['count'], 'captions': statuses, 'output': str(args.output)}))


if __name__ == '__main__':
    main()
