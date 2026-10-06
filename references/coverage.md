# Collection coverage

Snapshot: **October 5, 2026 · America/Chicago**. Channel: [Return3](https://www.youtube.com/@return3116), ID `UC6e7E2AeC4j5Wq2BPp_pVYg`.

| Check | Result |
|---|---|
| Public uploads returned | 54; matches the channel header |
| Cataloged runtime | 13:59:02 (approximately 14 hours) |
| Recent business/mindset uploads | 9, totaling 12:06:17 |
| Detailed metadata | 53 via yt-dlp; visible metadata for 1 via browser |
| English captions retrieved | 40: 39 via yt-dlp, 1 via browser transcript export |
| No caption tracks exposed | 14 older uploads |
| Recent business/mindset captions | 9 of 9 retrieved |
| Video media downloaded | None |
| Full visual review | Not performed |

## What was reviewed

Business-relevant transcript passages and descriptions were reviewed across all nine recent uploads. The 6:49:01 compilation was reviewed through its introduction, samples at five-minute intervals across the timeline, and targeted searches for business/production terms; it was not read line by line. The older 45 uploads were screened through titles, descriptions, and caption samples where available. Music captions often contain sparse or inaccurate text and do not explain editing technique.

The nine recent caption tracks reach to within a few seconds of their listed video duration. This checks the returned timeline, not transcription accuracy or complete speech coverage. All are automatic captions; spelling, numbers, punctuation, and speaker attribution can be wrong.

The unauthenticated downloader returned an age-access error for `3TtG9GALlWA`. The existing browser session exposed the transcript and upload date, which were recorded separately. No login credentials or cookies were exported. The downloader finished with a nonzero aggregate status because of that single access error; the catalog reflects its recovered browser source.

“All” means the 54 uploads publicly returned by this channel at collection time. It does not include inaccessible private/deleted videos, unlisted videos not exposed by the channel, or future uploads. The header showed Home, Videos, and Playlists; no separate Shorts or Live tab was exposed.

## Files and reproducibility

- [Operating guide](operating-guide.md): practical procedures, with proposed implementation distinguished from source claims.
- [Source notes](source-notes.md): the nine relevant videos, timestamps, and limitations.
- [Machine-readable catalog](video-catalog.json): per-video retrieval and review status.
- [Agent entrypoint](../SKILL.md): when and how to apply the guide.
- [Collection script](../scripts/collect_channel.py): repeatable public metadata/caption collection.

Raw metadata and captions were retained in the task scratch directory under `work/`. The deliverable package contains original notes and links rather than full third-party transcripts or video files. It is a portable skill folder, not an automatically installed global skill.

Example refresh from a working directory (requires `yt-dlp` on PATH):

```sh
python3 /path/to/return3-playbook/scripts/collect_channel.py \
  --work-dir ./work/return3-refresh \
  --output ./work/return3-refresh/video-catalog.json
```

Use `--catalog-only` to rebuild from local data or `--limit 1` for a bounded collection check. Review source changes before replacing the guide. For supported browser transcript exports, place the exported text in `work-dir/browser-exports/VIDEO_ID.txt` and any manually observed metadata in `VIDEO_ID.metadata.json`, then rebuild the catalog. The script records retrieval, never claims a content review.

## Validation

The skill validator passed. The collector passed a live one-video smoke run and an offline rebuild against the full research collection. Local links, source video IDs, timestamp bounds, unique video count, and caption totals were checked. These checks validate the package and retrieval accounting, not the creator's business claims.

## Complete public upload index

| Date | Video | Duration | Captions | Review |
|---|---|---:|---|---|
| 2026-10-04 | [Ai Girls \| start of october brain dump (8k day, scaling structure, mindset changes)](https://www.youtube.com/watch?v=C5LFf6LE4NY) | 27:49 | Retrieved | Business transcript |
| 2026-09-20 | [Who Is Your King? (21Y/O 6Fig Online Entrepreneur Rambling)](https://www.youtube.com/watch?v=8CVJXLvImpg) | 20:00 | Retrieved | Business transcript |
| 2026-09-15 | [Successful Inputs Before I Hit $50k/mo](https://www.youtube.com/watch?v=lFAG6YhTZlI) | 6:49:01 | Retrieved | Compilation sampling |
| 2026-09-13 | [Moneymaxxing vs Socialmaxxing](https://www.youtube.com/watch?v=3TtG9GALlWA) | 50:05 | Browser export | Business transcript |
| 2026-08-22 | [Ai Girls: 6 fig operator brain dump (principles, mistakes, life review)](https://www.youtube.com/watch?v=ZrK8NcbZPZM) | 1:21:57 | Retrieved | Business transcript |
| 2026-08-06 | [Ai Girls: Month 14 ($140k/mo + Almost Died)](https://www.youtube.com/watch?v=707kRLMSdTA) | 48:21 | Retrieved | Business transcript |
| 2026-06-27 | [Ai Girls: 13 Months Deep ($150k/mo)](https://www.youtube.com/watch?v=PYrZqtzRGvQ) | 42:15 | Retrieved | Business transcript |
| 2026-05-15 | [Year 1: AI Girls (my real story)](https://www.youtube.com/watch?v=t3aA8QstXuQ) | 36:04 | Retrieved | Business transcript |
| 2026-03-22 | [$25k in a month \| Raw Ai OFM Online Business Fundamentals \| 10 months in](https://www.youtube.com/watch?v=69YdioCCiH4) | 10:45 | Retrieved | Business transcript |
| 2024-07-24 | [frag clips you can eat dinner too](https://www.youtube.com/watch?v=feAKCgS4e1Y) | 3:53 | Retrieved | Metadata/sample |
| 2024-06-12 | [dps clips i ate a sandwich too](https://www.youtube.com/watch?v=RosovAwRQi8) | 3:34 | None exposed | Metadata/sample |
| 2024-04-14 | [egoing diamonds](https://www.youtube.com/watch?v=Go4UrM9oEJw) | 7:24 | Retrieved | Metadata/sample |
| 2023-12-25 | [unfinished HXH long glitch edit from March 2022](https://www.youtube.com/watch?v=haATWJCLaQ4) | 1:44 | Retrieved | Metadata/sample |
| 2023-12-18 | [ODIE - Little Lies](https://www.youtube.com/watch?v=MS7dCRv6_sY) | 0:15 | None exposed | Metadata/sample |
| 2022-07-11 | [Fair Trade \| Bleach](https://www.youtube.com/watch?v=ce3U5T6szZs) | 0:18 | None exposed | Metadata/sample |
| 2022-05-29 | [Get Health Insurance! \| High School Skit](https://www.youtube.com/watch?v=cgyqz9j40vo) | 4:36 | Retrieved | Metadata/sample |
| 2022-05-03 | [The Millionaire Detective \| Vibe Edit / AMV](https://www.youtube.com/watch?v=_tryRecvt1g) | 0:21 | Retrieved | Metadata/sample |
| 2021-09-22 | [VALEMPIRE \| Kingcity Tri-lab](https://www.youtube.com/watch?v=6Bo8h1wzOxg) | 0:49 | Retrieved | Metadata/sample |
| 2021-07-27 | [DEVILISH - TOKYO GHOUL EDIT](https://www.youtube.com/watch?v=lCQ7jnaFkXs) | 0:22 | Retrieved | Metadata/sample |
| 2021-05-13 | [XXXTENTACION - KING (DEMON SLAYER EDIT)](https://www.youtube.com/watch?v=H9rcP5H7prY) | 0:57 | None exposed | Metadata/sample |
| 2021-04-14 | [Return3's Editing Compilation #2](https://www.youtube.com/watch?v=MgUHlbQux-E) | 3:22 | Retrieved | Metadata/sample |
| 2021-01-07 | [Return3's Editing Compilation Late 2020-Early 2021](https://www.youtube.com/watch?v=1S7ykO8LkJI) | 6:05 | None exposed | Metadata/sample |
| 2020-11-29 | [Relentless \| GOH x Naruto \| AMV](https://www.youtube.com/watch?v=o4wUuaIEE4s) | 0:37 | Retrieved | Metadata/sample |
| 2020-11-04 | [DESPAIR \| ITACHI \| AMV](https://www.youtube.com/watch?v=ER1eGoQLILo) | 1:03 | Retrieved | Metadata/sample |
| 2020-10-01 | [AHIM$A - MELIODAS \| NARUTO VS SASUKE「AMV」](https://www.youtube.com/watch?v=24JfQYtoKiw) | 1:53 | Retrieved | Metadata/sample |
| 2020-09-30 | [Flashboy - Sharingan \| Sasuke VS Itachi](https://www.youtube.com/watch?v=2RUKeyx-Gcw) | 2:08 | Retrieved | Metadata/sample |
| 2020-07-26 | [Nerf Boostio](https://www.youtube.com/watch?v=3CYHFgnWHDs) | 1:53 | None exposed | Metadata/sample |
| 2019-12-13 | [Freshman Rap Video \| Mitosis \| The Meta Squad](https://www.youtube.com/watch?v=zHHrEZT7W4c) | 7:24 | Retrieved | Metadata/sample |
| 2019-12-03 | [rust clan \| base tour](https://www.youtube.com/watch?v=M9zSdezN4S4) | 4:30 | None exposed | Metadata/sample |
| 2019-10-09 | [this kid is the best vendor in superior servers trading](https://www.youtube.com/watch?v=dv9W1msqslE) | 1:15 | Retrieved | Metadata/sample |
| 2019-09-22 | [Rocket Launchers On Top](https://www.youtube.com/watch?v=pMLxUR8dJkw) | 0:36 | Retrieved | Metadata/sample |
| 2019-09-09 | [is it legit? gamecountry base 1](https://www.youtube.com/watch?v=pszyPV9BgAY) | 1:39 | Retrieved | Metadata/sample |
| 2019-09-09 | [jesus's VS overpowered](https://www.youtube.com/watch?v=c021eW6yBag) | 2:15 | Retrieved | Metadata/sample |
| 2019-08-14 | [TwinTowerPower with a hint of Minecraft](https://www.youtube.com/watch?v=UuNkPjwnO6Q) | 4:58 | Retrieved | Metadata/sample |
| 2019-07-30 | [250$ ezpz](https://www.youtube.com/watch?v=wOwOV1Ktvxo) | 0:39 | Retrieved | Metadata/sample |
| 2019-06-29 | [Milkery Obliterated (Gmod)](https://www.youtube.com/watch?v=2U6LIiwxAso) | 5:14 | Retrieved | Metadata/sample |
| 2019-04-07 | [csgo montage #4](https://www.youtube.com/watch?v=mpqQ7yLb6fY) | 7:14 | None exposed | Metadata/sample |
| 2019-03-12 | [overwatch montage #4](https://www.youtube.com/watch?v=KhYe-zZEm1I) | 7:07 | None exposed | Metadata/sample |
| 2019-03-11 | [fortnite-montage #1](https://www.youtube.com/watch?v=vShGdBfgOyU) | 1:16 | None exposed | Metadata/sample |
| 2019-02-27 | [overwatch movie #3](https://www.youtube.com/watch?v=qgMghiog-tI) | 5:32 | Retrieved | Metadata/sample |
| 2019-02-13 | [csgo movie #3](https://www.youtube.com/watch?v=GuMMY4mhRt0) | 2:30 | Retrieved | Metadata/sample |
| 2019-02-12 | [overwatch movie #2](https://www.youtube.com/watch?v=yH-7EWcWXhg) | 1:39 | Retrieved | Metadata/sample |
| 2019-02-12 | [csgo movie #2](https://www.youtube.com/watch?v=Jn06TOTL6lk) | 1:02 | None exposed | Metadata/sample |
| 2019-02-08 | [csgo movie #1 (scout mostly)](https://www.youtube.com/watch?v=ZhW2znURu3o) | 1:37 | Retrieved | Metadata/sample |
| 2019-02-07 | [overwatch clip movie #1](https://www.youtube.com/watch?v=SXq0iycemwc) | 1:47 | Retrieved | Metadata/sample |
| 2019-01-13 | [CS:GO\| Karambit Night FT \| AK-47 Bloodsport ST MW \| 1080p-](https://www.youtube.com/watch?v=SZ7U4yzZXCI) | 2:01 | Retrieved | Metadata/sample |
| 2018-12-27 | [M9 Bayonet \| Fade \| Factory New \| 89% Fade](https://www.youtube.com/watch?v=OoQNYbXqq74) | 2:43 | Retrieved | Metadata/sample |
| 2018-12-19 | [lit 4k w. awp](https://www.youtube.com/watch?v=lbpLHtPY3mQ) | 0:40 | Retrieved | Metadata/sample |
| 2018-11-16 | [quick lil edited awp clip (mirage 3k)](https://www.youtube.com/watch?v=MuKDApVY2Pc) | 0:27 | None exposed | Metadata/sample |
| 2018-10-07 | [Purple Feelings - A Brawlhalla Montage](https://www.youtube.com/watch?v=dQvCf9CSagU) | 0:53 | None exposed | Metadata/sample |
| 2018-09-24 | [the ultimate no u card](https://www.youtube.com/watch?v=sXRRfs4LExQ) | 1:01 | Retrieved | Metadata/sample |
| 2018-09-21 | [just some clip ive always wanted to do](https://www.youtube.com/watch?v=ld84z9uDzfg) | 1:37 | Retrieved | Metadata/sample |
| 2018-06-19 | [INSANE Fastest 4k on Inferno (CS:GO)!](https://www.youtube.com/watch?v=BYN71NbIDrM) | 1:47 | Retrieved | Metadata/sample |
| 2016-12-02 | [Montage #1 - Brandoe (music included)](https://www.youtube.com/watch?v=dKIS-pzfgk0) | 2:08 | None exposed | Metadata/sample |
