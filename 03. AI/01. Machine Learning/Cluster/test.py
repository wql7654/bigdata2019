with open('lotto.txt','r') as f:
    read=f.readlines()
b=[]
for i in read:
    i=i.replace('\t',',')
    b.append(i)
b=''.join(b)
with open('lotto.csv', 'w', encoding='utf-8') as f:
    f.write(b)