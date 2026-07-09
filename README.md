# shawn-bio-search-lite

Search layer: public scholarly metadata adapters for PubMed, Europe PMC, OpenAlex, and Crossref. No private PDFs, corpora, manuscripts, credentials, or internal workflow state.

## SHawn OSS stack role

```text
Search: shawn-bio-search-lite
Map: paper-map-lite
Report: SHawn-EvidenceMap
Coordinate: shawn-sync-lite
Execute safely: newbrain-router
QA docs: shawn-docx-qa / SHawn-hwp
Present: SHawn-WEB
```

## Public boundary

This repository is a clean public-safe projection. It contains only schemas, templates, toy data, public metadata adapters, mock executors, and public reports.

It must not contain private databases, private manuscripts, PDFs, private corpora, local/internal paths, Discord identifiers, workflow logs, memory exports, credentials, or private project state.

## Quick start

```bash
python -m pip install -e .[dev]
python -m pytest -q
python scripts/public_safety_scan.py .
```

## Status

Early public scaffold for OpenAI/Codex OSS maintainer evidence and public-safe SHawn OSS release gates.
