# 人物 IP 包

只在选择、注册、更新或确认人物 IP 时读取。

## 目录契约

```text
assets/ip/<slug>/
├── profile.yaml
└── references/
    ├── reference-01.png
    └── ...
```

`slug` 只允许小写英文字母、数字和连字符，长度 1–63。`profile.yaml` 至少包含：

```yaml
id: person-slug
display_name: 显示名
status: pending_confirmation
references:
  - references/reference-01.png
identity_notes: []
wardrobe_preferences: []
avoid: []
```

状态只能是 `pending_confirmation` 或 `confirmed`。未确认人物不能作为稳定默认身份源。

## 选择规则

1. 当前请求中的临时参考图。
2. 用户明确指定且状态为 `confirmed` 的人物包。
3. 本地 `xiao-a` 且状态为 `confirmed`。

若本地没有 `xiao-a`，不要换成陌生人物。请用户提供临时参考图，或通过 `scripts/register_ip.py` 注册自己的 IP。

## 隐私边界

- 临时参考图仅用于当前生成，不能自动复制、注册、提交或推送。
- 注册只复制用户明确选择的文件；初始状态始终待确认。
- 不从照片推断种族、健康、宗教、政治、性取向等敏感属性。
- 公开仓库只放匿名示例配置。原始照片、视频与本地私有 IP 应由 `.gitignore` 排除。

## 身份确认

注册后生成一张不带营销文字的清晰半身确认图。用户明确确认相似度后，才能把 `status` 改为 `confirmed`。身份变化较大时保留原参考图，并再次确认，不静默覆盖。

