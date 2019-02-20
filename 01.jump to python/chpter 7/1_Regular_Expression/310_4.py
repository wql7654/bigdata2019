import re
p = re.compile("python", re.MULTILINE) #findall과 동일한 효과

data = """python one python debug
life is too short
python two
you need python
python three
i will study python
"""

print(p.findall(data))

