import re
p=re.compile("[a-c]")
m=p.match("a")
print(m)
p=re.compile("[a-z]")
m=p.match("hc")
print(m)
p=re.compile("[1-z]")
m=p.match("d")
print(m)
p=re.compile("[a-c]")
m=p.match("dc")
print(m)
p=re.compile("[4-9]")
m=p.match("7")
print(m)