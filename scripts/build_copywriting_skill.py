"""Maintainer tool: synchronize shared copywriting resources, check and package both skills."""
import argparse
from pathlib import Path
import re
import zipfile

SHARED = ('references/game-copywriting.md', 'references/character-and-context.md',
          'assets/templates/game-lexicon.md')
NOTICE = '<!-- Generated from the main skill resource at {path}; use scripts/build_copywriting_skill.py to update. -->\n\n'

def expected(root, name):
    return (NOTICE.format(path=name) + (root / name).read_text(encoding='utf-8')).encode('utf-8')

def files(folder):
    return sorted(p for p in folder.rglob('*') if p.is_file()
                  and not any(x in ('.git', '__pycache__', 'node_modules', '.godot') for x in p.relative_to(folder).parts))

def check_links(folder, members):
    allowed = {p.resolve() for p in members}
    for p in members:
        if p.suffix != '.md':
            continue
        for link in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
            if '://' in link or link.startswith('#'):
                continue
            target = (p.parent / link.split('#')[0]).resolve()
            if target not in allowed:
                raise ValueError(f'Link outside packaged files: {p.name} -> {link}')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check without rewriting shared resources')
    parser.add_argument('--output', type=Path, help='New directory for deterministic ZIP files')
    parser.add_argument('--version', default='1.2.1')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    standalone = root / 'standalone/game-copywriting-studio'
    try:
        if not re.fullmatch(r'\d+\.\d+\.\d+', args.version):
            raise ValueError('Version must have three numeric components')
        if args.output:
            destination = args.output.resolve()
            if destination == root or root in destination.parents:
                raise ValueError('Archive output must be outside the skill source')
            if destination.exists():
                raise ValueError('Archive output already exists')
        for name in SHARED:
            target = standalone / name
            content = expected(root, name)
            if args.check:
                if not target.exists() or target.read_text(encoding='utf-8') != content.decode('utf-8'):
                    raise ValueError(f'Shared resource drift: {name}')
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
        for folder in (root, standalone):
            check_links(folder, files(folder))
        if args.output:
            destination.mkdir(parents=True, exist_ok=False)
            # Main archive includes the nested standalone source to preserve repository links.
            for folder in (root, standalone):
                archive = destination / f'{folder.name}-v{args.version}.zip'
                with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
                    for p in files(folder):
                        info = zipfile.ZipInfo(folder.name + '/' + p.relative_to(folder).as_posix(), (2020, 1, 1, 0, 0, 0))
                        info.compress_type = zipfile.ZIP_DEFLATED
                        info.external_attr = 0o100644 << 16
                        z.writestr(info, p.read_bytes())
        print('Shared resources and self-contained links checked' + ('; archives created' if args.output else ''))
        return 0
    except (OSError, ValueError) as error:
        print(f'Not built: {error}')
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
