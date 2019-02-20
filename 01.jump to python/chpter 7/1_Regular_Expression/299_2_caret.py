import re
p=re.compile("[\d]") #[ 0-9]
m=p.match('1')
print(m)

p=re.compile("[\D]") #[^0-9]
m=p.match('1')
print(m)


p=re.compile("[\s]") #[\t\n\r\f\v 공백문자]
m=p.match('     ')
print(m)

m=p.match("""
""")
print(m)


p=re.compile("[\W]") #[\t\n\r\f\v 공백문자]
m=p.match('        ')
print(m)

m=p.match("""
""")
print(m)
