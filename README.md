# 小A人物 IP 封面 Skill

当前版本：2.1，样式目录版本 3。首次上传自己的三视图，接着选择喜欢的风格，再用标题生成原生 3:4、1080×1440 的真人封面。四种方案在风格、排版、色调和互动方式上分别设计，不再统一套用暖白黑橙模板。

## 首次使用

1. 上传自己的正面、侧面、背面三视图，一张拼图或三张图片均可。
2. 检查人物一致性后，选择 A–D 样式。
3. 提供标题与可选副标题，生成封面。

有效人物和样式仅需初始化一次；之后直接给新标题。换人物时重新导入，人物三视图和配置保存于仓库外的本地目录。公开示例中的作者面容不作为默认人物。

## 四种风格、排版与色调展示

四张示例使用相同标题「codex实战落地用法」，可点击查看 1080×1440 原图。

| A · 暖白黑橙科技 | B · 暗紫电影质感 |
| :---: | :---: |
| <a href="docs/showcase/codex-touch-screen.png"><img src="docs/showcase/codex-touch-screen.png" width="320" alt="暖白黑橙：左上平面科技大标题，右侧真人触控任务卡" /></a> | <a href="docs/showcase/codex-result-in-hand.png"><img src="docs/showcase/codex-result-in-hand.png" width="320" alt="暗紫电影：居中真人、紫色成果光效、底部大标题" /></a> |
| 明亮平面科技排版，暖白、黑、鲜橙。 | 深紫黑与紫白光效，居中人像、主标题置底。 |
| **C · 薄荷绿极简** | **D · 酒红复古拼贴** |
| <a href="docs/showcase/codex-command-desk.png"><img src="docs/showcase/codex-command-desk.png" width="320" alt="薄荷绿极简：俯视薄荷工作台、左侧三行深绿标题" /></a> | <a href="docs/showcase/codex-cross-screen-drag.png"><img src="docs/showcase/codex-cross-screen-drag.png" width="320" alt="酒红复古拼贴：真人剪贴、杂志字阶、底部奶油白撕纸字带" /></a> |
| 薄荷白、鼠尾草绿，俯视工作台与三行字阶。 | 酒红、奶油白，复古字形、撕纸和真人剪贴。 |

这些成品经作者授权公开展示。作者三视图和原视频仅保存在本地，不随仓库提供。使用者需上传自己的三视图，衣服、发型和配饰以使用者的参考为准。

## 安装与调用

克隆本仓库为 Codex 技能目录中的 xiao-a-cover 文件夹。配置了 CODEX_HOME 时使用其 skills 目录，否则使用 ~/.codex/skills。刷新技能列表或新开会话后调用：

```text
使用 $xiao-a-cover 制作封面，标题：用AI搭建一个个人网站。
```

首次调用先要求上传三视图，再展示四种互动效果供选择；不会擅自替用户选定风格。已经上传和选择的内容不重复询问。要求“四种都做”时生成四张单独成品。

人物资产与 active-profile.json 默认存放在 ~/.agents/xiao-a-cover/，不写入此仓库。

## 运行依赖与尺寸导出

运行环境需有图像生成工具；本仓库不包含生图模型、API 密钥或作者身份资产。尺寸导出需要 Python 3.10+ 和 Pillow。

```text
python -m pip install -r requirements.txt
python scripts/finalize_cover.py source.png cover.png
```

先生成原生 3:4，再整图缩放至 1080×1440 PNG。不裁剪、不补边，不合格比例需重新生成；已有目标文件默认不覆盖。

## 验证与公开打包

```text
python -m unittest discover -s tests -v
python scripts/package_public.py ../xiao-a-cover-public.zip
```

打包器只接受明确清单中的文件。四张授权展示图按固定路径和 SHA-256 校验，其它人物照片、三视图、视频、本地配置和旧压缩包会被拒绝。新增展示图应先获得授权并更新明确清单。

## 文件入口

- SKILL.md：首次导入、样式选择与封面生成流程。
- references/onboarding.md：三视图检查、仓库外保存和样式状态。
- references/styles.md：四种互动场景的人物动作、镜头与验收要求。
- references/prompt-patterns.md：使用者三视图与互动场景的提示词结构。
- docs/showcase/：四张授权成品和图片说明。
- scripts/：尺寸导出与公开包检查。

代码许可见 [LICENSE](LICENSE)。展示图用于效果说明，不代替使用者自己的身份参考。
