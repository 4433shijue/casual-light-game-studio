"""Copy a bundled engine starter into a new directory; never overwrite a project."""
import argparse
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('engine', choices=['godot', 'phaser'])
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / 'assets' / 'starters' / args.engine
    target = args.output.resolve()
    try:
        if target == source or source in target.parents:
            raise ValueError('Output cannot be inside the bundled starter')
        shutil.copytree(source, target, ignore=shutil.ignore_patterns('.godot', 'node_modules', '__pycache__'))
    except (OSError, ValueError) as exc:
        print(f'Not created: {exc}')
        return 1
    print(f'Created {args.engine} starter: {target}; dependencies have not been installed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
