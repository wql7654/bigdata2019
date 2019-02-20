import re

p = re.compile(r'(\b\w+)(\s+)\1')
s=p.search('Paris in the the spring').group()
print(s)
c=p.search('Paris in the the the spring paris it it was really great').group()
print(c)