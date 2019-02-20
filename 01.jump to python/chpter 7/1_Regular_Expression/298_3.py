import re
original_text="""s,.1 
bc dasdsad
dd asdsadsa
3d asdsadsa
2dsadsadasda
zxczxcwq
vbdfasd
udsadsd
cczx asdqwd
"""
p=re.compile("[1-zA-Z],.[0-1]")
m=p.match(original_text)
print(m)
