# apply_humanizer_rules.py
"""
Systematically cleans and humanizes all thesis source files according to:
- no-ai-slop rules (anti-slop-rules.md, AGENTS.md)
- humanizer directives (banned-list.md, discourse-tells.md, rewrites.md)
"""
import re
import os

REPLACEMENTS = [
    # Banned transitions
    (r'\bFurthermore,\s*', ''),
    (r'\bFurthermore\b', 'Also'),
    (r'\bMoreover,\s*', ''),
    (r'\bMoreover\b', 'Also'),
    (r'\bAdditionally,\s*', ''),
    (r'\bAdditionally\b', 'Also'),
    (r'\bSubsequently,\s*', 'Next, '),
    (r'\bSubsequently\b', 'Next'),
    (r'\bWith that in mind,\s*', ''),
    (r'\bIt is worth noting that\s*', ''),
    (r'\bit is worth noting that\s*', ''),
    (r'\bIn conclusion,\s*', 'To summarize, '),
    
    # Banned adjectives & adverbs
    (r'\brobust\b', 'resilient'),
    (r'\bRobust\b', 'Resilient'),
    (r'\bseamlessly\b', 'directly'),
    (r'\bseamless\b', 'direct'),
    (r'\bSeamless\b', 'Direct'),
    (r'\bdelve into\b', 'examine'),
    (r'\bdelve\b', 'dig'),
    (r'\bpivotal\b', 'central'),
    (r'\bPivotal\b', 'Central'),
    (r'\btestament to\b', 'proof of'),
    (r'\ba testament to\b', 'proof of'),
    (r'\btapestry\b', 'network'),
    (r'\blandscape\b', 'environment'),
    (r'\bLandscape\b', 'Environment'),
    (r'\bparamount\b', 'essential'),
    (r'\bcutting-edge\b', 'modern'),
    (r'\bCutting-edge\b', 'Modern'),
    (r'\bparadigm shift\b', 'architectural transition'),
    (r'\bParadigm shift\b', 'Architectural transition'),
    (r'\bgame changer\b', 'major step forward'),
    (r'\bmultifaceted\b', 'varied'),
    (r'\bmeticulous\b', 'careful'),
    (r'\bmeticulously\b', 'carefully'),
    (r'\bintricate\b', 'detailed'),
    (r'\btransformative\b', 'impactful'),
    (r'\belevate\b', 'improve'),
    (r'\bembark on\b', 'start'),
    (r'\bembark\b', 'start'),
    (r'\bsupercharge\b', 'accelerate'),
    (r'\bharness the power of\b', 'use'),
    (r'\bharness\b', 'use'),
    (r'\bharnessing\b', 'using'),
    (r'\bever-evolving\b', 'changing'),
    (r'\bunderscore\b', 'highlight'),
    (r'\bunderscores\b', 'highlights'),
    (r'\bfoster\b', 'support'),
    (r'\bfostering\b', 'supporting'),
    (r'\bleverage\b', 'use'),
    (r'\bleveraging\b', 'using'),
    (r'\bleveraged\b', 'used'),
    (r'\butilize\b', 'use'),
    (r'\butilizes\b', 'uses'),
    (r'\butilized\b', 'used'),
    (r'\butilizing\b', 'using'),
    (r'\bfacilitate\b', 'enable'),
    (r'\bfacilitates\b', 'enables'),
    (r'\bfacilitated\b', 'enabled'),
    (r'\bfacilitating\b', 'enabling'),
    (r'\bempower\b', 'allow'),
    (r'\bempowers\b', 'allows'),
    (r'\bstreamline\b', 'simplify'),
    (r'\bstreamlines\b', 'simplifies'),
    (r'\bstreamlined\b', 'simplified'),
    
    # Weak verbs
    (r'\bserves as a\b', 'acts as a'),
    (r'\bacts as a\b', 'is a'),
    
    # Em dashes
    (r'—', ' - '),
    (r'–', '-'),
]

files = [
    'thesis_prelims.py',
    'thesis_ch1_ch2.py',
    'thesis_ch3_ch4.py',
    'thesis_ch5_ch6.py',
    'thesis_ch7_ch8.py',
    'thesis_ch9_refs.py',
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for pattern, repl in REPLACEMENTS:
        content = re.sub(pattern, repl, content)
    
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Cleaned banned patterns in: {fpath}')
    else:
        print(f'No banned patterns found in: {fpath}')

print('Humanizer rule pass complete.')
