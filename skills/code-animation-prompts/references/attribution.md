# 素材与许可

本技能封装的是随项目提供的「代码动画_341种风格提示词_免费」素材包。原作者的说明、提示词、示例与许可保留在 `../assets/library/`。XiaoyeCodes 负责本仓库的技能封装、检索／安装／渲染脚本和展示文档，不将素材包中的全部作品声明为自己的原创。

- [原始说明](../assets/library/说明.md)：免费使用、免费转发；禁止将这些内容包装成课程、付费 skills 或其他收费内容出售。
- [原始来源说明](../assets/library/许可与来源.md)：原整理者对自制／改写部分的说明。
- [Lemo-Opuscar](../assets/library/第三方许可/Lemo-Opuscar_LICENSE.txt)：MIT，Copyright (c) 2026 LemoLab。
- [mg-styles-15](../assets/library/第三方许可/mg-styles-15_LICENSE.txt)：MIT，Copyright (c) 2026 Vincentwei1021。
- [code-video](../assets/library/第三方许可/code-video_LICENSE.txt)：MIT，Copyright (c) 2026 Bae-ChangHyun。

感谢原素材整理者——哔哩哔哩 [**俯仰观照**](https://space.bilibili.com/3690990015613855/?spm_id_from=333.788.upinfo.detail.click) 的资源分享。

## 社区补充与原包基线

- **Strange Leo (@strangeyu911-tech)**：通过 [PR #1](https://github.com/XiaoyeCodes/code-animation-prompts/pull/1) 提供 K1 扁平矢量、K2 Q 版、K3 卡哇伊三张 1920×1080 JPEG 参考说明卡。这些是社区新增作品，不是原包自带的图片。
- 作者说明图片通过 SVG 绘制并渲染，但 PR 只提交 JPEG，未附 SVG 源文件；本仓库不把 JPEG 宣称为可编辑的矢量源码。
- 原始素材包含 193 张静帧；加上社区补图后，当前目录有 196 张。原包 `说明.md` 中的 193 保留为历史原文，当前数量以 `catalog.json` 与挑选器为准。
- 仓库的 `docs/source-manifest.json` 保留原始 555 个文件的哈希基线，不用当前文件重新覆盖它。[library-changes.json](library-changes.json) 记录两处有意修改（挑选器、统计）及三张新增图片的哈希、来源和原因，并随技能安装。校验分别核对原始未改动文件、登记的修改与新增素材。

不同来源的内容保留各自许可。免费分享约定不改写第三方 MIT 文本；整个合集不能简单标成全部 MIT。电影、艺术风格与示例名称是参考描述，不代表官方合作或背书。
