import re
original_text="""dlszxcsldkslk
lgkelkdlakld
bczxcccccccx
"""
p=re.compile("[a-z]*.[a-z]*")
m=p.match(original_text)
print(m)
p=re.compile("[a-z]*.[a-z]*",re.DOTALL) #원문의 줄바꿈 \n 을 매칭시킬 '.'이 re.DOTALL 옵션사용시 필요하다.
m=p.match(original_text)
print(m)
