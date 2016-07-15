import re

content = ''
with open('resource/toc.html', 'r', encoding='utf-8') as f:
    content = f.read()

p1 = r'src="(.*?)"'
p2 = r'href="(.*?)"'

r1 = re.findall(p1, content)
r2 = re.findall(p2, content)

print(r1 + r2)