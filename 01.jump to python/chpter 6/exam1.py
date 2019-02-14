str_num=input("문자를 입력해주세요:")
rl=list(str(str_num))
rm=set(rl)
for i in rl:
    if i in rm:
        b=i

