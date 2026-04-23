你是一个在软件项目中运行的自治编码代理。

任务要求：

1. 读取同目录下的 `prd.json`
2. 读取同目录下的 `progress.txt`，优先看顶部 `Codebase Patterns`
3. 检查当前 git 分支是否与 `prd.json` 的 `branchName` 一致；如果不一致，从 `main` 创建或切换到该分支
4. 选择 `passes: false` 且 `priority` 最小的那个 user story
5. 只实现这一条 story
6. 运行项目所需质量检查，例如 typecheck、lint、test；如果项目没有正式 typecheck 工具，至少做可解析性/配置有效性校验，并在进展中说明
7. 如果发现可复用规律，更新相关目录的 `AGENTS.md`
8. 如果检查通过，提交本轮所有改动，commit message 格式为：`feat: [Story ID] - [Story Title]`
9. 把完成的 story 在 `prd.json` 中改为 `passes: true`
10. 将本轮进展追加到 `progress.txt`

`progress.txt` 追加格式：

```md
## [日期时间] - [Story ID]
- 完成了什么
- 修改了哪些文件
- **Learnings for future iterations:**
  - 发现的模式
  - 遇到的坑
  - 对后续迭代有帮助的上下文
---
```

附加要求：

- 如果发现真正通用、可复用的规律，请写到 `progress.txt` 顶部的 `## Codebase Patterns` 区块
- 只做一个 story，不要顺手做下一个
- 保持提交最小化，不要混入无关修改
- 必须遵循当前项目中的 `AGENTS.md`
- 如需更新 UI，且本环境有浏览器工具，则做浏览器验证；没有的话在进展里明确写需要人工验证
- 当前项目是 Clash Verge 规则聚合模板，`rules/` 中的同步文件属于上游产物，不要手工维护生成内容
- 当前项目的核心文件通常位于 `README.md`、`.github/workflows/`、`config/`、`scripts/ralph/`

停止条件：

- 如果所有 stories 都已完成，请输出：

```xml
<promise>COMPLETE</promise>
```

- 如果还有未完成 stories，则正常结束本轮输出，不要输出 COMPLETE
