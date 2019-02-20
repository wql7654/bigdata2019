import re

file_name=["foo.bar","autoexec.bat","sendmail.cf","sandstrom.p"]
#확장자가 bat인 파일은 제외해야 하는 조건 추가

p = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$")
for file in file_name:
    m = p.search(file)
    print(m)



#확장자길이가 1~3개까지 가능
#확장자의 글자의 갯수가 2이상이 되도록 "?"를 추가하여
# ver 2에서 추가한 확장자가 'bat'인 파일을 제거하기 위한 요구사항을 만족했다.