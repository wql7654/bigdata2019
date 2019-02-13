input_data=tuple(str(input("소스코드를 입력하세요")))
join_code=[]
for cnt in input_data:
    if cnt =="\t":
        join_code.append('    ')
    else:
        join_code.append(cnt)

print("".join(join_code))