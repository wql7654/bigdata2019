import re

p=re.compile("ca?t") # 0또는 1만 적용이된다.
a=p.match('ct')
print(a)
a=p.match('cat')
print(a)
a=p.match('caat')
print(a)
a=p.match('cats')
print(a)
