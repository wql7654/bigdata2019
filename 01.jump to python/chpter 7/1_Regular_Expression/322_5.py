import re

file_name=["foo.bar","autoexec.bat","sendmail.cf","exe.bat."]
#확장자가 bat인 파일은 제외해야 하는 조건 추가

p = re.compile(".*[.](?!bat$|exe$|$).*$")
for file in file_name:
    m = p.search(file)
    print(m)




