count=0
for num in range(0,10000):
    num=list(str(num))
    for eight in num:
      if (eight=='8'):
          count+=1

print(count)


