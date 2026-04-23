from pathlib import Path
import sys
import yaml

readme = Path('README.md').read_text(encoding='utf-8')
config_text = Path('config/clash-verge-rules.example.yaml').read_text(encoding='utf-8')
config = yaml.safe_load(config_text)

errors = []
providers = config.get('rule-providers', {})
rules = config.get('rules', [])

if '## 配置示例说明' not in readme:
    errors.append('README 缺少“配置示例说明”小节')

required_readme_phrases = [
    '仅适用于 Clash Verge / Mihomo',
    '所有 URL 都使用你自己的 GitHub 仓库占位符',
    '示例默认假设主配置里已经存在 `PROXY` 代理组',
    '`behavior: domain` 对应域名类文本规则',
    '`behavior: ipcidr` 对应 IP CIDR 文本规则',
    '`behavior: classical` 对应原始 YAML 规则',
    '先拦截广告与隐私类规则，再匹配 AI / 流媒体专项规则，最后回落到基础直连 / 代理 / GEOIP / MATCH',
]
for phrase in required_readme_phrases:
    if phrase not in readme:
        errors.append(f'README 缺少说明：{phrase}')

if not providers:
    errors.append('配置缺少 rule-providers')
if not rules:
    errors.append('配置缺少 rules 顺序示例')

placeholder = 'https://raw.githubusercontent.com/你的用户名/你的仓库名/main/rules/'
for name, provider in providers.items():
    url = provider.get('url', '')
    if not url.startswith(placeholder):
        errors.append(f'{name} 未使用个人仓库占位 URL')

expected_behaviors = {
    'private': 'domain',
    'reject': 'domain',
    'direct': 'domain',
    'proxy': 'domain',
    'lancidr': 'ipcidr',
    'cncidr': 'ipcidr',
    'OpenAI': 'classical',
    'Anthropic': 'classical',
    'Claude': 'classical',
    'Copilot': 'classical',
    'Telegram': 'classical',
    'Netflix': 'classical',
    'Disney': 'classical',
    'Advertising': 'classical',
}
for name, behavior in expected_behaviors.items():
    actual = providers.get(name, {}).get('behavior')
    if actual != behavior:
        errors.append(f'{name} 的 behavior 应为 {behavior}，实际为 {actual}')

expected_rules = [
    'RULE-SET,private,DIRECT',
    'RULE-SET,reject,REJECT',
    'RULE-SET,Advertising,REJECT',
    'RULE-SET,OpenAI,PROXY',
    'RULE-SET,Anthropic,PROXY',
    'RULE-SET,Claude,PROXY',
    'RULE-SET,Copilot,PROXY',
    'RULE-SET,Telegram,PROXY',
    'RULE-SET,Netflix,PROXY',
    'RULE-SET,Disney,PROXY',
    'RULE-SET,direct,DIRECT',
    'RULE-SET,proxy,PROXY',
    'RULE-SET,lancidr,DIRECT',
    'RULE-SET,cncidr,DIRECT',
    'GEOIP,LAN,DIRECT',
    'GEOIP,CN,DIRECT',
    'MATCH,PROXY',
]
if rules != expected_rules:
    errors.append('rules 顺序示例与预期不一致')

if errors:
    for error in errors:
        print(error)
    sys.exit(1)

print('US-005 config example checks passed')
