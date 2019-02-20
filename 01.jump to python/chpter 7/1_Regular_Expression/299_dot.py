import re

p=re.compile(".") #모든문자가 리딩이된다
                  # []문자열 클래스가 아닌 일반 문법으로 사용됬을경우
                  # '.'은 모든 문자를 의미하는 메타 문자로 사용된다.
m=p.match("""
""")
print(m)
m=p.match(" ")
print(m)
m=p.match("ㅊ")
print(m)
p=re.compile("...") #모든문자가 리딩이된다 정규식 기준으로
m=p.match("김철중")
print(m)
p=re.compile("...")
m=p.match("니 안! 에 멋지고 ")
print(m)


p=re.compile("as.")
m=p.match("as!")
print(m)

p=re.compile("as[.]") #.을 사용하고 싶다면 이걸 이용한다.
m=p.match("as!")
print(m)


