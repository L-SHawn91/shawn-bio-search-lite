#!/usr/bin/env python3
"""Run every suite in this repository independently, then run the public-safety scans.

The unified repo holds one root package plus consolidated component packages under
``packages/``. Each suite is executed in its own pytest session so that root and
component test modules never share an import namespace, and so a failure is
attributed to exactly one package.

Usage:
    python scripts/check_all.py

Exit code 0 means every suite and every public-safety scan passed.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPONENTS = ("packages/paper-map-lite", "packages/shawn-sync-lite")


def run(label: str, cmd: list[str], cwd: Path) -> bool:
    print(f"\n=== {label} ===\n$ {' '.join(cmd)}  (cwd={cwd.relative_to(ROOT) if cwd != ROOT else '.'})", flush=True)
    proc = subprocess.run(cmd, cwd=cwd)
    return proc.returncode == 0


def main() -> int:
    py = sys.executable
    results: list[tuple[str, bool]] = []

    # 1. Root suite (root package under src/).
    results.append(("root suite", run("root suite", [py, "-m", "pytest", "-q", "tests"], ROOT)))

    # 2. Component suites, each in its own pytest session and its own project root.
    for component in COMPONENTS:
        pkg = ROOT / component
        results.append((f"{component} suite", run(f"{component} suite", [py, "-m", "pytest", "-q", "tests"], pkg)))

    # 3. Public-safety scans: the root scanner covers the whole tree (including the
    #    imported component packages), then each package scanner re-checks its own tree.
    results.append(("root public-safety scan", run("root public-safety scan", [py, "scripts/public_safety_scan.py", "."], ROOT)))
    for component in COMPONENTS:
        pkg = ROOT / component
        results.append((f"{component} public-safety scan", run(f"{component} public-safety scan", [py, "scripts/public_safety_scan.py", "."], pkg)))

    print("\n=== summary ===")
    for label, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}\t{label}")
    failed = [label for label, ok in results if not ok]
    if failed:
        print(f"\nFAILED: {', '.join(failed)}")
        return 1
    print("\nALL_CHECKS_PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
