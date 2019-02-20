import re

p = re.compile('[\d]')
print(p.search('7'))
p = re.compile("[\w]")
print(p.search(' Z '))
p = re.compile('\d')
print(p.search('7'))
p = re.compile("\w")
print(p.search(' Z '))
p = re.compile('[\s]')
print(p.search(' '))
p = re.compile("\s")
print(p.search('  '))