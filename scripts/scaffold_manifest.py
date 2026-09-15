#!/usr/bin/env python3
"""Create a starter asset manifest for a new lightweight game."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Path for the new manifest.json")
    parser.add_argument("--game", default="new-game", help="Game identifier")
    args = parser.parse_args()
    if args.output.exists():
        print(f"Refusing to overwrite existing file: {args.output}")
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "game": args.game,
        "version": "A",
        "assets": [
            {
                "id": "A-01-player-placeholder",
                "category": "character",
                "version": "A",
                "format": "svg",
                "status": "placeholder",
            },
            {
                "id": "A-02-background-placeholder",
                "category": "background",
                "version": "A",
                "format": "svg",
                "status": "placeholder",
            },
        ],
    }
    try:
        with args.output.open("x", encoding="utf-8") as stream:
            stream.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    except OSError as exc:
        print(f"Not created: {exc}")
        return 1
    print(f"Created manifest with {len(data['assets'])} starter assets: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
