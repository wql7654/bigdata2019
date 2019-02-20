import re

p=re.compile("ca{2}t") #{} 숫자가 한개만 올때는 해당 반복수를 정확히 지킨 문자열만 매칭이 된다
a=p.match('ct')
print(a)
a=p.match('cat')
print(a)
a=p.match('caat')
print(a)
a=p.match('caaat')
print(a)


p=re.compile("do{2,5}g") #{} 2~5까지의 문자열만 지원
a=p.match('dooog')
print(a)
a=p.match('doooooooog')
print(a)
a=p.match('doog')
print(a)
a=p.match('dooooog')
print(a)


p=re.compile("pi{2,}g") #{} 반복이 2이상일때만 적용
a=p.match('pig')
print(a)
a=p.match('piiiiiiiig')
print(a)
a=p.match('piig')
print(a)
a=p.match('piiiiiig')
print(a)

p=re.compile("he{,5}g") #{} 반복이 2이상일때만 적용
a=p.match('heg')
print(a)
a=p.match('heeeeeeeg')
print(a)
a=p.match('heeg')
print(a)
a=p.match('heeeeeg')
print(a)




