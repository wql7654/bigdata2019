import re

p = re.compile('\section') #\s 가 공백문자를 표현하는 정규식이기 때문에
print(p.search('section'))
p = re.compile('\\section') # \\s 도 현재버젼에서는 정규식으로 처리
print(p.search('\section')) #raw string 문법으로 보면 r'\\'은 '\\\\'의미 이지만 아래 '\'가 한개인 string에도 매치가된다.
p = re.compile(r'\\section')
print(p.search('\section'))
p = re.compile('\\\section')
print(p.search('\section'))
p = re.compile('\\\\section')
print(p.search('\\section'))
p = re.compile(r'\\section')
print(p.search('\\section'))

