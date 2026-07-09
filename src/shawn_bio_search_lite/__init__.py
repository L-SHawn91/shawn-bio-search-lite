from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Iterable, List

@dataclass
class PublicPaper:
    source: str
    title: str
    year: int | None = None
    doi: str | None = None
    url: str | None = None
    abstract: str | None = None

def toy_search(query: str, limit: int = 5) -> list[dict]:
    """Return deterministic toy metadata for demos/tests. Real adapters must use public APIs only."""
    q = query.strip() or "example"
    rows = [
        PublicPaper("toy-pubmed", f"Public metadata result for {q}", 2026, "10.0000/example", "https://pubmed.ncbi.nlm.nih.gov/"),
        PublicPaper("toy-openalex", f"Open scholarly graph result for {q}", 2025, None, "https://openalex.org/"),
    ]
    return [asdict(r) for r in rows[:limit]]
