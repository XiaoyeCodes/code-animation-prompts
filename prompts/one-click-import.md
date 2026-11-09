# 一键导入提示词

[한국어](one-click-import.ko.md)

复制下面整段到有本地文件与终端权限的 Claude Code 或 Codex。

```text
请将 https://github.com/XiaoyeCodes/code-animation-prompts 安装为当前编程助手可用的 skill。

1. 将仓库下载到合适的本地目录；若已有同名目录，先检查内容，不覆盖已有改动。
2. 阅读 README.md、docs/INSTALL.md 和 skills/code-animation-prompts/SKILL.md。
3. 根据当前助手选择安装目标：Codex 使用 ~/.agents/skills/code-animation-prompts，
   Claude Code 使用 ~/.claude/skills/code-animation-prompts。
   在仓库根目录运行 python scripts/install_skill.py --target codex 或 --target claude。
   如果当前助手无法确定，只向我确认目标；不要擅自安装到两个位置。
4. 安装时保留完整 skill 文件夹，包括 assets/library 中全部提示词、静帧、HTML、
   示例视频和许可文件。若目标已存在，保留现有目录并报告，不自动删除或覆盖。
5. 执行已安装目录中的 scripts/styles.py search 水墨，确认可查到风格；
   再执行 scripts/styles.py show B3，确认能读取完整提示词。
6. 告诉我实际安装路径、如何调用，以及是否需要新开会话。
   最后给我一句可以直接使用的“12 秒粒子聚形动画”请求示例。

本次只安装风格 skill，不自动安装视频渲染依赖、不修改其他助手配置。
```

[返回 README](../README.md)
