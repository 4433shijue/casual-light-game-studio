# 最小项目模板与工具

> 使用定位：本资料仅供启发与按需取用，可改写、组合或跳过。用户与智能体的创意决定方案；示例类型、数值、流程和结构不构成创作限制。技术操作的真实前提、执行授权与验证诚实性仍需遵守。

仅在用户已经选定技术栈、并要求落地时使用。默认方案阶段不创建工程。Godot 与 Phaser 两个模板都是“20 秒点击 5 个目标”的教学骨架，数字是演示配置，不是用户项目需求。支持鼠标/触控、暂停、成功/失败、重玩及本地最佳成绩；关卡参数与表现分开。已有项目先分析入口，仅移植必要模块，不能覆盖整个工程。

HTML 模板是无目标的色带互动，展示统一指针输入、键盘操作、暂停、重置和横竖窗口重排。它不带第三方库、网络、存档或音频。三个模板只演示局部实现方法，不规定成品的玩法、UI 或方向。

## 创建与运行

从技能根目录运行（Python 3.10+，只有标准库）：

```text
python scripts/create_starter.py html /path/to/new-html-project
python scripts/create_starter.py godot /path/to/new-project
python scripts/create_starter.py phaser /path/to/new-project
```

目标目录必须不存在。脚本复制模板，不安装依赖、不运行构建、不连接账号。失败后保留现场，换新目录重试或由用户决定清理。

HTML 模板可直接复制 `assets/starters/html/index.html`，不运行脚本也能使用。双击在浏览器打开，拖动或点选画布后按方向键，空格切换暂停，R 重置。暂停时重置仍保持暂停；系统偏好减少动态效果时初始暂停，可自行继续。横屏示例把说明放侧面，窄屏改到上方，这只是一个可替换的布局。

Godot 模板面向 Godot 4。用编辑器导入 `project.godot` 后运行；或 `godot --path /path/to/new-project`。导出前按目标平台配置导出模板与预设，包中未伪造平台导出配置。

Phaser 模板固定 Phaser 3.90.0，采用原生 ES module + 本地 npm 包，无 Vite 构建层。先检查 Node/npm，再在项目目录运行 `npm install`，然后 `python -m http.server 8080 --bind 127.0.0.1`，打开 `http://127.0.0.1:8080`。不要双击 HTML。发布时复制 HTML、src 和 Phaser 运行文件，或按项目需要迁移到已验证的构建工具并锁定依赖。首次安装需要网络；游戏本身不依赖 CDN。

## 移植指南

- 输入：Phaser 使用统一 pointer；Godot 使用 Button 的 GUI 输入，避免额外监听造成双击计分。
- UI：Godot 与 Phaser 示例使用顶部状态和底部控制，HTML 示例采用侧栏或上方说明。它们都可以替换；根据实际玩家动作安排空间，修改后检查目标方向、遮挡及指针坐标。
- 状态：计时示例暂停不扣时，结束后不再计分；重玩完整恢复时间、分数和目标。
- 内容：Godot 与 Phaser 可修改 `level` 参数改变目标数、时长和目标位置；扩展关卡时采用稳定 ID，不使用数组位置当存档身份。
- 存档：HTML 无存档，Godot 与 Phaser 仅存最佳成绩。损坏/不可写时仍可游玩；需跨局进度时增加 schemaVersion、迁移与备份，不能直接沿用示例成绩结构。
- 摄像机：当前为固定逻辑画布。只有空间探索才增加跟随、边界与死区；不要为点击游戏强加摄像机移动。
- 资产：几何占位可直接替换，但需保持命中区、锚点和可读性。替换后重新试玩。

## 文档与任务生成

填写 [项目简报样例](../assets/templates/brief.example.json)，运行：

```text
python scripts/generate_game_docs.py brief.json new-docs
```

生成 `design.md`、`tasks.md`、`playtest.md`。任务来自简报中的真实模块、依赖和验收条目，脚本只整理，不凭空设计玩法。拒绝缺失任务依赖、循环依赖和覆盖已有目录。样例只演示格式；空白试玩记录不能被当作已通过。

## 技术资料

- [Phaser 输入](https://docs.phaser.io/phaser/concepts/input)
- [Phaser 画布适配](https://docs.phaser.io/phaser/concepts/scale-manager)
- [Godot 命令行](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html)

这些链接是按需查阅来源。使用不同版本或导出平台时核验对应官方接口与环境，不能从本文推断全部平台已经通过测试。
