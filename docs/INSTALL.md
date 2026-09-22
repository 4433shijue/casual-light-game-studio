# 安装说明

先把完整资料包交给智能体。模板和脚本还在里面，别只带走封面。

## 让智能体安装

如果你的工具支持从 GitHub 安装 Skill，可以直接发这段话。

```text
请安装 https://github.com/4433shijue/casual-light-game-studio 这个 Skill。
仓库根目录包含 SKILL.md，请保留 references、assets、scripts 和 agents 目录。
安装前检查同名技能；如果我已有本地修改，请先说明差异，保留我的内容。
```

不同工具的安装目录和菜单可能不同，按当前工具的说明处理。安装后让它确认能找到 `casual-light-game-studio` 并读取主文件；没有识别到时，重新开启一个会话，再按常见问题排查。

## 手动下载

1. 在仓库页面点击 `Code`，再选择 `Download ZIP`。
2. 解压后找到直接包含 `SKILL.md` 的那一层。
3. 将该目录命名为 `casual-light-game-studio`，连同内部文件放入你的智能体支持的技能目录。
4. 按该工具的方式启用或调用技能。

有 Git 的读者也可以下载源码。

```bash
git clone https://github.com/4433shijue/casual-light-game-studio.git
```

克隆只会下载仓库。自动识别技能仍由你的智能体决定。

## 先不安装也能试

把仓库放到智能体能读取的工作区，告诉它读取根目录的 `SKILL.md` 后回答你的小游戏需求。引用资料时应按需读取，暂时不用把整个文件夹塞进一条聊天消息。

## 更新

没有本地修改的 Git 克隆可以运行下面的命令。

```bash
git pull --ff-only
```

如果修改过模板或指令，先保存自己的改动并查看差异。ZIP 用户下载新版后，也要先比较再替换。辛苦改好的规则值得留下，不必献祭给更新按钮。

## 开发环境

- Python 工具需要 Python 3.10+，只用标准库。Windows 可把命令里的 `python` 换成 `py -3`。
- Godot 模板面向 Godot 4，当前有 4.6.3 的无界面验证记录。
- Phaser 模板固定依赖 3.90.0，需要 Node/npm 安装依赖，再通过本地 HTTP 服务打开。不要双击 HTML。

仅使用策划、案例和提示词时，可以暂时不安装这些开发环境。模板也不会偷偷替你下载引擎。

## 升级到 v1.2.1

从 [版本发布页](https://github.com/4433shijue/casual-light-game-studio/releases/tag/v1.2.1) 下载 `casual-light-game-studio-v1.2.1.zip`。先备份安装目录里你自己改过的内容，再用 ZIP 中的完整 `casual-light-game-studio` 文件夹更新安装。

本次新增数值推演与作品交付参考，只换 `SKILL.md` 会缺少引用文件。更新后按所用智能体的方式重新加载技能，再试试使用示例中的局部改名请求。本次不需要迁移游戏代码或存档。

## 单独安装游戏文案工作室

只需要文案时，下载同一 Release 下的 game-copywriting-studio-v1.2.1.zip，安装包内 game-copywriting-studio 完整目录。也可从仓库 standalone/game-copywriting-studio 路径安装。它不需要主 Skill 或额外写作 Skill。

小游戏工作室的安装方式保持不变，自带全部文案参考。无需安装两个才能使用文案功能；需要独立调用入口时再安装文案版。两个入口同时安装也不要求相互调用。

## 维护者构建

共享文案方法、案例和模板只修改主包对应文件。运行 `python scripts/build_copywriting_skill.py` 同步独立副本；用 `--check` 只检查一致性。需要 ZIP 时加 `--output` 指向源目录之外的新目录，可配合 `--version 1.2.1`。生成的两个 ZIP 都能独立使用，主包也包含独立入口的资料副本以保持仓库说明链接有效。

安装用户不用运行构建工具。主包通过自身参考文件使用文案能力，不依赖嵌套技能被自动发现；需要直接调用独立入口时安装独立 ZIP。
