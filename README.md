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

以上 6 个基础规则会由 workflow 原样下载到 `rules/` 目录，不做解析、合并、重写或筛选。

### blackmatrix7/ios_rule_script (`release`, Clash)
- `OpenAI.yaml`
- `Anthropic.yaml`
- `Claude.yaml`
- `Copilot.yaml`
- `Telegram.yaml`
- `Netflix.yaml`
- `Disney.yaml`
- `Advertising.yaml`

### 专项服务规则（blackmatrix7/ios_rule_script）
- workflow 会直接从 `blackmatrix7/ios_rule_script` 的 `release/rule/Clash/<Rule>/<Rule>.yaml` 下载以上 8 个专项服务规则。
- 这些规则会以原始 YAML 文件形式原样保存到 `rules/` 目录，不做 YAML 解析、重写、合并、过滤或其他二次处理。
- 具体 URL 可直接从 `.github/workflows/update-rules.yml` 的下载步骤追溯。

## 仓库结构

```text
.
├─ README.md
├─ .github/workflows/update-rules.yml
├─ config/clash-verge-rules.example.yaml
└─ rules/.gitkeep
```

- `README.md`：记录同步来源、初始化步骤和后续维护方式。
- `.github/workflows/update-rules.yml`：负责定时拉取上游规则并写入 `rules/`。
- `config/clash-verge-rules.example.yaml`：提供 Clash Verge / Mihomo 的接入示例。
- `rules/.gitkeep`：仅用于保留空目录；首次运行 workflow 后会被真实同步文件填充。

## 维护方式

- 这个模板只负责“原样同步上游规则 + 提供配置引用示例”，不承担规则合并、改写或复杂生成职责。
- 日常维护优先修改 workflow 中的 URL 列表与 README 文档，不手工编辑 `rules/` 下的同步结果。
- 新仓库初始化只需保留这套目录结构并运行一次 Actions，同步后的 `rules/` 就能作为统一规则源供 Clash Verge 使用。

## 初始化检查清单

```text
1. 创建自己的 GitHub 仓库
2. 推送本模板到默认分支
3. 手动运行 Update Rules workflow
4. 确认 rules/ 目录出现同步文件
5. 按自己的仓库地址替换示例配置中的占位符
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

## 配置示例说明

- `config/clash-verge-rules.example.yaml` 仅适用于 Clash Verge / Mihomo。
- 所有 URL 都使用你自己的 GitHub 仓库占位符；接入前请统一替换 `你的用户名` 与 `你的仓库名`。
- 示例默认假设主配置里已经存在 `PROXY` 代理组；如果你的组名不同，请同步替换 `rules` 段中的目标策略组。
- `behavior: domain` 对应域名类文本规则（`private.txt`、`reject.txt`、`direct.txt`、`proxy.txt`）。
- `behavior: ipcidr` 对应 IP CIDR 文本规则（`lancidr.txt`、`cncidr.txt`）。
- `behavior: classical` 对应原始 YAML 规则（如 `OpenAI.yaml`、`Telegram.yaml`、`Advertising.yaml`）。
- `rules` 顺序示例会先拦截广告与隐私类规则，再匹配 AI / 流媒体专项规则，最后回落到基础直连 / 代理 / GEOIP / MATCH。

## 自动更新说明

- 该 workflow 支持手动触发与每日定时同步：既可以在 GitHub Actions 页面手动运行 `Update Rules`，也会按默认 cron 每天自动执行一次。
- workflow 仅申请 `contents: write` 权限，用于把同步后的 `rules/` 变更提交回仓库。
- 只有 `rules/` 有变更时才会自动提交并推送。
- 没有变更时会直接退出，不会创建空提交。
- Clash Verge 本地 `rule-providers.interval` 默认也是 `86400`。
- 两层更新链路：
  - GitHub Actions：把上游规则同步到你的仓库
  - Clash Verge：从你的仓库自动拉取最新规则

## 建议

- 想更稳：继续使用当前 `release` 分支 URL
- 想更快：只把少数 AI/流媒体规则改成 `master`
- 想更轻：如果你不需要统一入口，可以直接引用上游 URL，不必自建本仓库
