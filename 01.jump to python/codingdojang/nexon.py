count=0
b=[]
for num2 in range(1,110):
    count=0
    num=list(str(num2))
    for eight in num:
      count+=int(eight)
    count=count+num2
    b.append(count)





