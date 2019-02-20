import re

p=re.compile("clzkl") # 0또는 1만 적용이된다.
a=p.match('clzkladksldk')
print(a)
a=p.match('cat')
print(a)
a=p.match('caat')
print(a)
a=p.match('cats')
print(a)
