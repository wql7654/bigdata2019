import re
original_text='life is too hard'
p=re.compile("[a-z]+") # 0또는 1만 적용이된다.

result=p.finditer(original_text) # 검색 결과는 매칭된 문자열을 리스트로 반환한다.
#매칭된 결과를 match object 리스트로 반환한다
print(result)
for r in result:
    print(r)