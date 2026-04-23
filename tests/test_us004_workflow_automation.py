from pathlib import Path
import re
import sys

readme = Path('README.md').read_text(encoding='utf-8')
workflow = Path('.github/workflows/update-rules.yml').read_text(encoding='utf-8')

errors = []

if 'workflow_dispatch:' not in workflow:
    errors.append('workflow 缺少手动触发 workflow_dispatch')

schedule_match = re.search(r'cron:\s*"([^"]+)"', workflow)
if not schedule_match:
    errors.append('workflow 缺少 schedule cron 配置')
else:
    cron = schedule_match.group(1)
    if '/2' in cron or '/3' in cron or '/7' in cron:
        errors.append('cron 频率看起来不是至少每日一次')

if 'permissions:\n  contents: write' not in workflow:
    errors.append('workflow 未限制为仅 contents: write 权限')

required_lines = [
    'git add rules README.md',
    'git diff --cached --quiet && exit 0',
    'git commit -m "chore: update rules"',
    'git push',
]
for line in required_lines:
    if line not in workflow:
        errors.append(f'workflow 缺少提交步骤关键语句: {line}')

if '支持手动触发与每日定时同步' not in readme:
    errors.append('README 未明确说明支持手动触发与每日定时同步')

if '只有 `rules/` 有变更时才会自动提交并推送' not in readme:
    errors.append('README 未明确说明仅在 rules/ 变更时才自动提交并推送')

if '没有变更时会直接退出，不会创建空提交' not in readme:
    errors.append('README 未明确说明无变更时不会创建空提交')

if 'workflow 仅申请 `contents: write` 权限' not in readme:
    errors.append('README 未明确说明 workflow 只申请 contents: write 权限')

if errors:
    for error in errors:
        print(error)
    sys.exit(1)

print('US-004 workflow automation checks passed')
