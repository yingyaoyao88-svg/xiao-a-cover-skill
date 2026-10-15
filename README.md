# xiao-a-cover

[![CI](https://github.com/yingyaoyao88-svg/xiao-a-cover-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/yingyaoyao88-svg/xiao-a-cover-skill/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

一个面向 Codex / Antigravity 的抖音人物 IP 封面 Skill：输入标题即可生成原生 3:4 构图，并无裁剪定稿为 1080×1440 PNG。

## 特性

- **原生 3:4 画布**：严格从空白画布生成 3:4 纵横比，拒绝粗暴裁剪或补边拉伸。
- **人物 IP 体系**：支持固化本地人物 IP，也可在单次对话中传入临时人物参考图。
- **高画质定稿**：内置定稿脚本通过高质量 Lanczos 算法精确等比缩放至 1080×1440 PNG 规格。
- **防重复与风格多变**：支持多视觉维度切换（构图骨架、配色家族、排版位置）。
- **隐私保护**：公开仓库与 Git 默认忽略用户私有人像、原视频及产出图。

## 安装

### 环境要求

- Python 3.10 或更高版本（推荐使用 Python 3.12）
- [Pillow](https://python-pillow.org/) >= 11.0, < 12.0

### 安装步骤

把仓库克隆到 Codex / Antigravity 的 skills 目录，并安装依赖：

```bash
# 1. 克隆仓库
git clone https://github.com/yingyaoyao88-svg/xiao-a-cover-skill.git xiao-a-cover
cd xiao-a-cover

# 2. 安装基础依赖
python -m pip install -r requirements.txt

# 或者通过 pyproject.toml 安装项目
python -m pip install -e .
```

## 使用说明

### 1. 自然语言调用

将仓库放入 skills 目录后，可以直接用自然语言触发：

```text
用“小A封面图”做一张抖音封面，标题：Skill 到底是什么
```

### 2. 显式 Skill 调用

支持输入标题、副标题、风格、人物 IP 等多项参数：

```text
$xiao-a-cover 标题：让 AI 按时上班；副标：设置六步 + 三个坑 + 五条法则；换一种风格
```

带系列与期数的场景：

```text
$xiao-a-cover 标题：Prompt 高级调试手册；系列：AI 进阶课；期数：第 03 期；ip：tech-host
```

### 3. 命令行工具使用

#### 封面定稿脚本 (`finalize_cover.py`)

用于校验源图比例并无损等比缩放为 1080×1440 PNG：

```bash
python scripts/finalize_cover.py source.png output/cover.png

# 允许自定义宽高比误差容差并允许覆盖已有文件
python scripts/finalize_cover.py raw_output.png output/cover.png --tolerance 0.005 --overwrite
```

#### 人物 IP 注册脚本 (`register_ip.py`)

长期使用新人物 IP 时进行注册：

```bash
python scripts/register_ip.py my-ip "我的人物IP" portrait.png --ip-root assets/ip
```

## 更换人物 IP

长期使用新人物时，运行注册命令：

```bash
python scripts/register_ip.py my-ip "我的人物IP" portrait.png --ip-root assets/ip
```

首次注册状态为 `pending_confirmation`。请先生成身份确认图，确认后再把 `profile.yaml` 的状态改为 `confirmed`。

当前任务也可以直接附上一张临时人物参考图。临时图只用于本次封面，不会复制进 Skill 或推送到 GitHub。

## 输出约束

- 从空白画布原生生成 3:4，不把旧图裁剪为 3:4。
- `scripts/finalize_cover.py` 只做整图等比缩放，最终输出 1080×1440 PNG。
- 明显不是 3:4 的源图会被拒绝并要求重新生成。
- 文字要求：主标题与副标题必须清晰可读，禁止出现随机乱码、无关英文或未经授权的水印。

## 隐私

公开仓库不附带小A或其他用户的私人照片、原始视频和生成输出。本机可以在 `assets/ip/xiao-a/` 保存私有小A人物包，该目录默认不会被 Git 跟踪。临时参考图不会自动注册。

## 开发与测试

### 安装开发依赖

```bash
# 安装开发环境依赖 (pytest, ruff)
python -m pip install -e ".[dev]"
```

### 运行单元测试

项目内置完整的测试套件：

```bash
# 使用 pytest
pytest tests/

# 或使用 Python 自带 unittest
python -m unittest discover tests
```

### 代码检查

```bash
ruff check .
```

## 项目结构

```text
xiao-a-cover-skill/
├── .github/workflows/ci.yml  # GitHub Actions CI 工作流
├── agents/                   # Agent 定义配置
├── assets/ip/                # 人物 IP 资源库（默认忽略私有 IP）
├── references/               # 提示词规范、视觉风格系统与 IP 指南
├── scripts/                  # 核心脚本工具
│   ├── finalize_cover.py     # 封面验证与定稿缩放 (1080x1440)
│   └── register_ip.py        # 人物 IP 包注册与管理
├── tests/                    # 单元测试用例
├── .gitignore
├── .python-version           # Python 版本声明 (3.12)
├── LICENSE                   # MIT 开源许可证
├── pyproject.toml            # PEP 518/621 项目元数据与依赖
├── requirements.txt          # 项目依赖
├── README.md                 # 项目文档
└── SKILL.md                  # Skill 技能规范定义
```

## License

[MIT](LICENSE)
