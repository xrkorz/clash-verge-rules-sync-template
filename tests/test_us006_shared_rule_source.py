from pathlib import Path
import sys
import yaml

readme = Path('README.md').read_text(encoding='utf-8')
config = yaml.safe_load(Path('config/clash-verge-rules.example.yaml').read_text(encoding='utf-8'))
providers = config.get('rule-providers', {})

errors = []

if '## 多设备统一规则源' not in readme:
    errors.append('README 缺少“多设备统一规则源”小节')

required_phrases = [
    '所有设备都应指向同一组来自你自己仓库的规则 URL',
    '上游规则仓库 → 你的 GitHub 仓库 → Clash Verge 客户端',
    '不需要在每台设备上分别保存上游原始规则文件',
    '不需要在每台设备上各自运行同步脚本',
]
for phrase in required_phrases:
    if phrase not in readme:
        errors.append(f'README 缺少说明：{phrase}')

placeholder = 'https://raw.githubusercontent.com/你的用户名/你的仓库名/main/rules/'
urls = [provider.get('url', '') for provider in providers.values()]
if not urls:
    errors.append('配置示例缺少 rule-providers URL')
elif any(not url.startswith(placeholder) for url in urls):
    errors.append('配置示例并非全部指向统一的个人仓库 URL 前缀')

if errors:
    for error in errors:
        print(error)
    sys.exit(1)

print('US-006 shared rule source checks passed')
