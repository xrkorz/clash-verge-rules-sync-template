from pathlib import Path
import json
import sys

readme = Path('README.md').read_text(encoding='utf-8')
agents = Path('AGENTS.md').read_text(encoding='utf-8')
workflow = Path('.github/workflows/update-rules.yml').read_text(encoding='utf-8')
prd = json.loads(Path('scripts/ralph/prd.json').read_text(encoding='utf-8'))

errors = []

if '## 低维护成本约束' not in readme:
    errors.append('README 缺少“低维护成本约束”小节')

required_readme_phrases = [
    '新增规则源时，只需要补充 workflow 里的下载 URL 和 README 中的对应说明',
    '移除规则源时，只需要删除对应 URL 与文档条目，不需要改动额外的生成链路',
    '切换上游 URL 时，不需要重构仓库结构',
    '不要把这个仓库扩展成复杂的规则生成系统',
]
for phrase in required_readme_phrases:
    if phrase not in readme:
        errors.append(f'README 缺少说明：{phrase}')

if '涉及低维护成本的 story，应优先通过修改 workflow URL 列表与 README 文档完成新增/删除/切换规则源，避免引入额外生成链路或仓库结构重构。' not in agents:
    errors.append('AGENTS.md 缺少低维护成本的复用规则')

for forbidden in ['yq', 'python', 'python3', 'node', 'jq']:
    if forbidden in workflow:
        errors.append(f'workflow 不应引入复杂生成命令：{forbidden}')

story = next((item for item in prd['userStories'] if item['id'] == 'US-007'), None)
if not story:
    errors.append('scripts/ralph/prd.json 缺少 US-007')
else:
    if '不扩展为复杂规则生成系统' not in story.get('notes', ''):
        errors.append('scripts/ralph/prd.json 未在 US-007 notes 中明确禁止复杂规则生成系统')

if errors:
    for error in errors:
        print(error)
    sys.exit(1)

print('US-007 low maintenance checks passed')
