import re
original_text="""a
b
"""
p=re.compile("a.b") #정규식 '.' 는 원문에 \n 에 대해서 기본옵션으로 사용하면 패턴 매칭이 되지 않는다.
                    #참고 정규식에 \n 을 사용 한경우는 기본옵션을 사용해도 패턴 매칭을 할 수 있다
m=p.match(original_text)
print(m)

p=re.compile("a.b",re.DOTALL)
m=p.match(original_text)
print(m)


p = re.compile('a.b')
m = p.match('a\nb')
print(m)
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)