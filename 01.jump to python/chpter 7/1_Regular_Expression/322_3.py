import re

file_name=["foo.bar","autoexec.bat","sendmail.cf"]
#확장자가 bat인 파일은 제외해야 하는 조건 추가

p = re.compile(".*[.]([^b]..|.[^a].|..[^t])$")
for file in file_name:
    m = p.search(file)
    print(m)



# 확장자가  bar인 문자열을 필터링 안 하기 위한 '|' 조건이 확장자의 길이가 3임을 전제로 하기 때문에
# '.cf'와 같이 확장자의 길이가 2인 파일은 필터링 되어 실패한 조건이다.