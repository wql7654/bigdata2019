count=0
cur=0
cur2=0
nums=0
hig=0
lowe=0
mid=0
# rar=int(input("dd"))
for num2 in num_cnt:
    # print(num2)
    num=list(str(num2))
    a = 0
    cur = 0
    cur2 = 0
    for eight in num:
        eight=int(eight)

        if nums>=eight and a==1:
            cur+=1
        if nums<=eight and a==1:
            cur2+=1
        if cur2==len(str(num2))-1:
            # print("hight")
            hig+=1
        elif cur==len(str(num2))-1:
            # print("low")
            lowe+=1
        else:
            # print("oralgaral")
            mid+=1
        # print("%s,%s,%s,%s,%s"%(cur,cur2,len(str(num2))-1,eight,num))
        nums=eight
        a=1

print("%s,%s,%s,%s"%(hig,lowe,mid,hig+lowe))
