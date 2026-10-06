# Return3 Playbook

A practical guide to the AI creator business methods discussed on [Return3’s YouTube channel](https://www.youtube.com/@return3116), with timestamped source notes and a reusable agent skill.

**[Read the operating guide →](references/operating-guide.md)**

## What is included

| File | Purpose |
|---|---|
| [Operating guide](references/operating-guide.md) | Character and offer design, content testing, conversion tracking, quality review, and delegation |
| [Source notes](references/source-notes.md) | Nine business/mindset videos with timestamps and evidence limits |
| [Coverage report](references/coverage.md) | Complete 54-video index and retrieval/review status |
| [Video catalog](references/video-catalog.json) | Machine-readable metadata and caption availability |
| [Agent skill](SKILL.md) | Instructions an AI assistant can follow to apply the guide |
| [Collection script](scripts/collect_channel.py) | Refresh public metadata and available English captions |

## Research coverage

Snapshot: **October 5, 2026**.

- All **54 publicly listed uploads** cataloged, totaling approximately 14 hours.
- **40 caption tracks** retrieved for research, including all nine recent business/mindset videos.
- **14 older uploads** had no exposed caption tracks.
- Business-relevant transcript passages were reviewed; the nearly seven-hour learning compilation was sampled and searched, not read line by line.
- Older gaming and anime uploads were screened by metadata and available caption samples. No full visual review was performed.

This repository contains original notes and source links. Full transcripts, downloaded videos, browser data, and private research files are not included.

## Use the guide with an AI assistant

Give the assistant [SKILL.md](SKILL.md) and its linked references, then ask:

> Use the Return3 playbook. My current stage is [stage], my weekly time is [hours], my experiment budget is [amount], and my current assets and metrics are [details]. Identify the weakest measured stage, build the next concrete artifact, and define the test and stopping condition. Distinguish source evidence from your proposed implementation.

The skill folder is portable. It is not automatically installed by cloning this repository.

## Refresh the catalog

Requires Python 3 and `yt-dlp` available on your PATH. From the repository root:

```sh
python3 scripts/collect_channel.py \
  --work-dir ./work/return3-refresh \
  --output ./work/return3-refresh/video-catalog.json
```

For a bounded first run, add `--limit 1`. To rebuild from data already collected, add `--catalog-only`. Run `--help` for all options.

Raw metadata and captions remain in `work/`, which is ignored by Git. Inspect changes and update the research notes before replacing the published catalog. Retrieval does not establish that a video has been reviewed.

## How to interpret it

This is independent research, not an official Return3 product or endorsement. Revenue figures and performance claims are self-reported and unaudited. The guide separates observed advice from proposed operating procedures, tracks changes in his recommendations, and marks undisclosed production details as unknown. Its implementation uses disclosed fictional adult characters, original or licensed assets, and non-explicit content production.
