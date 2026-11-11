# shawn-bio-search-lite

Search layer: public scholarly metadata adapters for PubMed, Europe PMC, OpenAlex, and Crossref. No private PDFs, corpora, manuscripts, credentials, or internal workflow state.

**License:** Apache-2.0

## SHawn OSS stack role

This repository is an **early-stage public-safe scaffold**. APIs are unstable. It supports the SHawn Research OS flagship rather than replacing it.

| Layer | Public repo | Role |
|---|---|---|
| Search | [`shawn-bio-search-lite`](https://github.com/L-SHawn91/shawn-bio-search-lite) | Public scholarly metadata adapters |
| Map | [`paper-map-lite`](https://github.com/L-SHawn91/paper-map-lite) | Toy claim/evidence graph schemas |
| Report | [`SHawn-ResearchOS`](https://github.com/L-SHawn91/SHawn-ResearchOS) | Flagship evidence maps and public reports |
| Coordinate | [`shawn-sync-lite`](https://github.com/L-SHawn91/shawn-sync-lite) | Public-safe manifests and boundary templates |
| Execute safely | [`newbrain-router`](https://github.com/L-SHawn91/newbrain-router) | Dry-run routing and approval-gate examples |
| QA docs | [`shawn-docx-qa`](https://github.com/L-SHawn91/shawn-docx-qa) / [`SHawn-hwp`](https://github.com/L-SHawn91/SHawn-hwp) | Document QA utilities |
| Present | [`SHawn-WEB`](https://github.com/L-SHawn91/SHawn-WEB) | Public hub/demo surface |

## Public boundary

This repository is a clean public-safe projection. It contains only schemas, templates, toy data, public metadata adapters, mock executors, and public reports.

It must not contain private databases, private manuscripts, PDFs, private corpora, local/internal paths, Discord identifiers, workflow logs, memory exports, credentials, or private project state.

## Unified public research SDK

This repository is the **unified public research SDK** for the SHawn OSS evidence
workflow stack. It holds the `shawn-bio-search-lite` search package at the repo
root and the consolidated map and coordinate component packages under
`packages/`. Every component keeps its own distribution name, import namespace,
license, tests, and docs, so it can be used standalone or as part of the stack.

| Component | Install name | Import name | Path | Role |
|---|---|---|---|---|
| Search | `shawn-bio-search-lite` | `shawn_bio_search_lite` | `src/` | Public scholarly metadata adapters |
| Map | `paper-map-lite` | `paper_map_lite` | `packages/paper-map-lite/` | Toy claim/evidence graph schemas |
| Coordinate | `shawn-sync-lite` | `shawn_sync_lite` | `packages/shawn-sync-lite/` | Public-safe manifests and boundary templates |

Import names and distribution names are unchanged from the standalone
repositories, so existing code keeps working.

### Install all component packages

```bash
python -m pip install -e ".[dev]"
python -m pip install -e "packages/paper-map-lite[dev]"
python -m pip install -e "packages/shawn-sync-lite[dev]"
```

### Test all component packages

Run every suite and every public-safety scan with one command:

```bash
python scripts/check_all.py
```

This runs the root suite and each component suite in **separate pytest sessions**
so that no test module basename is ever registered twice, then re-runs the
public-safety scanner over the whole tree (root tree plus imported packages).

Individual suites can also be run on their own:

```bash
python -m pytest -q tests                          # root search suite
python -m pytest -q tests                          # inside packages/paper-map-lite
python -m pytest -q tests                          # inside packages/shawn-sync-lite
python scripts/public_safety_scan.py .             # public-boundary scan
```

CI runs the same `python scripts/check_all.py` entry point
(`.github/workflows/ci.yml`) on Python 3.10, 3.11, and 3.12.

### Consolidated sources

`paper-map-lite` and `shawn-sync-lite` were consolidated here from their
standalone public repositories. The original repositories remain the
authoritative history. Source URLs, exact commits, and a SHA-256 hash for every
imported file are recorded in [Source manifest](docs/SOURCE_MANIFEST.md)
(machine-readable copy: `docs/source_manifest.json`). Only `.git`, caches,
virtualenv/build artifacts, and agent instruction files were excluded on import;
no imported source file body was modified.

## Quick start

```bash
python -m pip install -e .[dev]
python -m pytest -q
python scripts/public_safety_scan.py .
```

## Status

Early public scaffold for OpenAI/Codex OSS maintainer evidence and public-safe SHawn OSS release gates.

## Project documents

- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)
- [Public boundary](docs/PUBLIC_BOUNDARY.md)
