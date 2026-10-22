# 小A 3D 爆款人物 IP 封面 Skill (`xiao-a-cover`) 🎨

<div align="center">

<a href="https://imaomyying.com/#/project/xhs-cover-gen" target="_blank">
  <img src="https://img.shields.io/badge/🌐_在线演示与产品介绍展示页-Live_Showcase_&_Interactive_Studio-ff2442?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Live Showcase & Interactive Studio" />
</a>

<br/>
<br/>

[![CI](https://github.com/yingyaoyao88-svg/xiao-a-cover-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/yingyaoyao88-svg/xiao-a-cover-skill/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776ab.svg?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex_Skill-Native-8b5cf6.svg?style=flat-square)](https://github.com/features/actions)
[![Output Spec](https://img.shields.io/badge/Output_Spec-3:4_(1080×1440)-ff2442.svg?style=flat-square)](#-输出规范与画质保障)
[![Scaling](https://img.shields.io/badge/Scaling-Lanczos_Algorithm-0ea5e9.svg?style=flat-square)](#-命令行工具使用)

**面向 Codex / Antigravity 的高点击率人物 IP 封面自动化生成 Skill**  
*原生 3:4 构图 · 角色特征锁死 · 四大戏剧化场景 · 双行 3D 立体排版 · 1080×1440 Lanczos 质感定稿*

---

### 🌐 [点击进入产品在线介绍展示页 (Live Interactive Showcase)](https://imaomyying.com/#/project/xhs-cover-gen)
可在展示页内自由切换**四大戏剧化创意场景**、实时定制**双行 3D 立体标题与配色**，并一键复制调试运行指令！

---

</div>

## 💡 为什么需要这个 Skill？

在小红书、抖音等以竖版视觉流为主的自媒体平台中，**封面点击率（CTR）直接决定了内容的生死**。然而，普通自媒体创作者与技术博主在封面制作上面临以下痛点：
1. **人物角色易“漂移”**：通用生图大模型在每次生成时极易发生换脸、五官比例变形、发型穿搭失控，无法稳定建立个人视觉品牌；
2. **构图粗暴裁切导致变形**：很多工具先生存 1:1 或 16:9 宽图再强制裁切成 3:4，画面主体断头、核心字样被截断、边缘畸变严重；
3. **制作繁琐耗时**：每期内容在选题立项后，光构思场景、PS 修图、调光合成、排版 3D 文字就要消耗 1 小时以上，严重拖慢日更节奏。

**`xiao-a-cover-skill`** 专为解决上述问题而设计。将个人 IP「小A」的角色资产与经过实战检验的高点击率视觉模型彻底固化，**输入标题与文案，60 秒内即可自动化输出一张原生 3:4（1080×1440 PNG）的 3D 爆款封面**！

---

## 🌟 核心特性与设计规范

### 1. 原生 3:4 画布（拒绝二次裁切）
从第一帧 Prompt 阶段即严格指定 `3:4` 竖版构图（Aspect Ratio: 3:4），不从正方形或横图补边拉伸，保证主体透视与远景景深的自然统一。

### 2. 人物 IP 资产包固化（反漂移系统）
- 内置固化的小A人物特征提示词与干净基准人像；
- 严格锁定「大头小身 Q 版比例」、「标志性利落短发与圆框眼镜」、「简约极客卫衣」；
- 支持在单次对话中临时传入外部人像，也支持通过专用脚本注册永久本地 IP。

### 3. 双行蓝白 3D 立体排版体系
- **上行（引子 / 动词）**：吸引视线，如「让 AI 按时上班」、「拆解 50 个开源神器」；
- **下行（量化钩子 / 利益点）**：承接核心价值，如「实测6步设置 · 避开3个致命坑」；
- **视觉风格**：采用加粗无衬线字体，白面黑底带 3D 蓝光/橙光立体挤压（Extruded Bevel），标题占画面宽度 80%~85%，保证手机端单列/双列瀑布流中 0.5 秒内极速抓人眼球。

### 4. 严苛隐私防外流机制
开源仓库与 Git 规则默认将所有用户私有人像、临时工作流生成图与视频素材加入 `.gitignore`，杜绝任何个人肖像资产被意外推送到公共代码库。

---

## 🎬 四大签名级戏剧化场景 (Signature Scenarios)

| 场景代码 | 场景名称 | 视觉风格与环境构成 | 适用内容场景 |
| :--- | :--- | :--- | :--- |
| `zero-gravity` | **失重零重力浮空** 🌌 | 人物处于失重悬浮态，周围漂浮发光 iPad、AI 芯片模型、书本与能量光环，蓝灰科技景深。 | AI 工具评测、大模型进阶、生产力爆发指南 |
| `map-pin` | **巨型地图打卡** 📍 | 人物脚踩 3D 浮雕城市等高线地标底座，身后插立发光的巨型立体地图图钉与导航箭头。 | 学习路线全景图、避坑指南、从 0 到 1 实操复盘 |
| `torn-paper` | **撕纸破次元弹窗** 📄 | 背景为 2D 黑白极简线稿草图，边缘呈现逼真的立体撕裂厚度，饱满鲜艳的 3D 小A破纸跃出。 | 效率翻倍揭秘、非共识观点、打破传统认知 |
| `cyber-hud` | **未来全息科技** 🏙️ | 赛博霓虹边缘冷暖光对比，半透明悬浮代码面板与发光数据流环绕，未来科技感拉满。 | 复杂技术架构、开源工作流解析、独立开发实录 |

---

## 🛠️ 安装与环境准备

### 环境要求
- **Python**: `>= 3.10`（推荐 Python 3.11 或 3.12）
- **Pillow**: `>= 11.0, < 12.0`

### 安装步骤

将本仓库克隆至 Codex / Antigravity 的 `skills/` 插件目录中：

```bash
# 1. 克隆仓库
git clone https://github.com/yingyaoyao88-svg/xiao-a-cover-skill.git xiao-a-cover
cd xiao-a-cover

# 2. 安装基础依赖
python -m pip install -r requirements.txt

# 3. 本地可编辑模式安装
python -m pip install -e .
```

---

## 🚀 使用与调用方式

### 方式一：自然语言对话触发
Skill 注册生效后，在任何支持 Codex / Antigravity 的对话环境中直接输入：

```text
用“小A封面图”做一张小红书封面，标题：让 AI 按时上班；副标：实测6步设置+3个避坑核心点
```

### 方式二：显式 Skill 指令参数调用
支持精准指定副标、场景、色调家族、期数与指定人物 IP：

```bash
$xiao-a-cover 标题："Prompt 高级调试手册" 副标："从新手到高手的5条法则" 场景："失重零重力浮空" 配色："电光青" 系列："AI 进阶课" 期数："第 03 期"
```

### 方式三：命令行工具脚本 (CLI Tools)

#### 1. 封面无损定稿脚本 (`scripts/finalize_cover.py`)
专门负责校验生成原图的宽高比（3:4，容差 0.005），并调用高质量 Lanczos 滤波器等比缩放为 **1080×1440 PNG**：

```bash
# 标准定稿
python scripts/finalize_cover.py source_raw.png output/cover_final.png

# 指定容差并强制覆盖
python scripts/finalize_cover.py source_raw.png output/cover_final.png --tolerance 0.005 --overwrite
```

#### 2. 新人物 IP 注册脚本 (`scripts/register_ip.py`)
若需要长期沉淀并切换新的团队角色或品牌吉祥物：

```bash
python scripts/register_ip.py designer-b "设计师小B" portrait_sample.png --ip-root assets/ip
```
首次注册状态为 `pending_confirmation`。生成测试效果确认无误后，把 `profile.yaml` 的状态变更为 `confirmed` 即可固化生效。

---

## 📐 输出规范与画质保障

| 维度 | 行业常规做法 | 本 Skill 规范 |
| :--- | :--- | :--- |
| **画布比例** | 1:1 或 16:9 二次硬裁剪 | **原生 3:4 构图，零边缘拉伸** |
| **最终分辨率** | 模糊不规则分辨率 | **精确 1080 × 1440 像素** |
| **文件格式** | 易产生噪点的 JPG | **无损高质量 PNG** |
| **重采样算法** | 普通双线性插值 (Bilinear) | **高精细度 Lanczos 滤波** |
| **标题排版** | 平面粗糙贴字 | **双行 3D 挤压倒角与高光投影** |

---

## 📁 仓库目录结构

```text
xiao-a-cover/
├── SKILL.md                 # Antigravity / Codex Skill 核心调用元规范
├── pyproject.toml           # 项目工程配置与依赖声明
├── requirements.txt         # 核心 Python 运行时依赖
├── assets/
│   └── ip/                  # 固化人物 IP 特征包与 profile.yaml (私有素材已忽略)
├── scripts/
│   ├── finalize_cover.py    # 1080×1440 PNG Lanczos 定稿缩放脚本
│   └── register_ip.py       # 人物 IP 注册与状态更新脚本
└── tests/
    └── test_finalize.py     # 比例容差与缩放算法单元测试
```

---

## 🤝 参与贡献与建议

欢迎提交 Pull Request 增加更多实战场景与排版模版！
1. Fork 本项目到你的 GitHub
2. 创建分支：`git checkout -b feature/new-scenario`
3. 提交代码与测试用例
4. 发起 Pull Request

---

## 💬 交流与合作

欢迎扫码添加作者微信（微信号：`15038098595`，添加请备注 GitHub 项目名），交流 AI 视觉生图、IP 固化设计、自媒体自动化工作流或探讨商业合作：

<div align="center">
  <img src="https://imaomyying.com/wechat-qrcode.jpg" width="220" alt="小A 微信二维码" />
  <p><b>扫码添加作者微信好友（微信号：15038098595）</b></p>
</div>

---

## 📄 开源协议

本项目基于 [MIT License](LICENSE) 协议开源。

---

<div align="center">
  <sub>Crafted with 💖 by <a href="https://imaomyying.com">@AomyYing (小A)</a> · 让每一个好想法都有爆款封面</sub>
</div>
