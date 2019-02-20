import re

file_name=["foo.bar","autoexec.bat","sendmail.cf"]
#확장자가 bat인 파일은 제외해야 하는 조건 추가

p = re.compile(".*[.][^b].*$")
for file in file_name:
    m = p.search(file)
    print(m)

#수행결과 foo.bar 도 필터링하기에 실패한조건

