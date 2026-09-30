---
name: xiao-a-cover
description: Generate 3:4 Douyin cover images from Chinese titles with a prominent replaceable person IP. Use for Xiao A covers, tutorial-series covers, or requests to continue or change a cover style; do not use for ordinary non-person posters, horizontal article art, or video editing.
---

# 生成小A封面图

把标题直接变成可发布的竖版抖音封面。主角默认是本地已确认的 `xiao-a` IP；也可使用当前请求中的临时人物参考图或其他已确认 IP 包。

## 输入

从自然语言中提取：

- `title`：必填，逐字保留。
- `subtitle`、`series`、`episode`：可选；用户给出的文字逐字保留。
- `ip`：可选，默认 `xiao-a`。
- `style`：可选；“换风格”必须更换至少三项视觉维度。
- `reference_images`：可选，仅用于当前任务，除非用户明确要求注册，否则不得复制进 Skill。
- `output_dir`：可选，默认 `<current-project>/output/xiao-a-covers/<slug>/`。

只有标题时直接生成，不追问非必要参数。自动补一条简短、不重复标题的副标，并在交付时说明它是自动生成内容。

## 工作流

1. 选择人物来源，优先级为：当前临时参考图、用户指定的已确认 IP、本地 `xiao-a`。若都不可用，明确要求用户提供人物图或运行注册脚本，不擅自换成陌生人物。
2. 需要读取、创建或确认人物包时，阅读 [references/ip-pack.md](references/ip-pack.md)。
3. 需要自动选型或响应“换风格”时，阅读 [references/style-system.md](references/style-system.md)，并查看最近 `cover-meta.json` 避免连续重复版式。
4. 构建生成指令时阅读 [references/prompt-patterns.md](references/prompt-patterns.md)。使用图像生成工具从空白画布原生生成 3:4 竖图；人物图只作为身份参考，不作为待裁剪底图。
5. 检查人物身份、脸部、手部、构图、标题、副标、额外乱码、水印与缩略图可读性。单一问题做定向修正，最多两次；不得无限重试。
6. 运行 `scripts/finalize_cover.py`。它只接受接近 3:4 的源图，并整图缩放为 1080×1440 PNG；比例不合格必须重新生成，禁止裁剪、补边或拉伸。
7. 写入 `cover-meta.json`：标题字段、IP、视觉家族、构图骨架、生成时间、提示词摘要、源尺寸和最终尺寸。
8. 显示成品，返回绝对路径。若仍存在文字或人物问题，明确标注，不声称已经通过验收。

## 必须保持

- 主标题、副标题、系列名、期数和英文大小写与用户输入一致。
- 不添加随机英文、伪界面文字、随机数字或水印。
- 人物是画面主体，标题在手机缩略图下仍清晰。
- 成品精确为 1080×1440 PNG，原始构图为 3:4。
- 公开仓库与远程提交不得包含用户原始照片、视频或未经明确授权公开的人像参考图。

## 人物注册

长期使用新人物时，运行：

```text
python scripts/register_ip.py <slug> "<显示名>" <参考图...> --ip-root assets/ip
```

新人物初始状态是 `pending_confirmation`。先生成身份确认样图，只有用户确认后才把状态改为 `confirmed`。临时人物图不执行注册命令。
