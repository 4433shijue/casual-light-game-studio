"""Render a validated project brief into design, ordered tasks and an untested playtest sheet."""
import argparse
import json
from pathlib import Path


def render(data):
    if not isinstance(data, dict):
        raise ValueError('Brief must be an object')
    for key in ('name', 'goal', 'platform'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'{key} must be non-empty text')
    experience_key = 'experience' if 'experience' in data else 'loop'
    experience = data.get(experience_key)
    if not isinstance(experience, str) or not experience.strip():
        raise ValueError(f'{experience_key} must be non-empty text')
    if data.get('tier') not in ('A', 'B', 'C'):
        raise ValueError('tier must be A, B or C')
    excluded = data.get('out_of_scope', [])
    if not isinstance(excluded, list) or any(not isinstance(x, str) for x in excluded):
        raise ValueError('out_of_scope must be an array of strings')
    modules = data.get('modules')
    if not isinstance(modules, list) or not modules:
        raise ValueError('modules must be a non-empty array')
    indexed = {}
    for module in modules:
        if not isinstance(module, dict):
            raise ValueError('Each module must be an object')
        for key in ('id', 'title'):
            if not isinstance(module.get(key), str) or not module[key].strip():
                raise ValueError(f'module {key} must be non-empty text')
        if module['id'] in indexed:
            raise ValueError('Duplicate module id')
        for key in ('depends_on', 'acceptance'):
            value = module.get(key)
            if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
                raise ValueError(f'{key} must be an array of non-empty strings')
        if not module['acceptance']:
            raise ValueError('Each module needs acceptance criteria')
        indexed[module['id']] = module
    ordered, pending = [], dict(indexed)
    for module in modules:
        if any(dep not in indexed for dep in module['depends_on']):
            raise ValueError('Unknown dependency')
    while pending:
        ready = [key for key, module in pending.items() if all(dep not in pending for dep in module['depends_on'])]
        if not ready:
            raise ValueError('Dependency cycle')
        for key in ready:
            ordered.append(pending.pop(key))
    design = f"# {data['name']}\n\n状态：方案草稿，尚未实现或验证\n\n目标：{data['goal']}\n\n体验结构或核心循环：{experience}\n\n版本：{data['tier']}\n\n平台：{data['platform']}\n\n## 不做范围\n\n"
    design += '\n'.join('- ' + item for item in excluded) + '\n'
    tasks = '# 开发任务\n\n按依赖顺序排列，以下均未执行。\n'
    for module in ordered:
        tasks += f"\n## {module['id']} · {module['title']}\n\n依赖：{', '.join(module['depends_on']) or '无'}\n\n"
        tasks += '\n'.join('- [ ] ' + item for item in module['acceptance']) + '\n'
    return design, tasks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('brief', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    try:
        design, tasks = render(json.loads(args.brief.read_text(encoding='utf-8-sig')))
        playtest = (Path(__file__).resolve().parents[1] / 'assets/templates/playtest.md').read_text(encoding='utf-8')
        args.output.mkdir(parents=True, exist_ok=False)
        for name, content in [('design.md', design), ('tasks.md', tasks), ('playtest.md', playtest)]:
            with (args.output / name).open('x', encoding='utf-8') as stream:
                stream.write(content)
    except (OSError, ValueError) as exc:
        print(f'Not generated: {exc}')
        return 1
    print(f'Created three planning documents: {args.output}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
