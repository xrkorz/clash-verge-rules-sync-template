from pathlib import Path
import re
import sys

readme = Path('README.md').read_text(encoding='utf-8')
workflow = Path('.github/workflows/update-rules.yml').read_text(encoding='utf-8')

required_rules = [
    'OpenAI', 'Anthropic', 'Claude', 'Copilot',
    'Telegram', 'Netflix', 'Disney', 'Advertising'
]

errors = []

if '### 专项服务规则（blackmatrix7/ios_rule_script）' not in readme:
    errors.append('README 缺少专项服务规则说明小节')

for name in required_rules:
    expected = f'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/release/rule/Clash/{name}/{name}.yaml'
    if expected not in workflow:
        errors.append(f'workflow 缺少 {name} 的 release/rule/Clash 下载 URL')
    if f'`{name}.yaml`' not in readme:
        errors.append(f'README 未列出 {name}.yaml')

if '原样保存到 `rules/` 目录' not in readme:
    errors.append('README 未明确写出专项服务规则会原样保存到 rules/ 目录')

if 'Keep the eight service-specific Clash YAML rules as upstream originals' not in workflow:
    errors.append('workflow 缺少专项服务规则“原样下载”注释')

if re.search(r'\b(yq|python|python3|ruby|node)\b', workflow):
    errors.append('workflow 中出现了可能的二次处理命令')

if errors:
    for error in errors:
        print(error)
    sys.exit(1)

print('US-003 service rule checks passed')
