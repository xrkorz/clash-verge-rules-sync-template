# clash-verge-rules-sync-template

适用于 **Clash Verge / Clash Verge Rev / Mihomo** 的最小规则聚合模板仓库。

## 目标

- 使用 GitHub Actions 定时同步上游规则
- 不 fork 上游仓库，不重跑生成链，不做二次加工
- Clash Verge 只引用你自己的仓库地址，便于长期维护

## 同步来源

### Loyalsoldier/clash-rules (`release`)
- `private.txt`
- `reject.txt`
- `direct.txt`
- `proxy.txt`
- `lancidr.txt`
- `cncidr.txt`

### blackmatrix7/ios_rule_script (`release`, Clash)
- `OpenAI.yaml`
- `Anthropic.yaml`
- `Claude.yaml`
- `Copilot.yaml`
- `Telegram.yaml`
- `Netflix.yaml`
- `Disney.yaml`
- `Advertising.yaml`

## 仓库结构

```text
.
├─ .github/workflows/update-rules.yml
├─ config/clash-verge-rules.example.yaml
└─ rules/
```

## 使用步骤

1. 新建 GitHub 仓库，例如 `my-clash-verge-rules`
2. 把本模板全部内容推到你的仓库默认分支（建议 `main`）
3. 打开 GitHub 仓库的 **Actions**
4. 手动运行一次 `Update Rules`
5. 等待 `rules/` 目录生成同步后的规则文件
6. 打开 `config/clash-verge-rules.example.yaml`
7. 把其中所有 `你的用户名` 和 `你的仓库名` 改成你自己的值
8. 将该配置片段并入 Clash Verge 主配置

## Clash Verge 说明

- Clash Verge 使用的是 Mihomo 兼容配置格式
- 本模板中的 `rule-providers` / `rules` 可直接用于 Clash Verge
- 你需要保证主配置中存在 `PROXY` 代理组；如需分流更细，可以改成你自己的组名

## 自动更新说明

- GitHub Actions 默认每天运行一次
- Clash Verge 本地 `rule-providers.interval` 默认也是 `86400`
- 两层更新链路：
  - GitHub Actions：把上游规则同步到你的仓库
  - Clash Verge：从你的仓库自动拉取最新规则

## 建议

- 想更稳：继续使用当前 `release` 分支 URL
- 想更快：只把少数 AI/流媒体规则改成 `master`
- 想更轻：如果你不需要统一入口，可以直接引用上游 URL，不必自建本仓库
