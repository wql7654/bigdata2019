import re

file_name=["foo.bar","autoexec.bat","sendmail.cf"]

p = re.compile(".*[.].*$")
for file in file_name:
    m = p.search(file)
    print(m.group())



p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())