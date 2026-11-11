"""Unified-stack integration test: the root package and both consolidated
component packages must coexist in one import namespace and expose their
documented public API.

This is the maintenance link between the consolidated packages and the root
package: if a component package is dropped, renamed, or its public API drifts,
this test fails in the root suite.
"""
from __future__ import annotations

import importlib
import json
from pathlib import Path

import shawn_bio_search_lite
from paper_map_lite import EvidenceEdge, toy_map
from shawn_sync_lite import scan_text

ROOT = Path(__file__).resolve().parent.parent


def test_all_three_distribution_modules_import():
    for name in ("shawn_bio_search_lite", "paper_map_lite", "shawn_sync_lite"):
        assert importlib.import_module(name) is not None


def test_root_search_package_public_api():
    rows = shawn_bio_search_lite.toy_search("public metadata", limit=2)
    assert len(rows) == 2
    assert all("source" in row and "title" in row for row in rows)


def test_map_component_produces_claim_evidence_graph():
    graph = toy_map()
    assert graph["claims"][0]["id"] == "C1"
    assert graph["edges"][0]["claim_id"] == "C1"
    assert graph["edges"][0]["relation"] == "supports"
    assert EvidenceEdge("C1", "P1", "supports").note == ""


def test_coordinate_component_scanner_flags_private_absolute_paths():
    assert scan_text("clean public text") == []
    # The scanner must still detect a private host path pattern. The path is
    # assembled from parts so this test file itself does not contain a literal
    # private absolute path (the public-safety scanner would flag that).
    private_path = "/" + "home" + "/" + "someone" + "/" + "SH" + "awn" + "/file"
    assert scan_text(f"path {private_path}") != []


def test_consolidated_component_layout_and_manifest_present():
    for pkg in ("paper-map-lite", "shawn-sync-lite"):
        pkg_dir = ROOT / "packages" / pkg
        assert (pkg_dir / "pyproject.toml").is_file()
        assert (pkg_dir / "src").is_dir()
        assert (pkg_dir / "tests").is_dir()
    manifest = json.loads((ROOT / "docs" / "source_manifest.json").read_text())
    assert set(manifest) == {"paper-map-lite", "shawn-sync-lite"}
    for pkg, info in manifest.items():
        assert info["source_commit"]
        assert info["files"]
        for entry in info["files"]:
            assert len(entry["sha256"]) == 64
            assert (ROOT / entry["path"]).is_file()
