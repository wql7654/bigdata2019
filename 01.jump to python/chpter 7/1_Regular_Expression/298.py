import re
# p=re.compile("[abc]")
# print(p)
# m=p.match("a")
# print(m) #매칭이 된다
# p=re.compile("[abc]")
# m=p.match("k")
# print(m)
# m=p.match("abcd")
# print(m)
# m=p.match("ab")
#
# print(m)

c=re.compile("d[dadbc]")
z=c.match("dad")
print(z)

c=re.compile("d[dadbc]a")
z=c.match("dad")
print(z)
c=re.compile("[ da c dbc]iu[c]")
z=c.match("ac")
#문자열이 패턴에 맞게보일수 있으나 순서와 맞지 않아서 매칭이안된다.

print(z)
# match 함수안에 첫글자를 [] 에서 검색해서 매칭한다
# []안은 1글자만 매칭되면 어떤위치에있어도 매칭된다
# []밖에는 완전매치가 되야지만 매칭이 된다. (100%)
#정규식을 기준으로 두번째까지는 매칭이 되나 세번째까지는 매칭이 되지 않는다.