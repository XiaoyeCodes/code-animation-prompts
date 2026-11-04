# 投稿与补图规范

欢迎为现有风格补充参考图、修复索引或提供可运行的代码动画。提交前先确认编号，避免重复补图；不必改写原有风格提示词。

## 参考图

- 建议 1920×1080、16:9，文件名与对应提示词一致，例如 `K1_扁平矢量.jpg`。默认预览优先使用纯画面，把名称、特征说明和色板放在附加说明中，保证缩略图仍能辨认画风。
- 一张图聚焦一种画风；对比多个风格时尽量使用同一场景。现有 K1–K3 是保留的首批社区说明卡，不作为必须沿用的版式。
- 代码生成的图片请尽量附 SVG、HTML 或生成脚本，说明渲染方法、尺寸、字体和依赖。只有 JPG 时请如实标注，不能宣称已经提供可编辑源码。
- 注明作者、来源与适用许可或分享约定；原创投稿请明确是否同意仓库的免费使用、修改与分享约定。第三方作品保留各自授权与署名。不要把未经确认的素材声明成原创或统一标成 MIT。

## 来源与索引

1. 原始 `docs/source-manifest.json` 是固定基线，请勿为了让校验通过而覆盖其中的哈希。
2. 在 `skills/code-animation-prompts/references/library-changes.json` 登记新增文件或有意修改：当前 SHA-256、原因、贡献记录；修改原文件还需保留与基线一致的 `original_sha256`。
3. 把作者和来源加入技能的 `references/attribution.md`，使安装后的副本也保留署名。原包说明和许可保留原文。
4. 更新挑选器和 `_统计.json`，然后运行 `python scripts/build_catalog.py`。同步 README、SKILL 与受影响的展示图，不只修改生成脚本。

## 提交前检查

```bash
python scripts/validate_repo.py
python skills/code-animation-prompts/scripts/styles.py search 水墨 --limit 3
python skills/code-animation-prompts/scripts/styles.py show K1
```

检查新增图片在挑选器里能加载、放大、筛选；在 PR 中附预览并列出验证结果。

README 图片由 `scripts/build_visuals.py` 生成，数量自动读取目录索引。安装 Playwright 后可运行：

```bash
python scripts/build_visuals.py --browser-channel chrome --skip-video
```

此命令使用本机 Chrome，更新 PNG 并保留未改动的 GIF。不指定浏览器通道时使用 Playwright 的 Chromium；需要重建 GIF 时去掉 `--skip-video` 并确保 FFmpeg 可用。
