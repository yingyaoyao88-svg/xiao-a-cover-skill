# xiao-a-cover

一个面向 Codex 的抖音人物 IP 封面 Skill：输入标题即可生成原生 3:4 构图，并无裁剪定稿为 1080×1440 PNG。

## 使用

将仓库放入 Codex skills 目录后，可以直接说：

```text
用“小A封面图”做一张抖音封面，标题：Skill 到底是什么
```

也可以显式调用：

```text
$xiao-a-cover 标题：让 AI 按时上班；副标：设置六步 + 三个坑 + 五条法则；换一种风格
```

## 更换人物 IP

```text
python scripts/register_ip.py my-ip "我的人物IP" portrait.png --ip-root assets/ip
```

首次注册状态为 `pending_confirmation`。请先生成身份确认图，确认后再把 `profile.yaml` 的状态改为 `confirmed`。

## 隐私

公开仓库不附带小A或其他用户的私人照片、原始视频和生成输出。本机可以在 `assets/ip/xiao-a/` 保存私有小A人物包，该目录默认不会被 Git 跟踪。临时参考图不会自动注册。

## 输出约束

- 从空白画布原生生成 3:4，不把旧图裁剪为 3:4。
- `scripts/finalize_cover.py` 只做整图等比缩放，最终输出 1080×1440 PNG。
- 明显不是 3:4 的源图会被拒绝并要求重新生成。

## License

MIT

