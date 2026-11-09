# 安装到 Claude Code / Codex

[한국어](INSTALL.ko.md)

本仓库针对有本地文件和终端能力的 Claude Code 与 Codex。先下载完整仓库（包含原始视频约 75 MiB，另有 README 图片），安装的是 `skills/code-animation-prompts/` 整个目录。

## 一句话交给助手

[复制一键导入提示词](../prompts/one-click-import.md)。助手会下载仓库、读取说明、选择当前工具的安装位置，并验证风格查询。

## Python 安装脚本

需要 Python 3.10+，不依赖第三方包。在仓库根目录运行：

```bash
python scripts/install_skill.py --target codex
python scripts/install_skill.py --target claude
```

选择其中一条即可。`--target both` 会安装到两个位置。`--dry-run` 只显示路径，不写入文件。

| 工具 | 用户级目录 | 项目级目录 |
|---|---|---|
| Codex | `~/.agents/skills/code-animation-prompts/` | `<项目>/.agents/skills/code-animation-prompts/` |
| Claude Code | `~/.claude/skills/code-animation-prompts/` | `<项目>/.claude/skills/code-animation-prompts/` |

`~` 指用户主目录；Windows 通常是 `C:\Users\用户名`。路径按 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills) 和 [Claude Code 官方技能文档](https://code.claude.com/docs/en/skills) 整理。

安装到指定项目：

```bash
python scripts/install_skill.py --target codex --scope project --project-dir "你的项目路径"
python scripts/install_skill.py --target claude --scope project --project-dir "你的项目路径"
```

不要同时在同一助手的用户级和项目级重复安装同名技能，避免出现多个同名入口。

## 不使用 Python

手动把仓库里的 `skills/code-animation-prompts/` 整个目录复制到表中的位置。最终应存在：

```text
<安装位置>/code-animation-prompts/SKILL.md
<安装位置>/code-animation-prompts/assets/library/风格挑选.html
<安装位置>/code-animation-prompts/references/catalog.json
```

只复制 `SKILL.md` 会丢失风格库。不要改变 `assets/library/` 内文件之间的相对位置。

## 验证安装

将 `<技能目录>` 换成真实安装路径：

```bash
python "<技能目录>/scripts/styles.py" search 水墨
python "<技能目录>/scripts/styles.py" show B3
```

开始新会话后，Codex 可输入 `$code-animation-prompts`；Claude Code 可输入 `/code-animation-prompts`。也可以直接说“使用 code-animation-prompts 制作一段动画”。如果当前会话未显示新技能，重新启动会话；账户或管理员设置可能影响技能发现。

## 更新

安装脚本不覆盖已有目录。更新前保存自己的修改，将旧技能目录备份到技能扫描目录之外；然后拉取仓库并重新运行安装命令。不要把带 `SKILL.md` 的备份留在 `.agents/skills/` 或 `.claude/skills/` 下面，否则可能仍被扫描。

更新仓库中的素材索引和检查完整性：

```bash
python scripts/build_catalog.py
python scripts/validate_repo.py
```

## 可选：视频导出

安装 skill 不会自动安装浏览器或 FFmpeg。需要实际导出视频时，再按 [渲染说明](../skills/code-animation-prompts/references/rendering.md) 配置依赖。

[返回 README](../README.md)
