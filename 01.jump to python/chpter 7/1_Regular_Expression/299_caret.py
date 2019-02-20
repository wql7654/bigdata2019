import re
# p=re.compile("[^1]")
# ^의 의미는 not
# m=p.match('0')
# print(m)
#
# p=re.compile("[^0]")
# m=p.match('0')
# print(m)

p=re.compile("[^1-9]")
m=p.match('1')
print(m)


p=re.compile("1^")
m=p.match("1^")
print(m)

p=re.compile('[^a-zA-Z0-6]')
m=p.match("7")
print(m)
#문자열클래스 안에서 ^는 전체다적용된다

## 대다수의 표현식 ^나& 등등은 문자열 클래스 안에서만 적용된다

