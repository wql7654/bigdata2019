import re
original_text='life is too hard'
p=re.compile("[a-z]+") # 0또는 1만 적용이된다.
a=p.search(original_text) #젤처음에 시작한 단어만 검색을 해준다.
print(a)
a=p.findall(original_text) #가지고 있는 전체를 검색해서 돌려준다.
print(a)

