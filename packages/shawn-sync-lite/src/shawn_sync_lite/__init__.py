from __future__ import annotations
import re
from pathlib import Path

FORBIDDEN_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|token)\s*[=:]\s*['\"]?[A-Za-z0-9_\-]{20,}"),
    re.compile(r"(?i)(private db|manuscript draft|workflow/active|discord id)"),
    re.compile(r"/(home|Users)/[^\s]+/(SHawn|SHide|OneDrive|Clouds)/"),
]

def scan_text(text: str) -> list[str]:
    hits=[]
    for pat in FORBIDDEN_PATTERNS:
        if pat.search(text): hits.append(pat.pattern)
    return hits

def scan_path(path: str | Path) -> dict:
    p=Path(path)
    findings={}
    for f in p.rglob('*'):
        if f.is_file() and '.git' not in f.parts and f.stat().st_size < 500_000:
            txt=f.read_text(errors='ignore')
            h=scan_text(txt)
            if h: findings[str(f.relative_to(p))]=h
    return findings
