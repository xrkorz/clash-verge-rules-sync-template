# Task Plan

## Goal
- 在本轮仅实现 `prd.json` 中一个 `passes: false` 且 `priority` 最小的 story，并完成校验、落盘、提交。

## Constraints
- 仅做一个 story。
- 必须遵循 `scripts/ralph/CLAUDE.md`、`scripts/ralph/CODEX.md` 与用户指令。
- 同步产物位于 `rules/`，不手工维护生成内容。
- 若无正式 typecheck，至少做可解析性/配置有效性校验。

## Phases
- [x] 读取技能说明并确认项目目录/约束
- [x] 建立 planning-with-files 落盘文件
- [x] 读取 PRD/进展并选定目标 story
- [x] 校验或切换 git 分支
- [x] 实现目标 story
- [x] 运行质量检查
- [x] 更新 PRD / progress.txt / 如有必要更新 AGENTS.md
- [x] 提交改动

## Notes
- 采用最小可执行改动，避免混入无关修改。

## Errors Encountered
- 暂无


### Phase 12: Ralph 单 Story 实现迭代（US-003）
- [x] 核对目标 story、分支与仓库边界
- [x] 先写最小失败校验覆盖专项服务规则说明缺口
- [x] 以最小改动补齐专项服务规则文档/注释
- [x] 运行 YAML 与 story 校验并记录结果
- [x] 回写 `scripts/ralph/prd.json` / `scripts/ralph/progress.txt`
- [x] 提交最小化变更
- **Status:** complete
