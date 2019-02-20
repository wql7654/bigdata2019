import re
p = re.compile("\w+\spython$", re.MULTILINE)

data = """python one python debug
life is too short
python two
you need python
python three
i will study python
"""

print(p.findall(data))