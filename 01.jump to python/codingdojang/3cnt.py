count=0
for i in range(0,1440):
    time_i=int(i/60)*100 + int((i%60))
    isnum=list(str(time_i))
    a=0
    for three in isnum:
        if three == '3' and a==0:
            count += 1
            a=1

print(count*60)
