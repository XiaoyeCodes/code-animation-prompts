<div align="center">

<img src="docs/images/hero.png" alt="Code Animation Prompts — 341 种代码动画风格" width="100%">

# Code Animation Prompts

**从一句创意，到一段有风格的代码动画。**

341 种风格提示词 · 196 张参考静帧 · 10 个系列 · Claude Code & Codex Skill

[![Styles](https://img.shields.io/badge/styles-341-b7f47b?style=flat-square&labelColor=161d28)](docs/STYLES.md)
[![Stills](https://img.shields.io/badge/reference_stills-196-86b7ff?style=flat-square&labelColor=161d28)](docs/images/style-gallery.png)
[![Skill](https://img.shields.io/badge/Agent_Skill-Claude_Code_%26_Codex-e6ceaa?style=flat-square&labelColor=161d28)](skills/code-animation-prompts/SKILL.md)
[![Sharing](https://img.shields.io/badge/sharing-free-ecb7cc?style=flat-square&labelColor=161d28)](LICENSE.md)

[浏览全部风格](docs/STYLES.md) · [一键导入](#一键导入claude-code--codex) · [手动安装](docs/INSTALL.md) · [原始示例](skills/code-animation-prompts/assets/library/示例) · [来源与许可](LICENSE.md)

</div>

## 先看风格

粒子、霓虹、水墨、剪纸、漫画、电影感……把喜欢的画面交给 AI，再用代码把它动起来。

![12 种风格的真实参考静帧](docs/images/style-gallery.png)

以上图片来自素材包自带的参考静帧，编号与提示词一一对应。**196 种有图，145 种为文字参考**；静帧展示视觉方向，实际动画取决于内容、实现和渲染结果。

| 想做什么 | 可以从这里开始 |
|---|---|
| 温暖的粒子叙事／片头 | **B3** 粒子聚形、**B2** 萤火光尘 |
| 国风片头／节日短片 | **Z5** 剪纸、**Z1** 水墨、**Z8** 敦煌 |
| 科技感／赛博城市 | **R1** 霓虹雨夜、**R5** 像素赛博、**R6** 东方赛博 |
| 科普／知识讲解 | **M1** 白板手绘讲解、**L10** 工程方案比较墙 |
| 漫画短片／有冲击力的表达 | **R3** 美式漫画、**X7** 英雄漫画 |
| 杂志式排版／电影视觉参考 | **H1** Biennale Yellow、**O** 系列 |

## 它包含什么

| 组成 | 你可以用它做什么 |
|---|---|
| **完整原始素材库** | 阅读 341 份 Markdown 提示词，查看静帧、参考实现与原始示例 |
| **离线风格挑选器** | 搜索、按类别筛选、放大图片、勾选风格、导出已选清单 |
| **可安装 Agent Skill** | 让 Claude Code／Codex 按需读取风格，规划镜头并制作代码动画 |
| **轻量检索脚本** | 按编号、关键词、系列查找；不必把整个素材库塞进上下文 |
| **浏览器渲染工具** | 将提供时间接口的 HTML 逐帧导出为 MP4，可混入已有音频 |
| **一键导入提示词** | 复制到有本地文件和终端权限的 Claude Code／Codex，完成下载与安装 |

## 一键导入：Claude Code / Codex

**复制下面整段，粘贴给 Claude Code 或 Codex：**

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

也可打开 [独立版导入提示词](prompts/one-click-import.md) 复制。这里的“一键导入”指把整段请求交给编程助手执行；普通网页聊天如果没有本地文件权限，无法代你安装。

<details>
<summary><b>更喜欢自己运行命令？</b></summary>

需要 Git 和 Python 3.10+。在终端执行：

```bash
git clone https://github.com/XiaoyeCodes/code-animation-prompts.git
cd code-animation-prompts

# 安装给 Codex
python scripts/install_skill.py --target codex

# 或安装给 Claude Code
python scripts/install_skill.py --target claude

# 两者都安装
python scripts/install_skill.py --target both
```

安装脚本仅复制文件，不下载额外依赖。已有同名技能时会停止，保留现有内容。项目级安装、没有 Python 时的复制方式见 [安装说明](docs/INSTALL.md)。

</details>

## 装好以后，直接这样说

**Codex：**

```text
使用 $code-animation-prompts，用 B3 粒子聚形做一段 12 秒横屏动画。
主题是“把想法变成现实”，依次呈现灵感、构建、完成三个阶段。
1920×1080，30 fps，深色背景配暖金色粒子，带中文字幕，无声。
请交付可编辑 HTML、关键帧预览和 MP4；若缺少渲染依赖，请明确说明。
```

**Claude Code：**

```text
/code-animation-prompts 用 Z5 剪纸做一段 12 秒的新年片头，16:9。
文字是“新的一年，万事可期”，红纸、米色宣纸、层叠阴影。
先做可编辑 HTML 和关键帧，声音先不加；环境具备依赖时导出 MP4。
```

**还没选好风格：**

```text
用 code-animation-prompts 帮我做一条讲“为什么下雨”的 30 秒科普短片。
面向小学生，竖屏 9:16，中文大字幕，想要手绘和温暖的感觉。
先给我 3 个有编号的候选风格，说明怎么动，再推荐一个。
```

技能提供风格参考与制作流程，视频仍需由编程助手编写并在本地渲染。只查风格不需要 API Key 或付费图像服务；助手本身的使用费用由相应平台决定。

## 用眼睛挑，比描述更快

![原始离线挑选器项目截图](docs/images/style-picker.png)

下载完整仓库后，双击打开：

```text
skills/code-animation-prompts/assets/library/风格挑选.html
```

在 Chrome／Edge 中可离线浏览。搜索关键词或编号 → 勾选风格 → 打开「已选清单」→ 复制给助手，再补充主题、时长、画幅和声音需求。

请保留它与 `风格提示词/` 的相对位置。GitHub 文件页面展示的是 HTML 源码，下载后在浏览器打开才能使用挑选器。

<details>
<summary>查看搜索状态截图</summary>

![按 R1 搜索的项目截图](docs/images/picker-search.png)

</details>

## 从原始示例看看动画

![B6 原始示例视频的节选动图](docs/images/b6-preview.gif)

*上图从素材包内 B6 示例视频节选，无声预览。原始文件名中的模型标注来自素材包，不代表本仓库另行进行过模型对比测试。*

| 示例 | 文件 |
|---|---|
| **B6 光速穿梭 · 爆炸 · 重聚** | [完整提示词](skills/code-animation-prompts/assets/library/示例/B6_光速穿梭·爆炸·重聚_同一份提示词/提示词.md) · [原始 HTML 与 2 个 MP4](skills/code-animation-prompts/assets/library/示例/B6_光速穿梭·爆炸·重聚_同一份提示词) |
| **X7 英雄漫画** | [一句话提示词](skills/code-animation-prompts/assets/library/示例/X7_英雄漫画_只给一句话/提示词.md) · [原始 HTML 与 MP4](skills/code-animation-prompts/assets/library/示例/X7_英雄漫画_只给一句话) |

**B6 是独立示例，不计入 341 个风格条目。** 原始 3 个 MP4、3 个示例 HTML 与过程截图均随仓库保留。

## 341 种风格怎么分

| 系列 | 数量 | 侧重点 |
|---|---:|---|
| A–G · 代码样片 | 26 | 字、粒子、线与墨、光与天气、图形与纸、讲解、质感 |
| M · 动态风格 | 40 | 整段视频怎么动、怎么剪、怎么讲 |
| K · 卡通画风 | 38 | 角色与画面的视觉语言 |
| Z · 中国风 | 15 | 水墨、工笔、剪纸、皮影、敦煌等 |
| H · 现成版式 | 12 | 配色与字体的成套搭配 |
| L · Lemo-Opuscar | 59 | 含完整做法的多类型风格 |
| V · mg-styles-15 | 15 | 动态图形风格 |
| X · code-video | 31 | 代码视频风格 |
| R · 照参考学来的 | 7 | 用代码呈现的赛博朋克等视觉参考 |
| O · 奥斯卡 98 部 | 98 | 按原素材整理的电影画风参考 |
| **合计** | **341** | **193 张静帧 + 148 份文字参考** |

→ [打开完整风格索引，每个条目均可点击](docs/STYLES.md)

## 导出你自己的视频

查找风格、阅读提示词和使用挑选器，不需要渲染依赖。只有使用随附 HTML → MP4 工具时，需要 **Playwright + Chromium + FFmpeg**。

```bash
python -m pip install playwright
python -m playwright install chromium
ffmpeg -version

# 用随附的时间接口示例验证环境
python skills/code-animation-prompts/scripts/render_video.py skills/code-animation-prompts/assets/starter/index.html --output output/demo.mp4 --duration 12 --fps 30 --width 1920 --height 1080
```

`ffmpeg -version` 是检查命令；如未安装，参见 [FFmpeg 官方下载](https://ffmpeg.org/download.html)。渲染器要求页面提供 `window.renderAt(t)` 并在 `?export=1` 时关闭实时循环；原始示例需要先适配这个接口，不能直接当成通用网页录屏器。具体见 [渲染接口与音频说明](skills/code-animation-prompts/references/rendering.md)。

## 仓库结构

```text
code-animation-prompts/
├── README.md
├── LICENSE.md                       # 各部分的来源与使用约定
├── prompts/one-click-import.md       # 复制给 Claude Code / Codex 的导入请求
├── docs/
│   ├── INSTALL.md                   # 安装位置、项目安装、更新方式
│   ├── STYLES.md                    # 341 个可点击条目
│   ├── images/                      # 封面、风格墙、真实项目截图、动图
│   └── source-manifest.json         # 原始 555 个文件的 SHA-256 清单
├── scripts/                         # 安装、索引生成、预览图生成、校验
└── skills/code-animation-prompts/
    ├── SKILL.md                     # 技能入口
    ├── agents/openai.yaml           # Codex 展示信息
    ├── references/                  # 风格索引、渲染与来源说明
    ├── scripts/                     # 检索与视频导出
    └── assets/
        ├── starter/index.html       # 新增的确定性动画接口示例
        └── library/                 # 完整原始「代码动画」文件夹
            ├── 风格挑选.html
            ├── 风格提示词/
            ├── 示例/
            ├── 第三方许可/
            ├── _统计.json
            ├── 说明.md
            └── 许可与来源.md
```

## 致谢与免费分享约定

感谢原素材整理者——哔哩哔哩 [**俯仰观照**](https://space.bilibili.com/3690990015613855/?spm_id_from=333.788.upinfo.detail.click) 的资源分享。

同时感谢 **LemoLab（Lemo-Opuscar）**、**Vincentwei1021（mg-styles-15）**、**Bae-ChangHyun（code-video）**。XiaoyeCodes 在原素材基础上增加技能封装、工具脚本和项目文档；原始素材与许可完整保留。

**免费使用，免费分享；请勿把这个合集包装成付费课程、付费 skills 或其他收费内容出售。** 第三方内容继续适用其各自许可，详见 [来源与许可](LICENSE.md)。本仓库没有把所有素材重新声明为 MIT。

---

<div align="center">

**选一种风格，写下你的故事，让代码动起来。**

如果这个项目对你有帮助，欢迎 Star，也欢迎分享你的代码动画作品。

</div>
