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
