#!/usr/bin/env python3
"""Validate a lightweight game's asset manifest without accessing external services."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED = {"id", "category", "version", "format", "status"}
ALLOWED_STATUS = {"placeholder", "prompt-ready", "candidate", "approved", "integrated", "verified"}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_game_manifest.py <manifest.json>")
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as exc:
        print(f"Invalid JSON: {exc}")
        return 1
    if not isinstance(data, dict):
        print("Manifest must be an object")
        return 1
    assets = data.get("assets")
    if not isinstance(assets, list):
        print("Manifest must contain an 'assets' array")
        return 1
    ids: set[str] = set()
    errors: list[str] = []
    for index, asset in enumerate(assets):
        if not isinstance(asset, dict):
            errors.append(f"assets[{index}] is not an object")
            continue
        missing = REQUIRED - asset.keys()
        if missing:
            errors.append(f"assets[{index}] missing: {', '.join(sorted(missing))}")
        for field in REQUIRED:
            if field in asset and (not isinstance(asset[field], str) or not asset[field].strip()):
                errors.append(f"assets[{index}].{field} must be non-empty text")
        asset_id = asset.get("id")
        if isinstance(asset_id, str) and asset_id in ids:
            errors.append(f"duplicate id: {asset_id}")
        if isinstance(asset_id, str):
            ids.add(asset_id)
        if not isinstance(asset.get("status"), str) or asset.get("status") not in ALLOWED_STATUS:
            errors.append(f"assets[{index}] has invalid status: {asset.get('status')}")
        if asset.get("version") not in ("A", "B", "C"):
            errors.append(f"assets[{index}] version must be A, B or C")
    if errors:
        print("Manifest invalid:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Manifest valid: {len(assets)} assets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
