# 项目规则

- 全中文沟通与说明。
- `rules/` 目录中的同步文件视为上游产物，不手工编辑；需要调整内容时，优先修改 `.github/workflows/update-rules.yml` 中的来源 URL。
- 本仓库只做“原样下载 + 提交变更”，不要在 workflow 中加入 YAML 解析、规则合并、过滤或重写逻辑。
- 如果仓库没有正式 typecheck，至少执行 YAML 可解析性/配置有效性校验，并把结果写入 `scripts/ralph/progress.txt`。
- 新增或调整专项服务规则时，要同时保持 `README.md` 的规则清单说明、workflow 中的下载 URL，以及 `tests/` 下对应 story 校验脚本三者同步。
