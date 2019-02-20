import re

# str='\'   \다음에 escape 코드가 와야 하지만 없으므로 문법적으로 오류를 발생시킨다
str='\\' #str은 내부적으로  '\\' 저장이 된다 하지만 문자로써는 '\'의 의미이다
print(str) #출력결과는 \
str='\\\\'
print(str) #출력결과는 \\
str=r'\\'
print(str) #출력결과는 \\
#str = r'\' 현재 버전에서 r  raw string 옵션을 사용하고 '\'를 한개 사용하는것을 허용하지않는다.

str='\section'
if str =='\\section':
    print(str)



p = re.compile('\section') #\s 가 공백문자를 표현하는 정규식이기 때문에
print(p.search('\ssection'))

