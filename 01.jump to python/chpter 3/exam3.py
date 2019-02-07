# coding: cp949

print("나이를 입력하세요:")
year_str=input()
year=int(year_str)
tap=0
if year>=0 and year<=3:
    money='무료'
    vip=1
elif year>=4 and year<=13:
    money=2000
    vip=2
elif year>=14 and year<=18:
    money=3000
    vip=3
elif year>=19 and year<=65:
    money=5000
    vip=4
elif year>=66:
    money='무료'
    vip=5
else:
    tap=1
    print("다시입력하세요")

if tap!=1 and money=='무료':
    print("귀하의 %s 등급이며 요금은 %s 입니다." %(vip,money))
elif tap!=1 and money!='무료':
    print("귀하의 %s 등급이며 요금은 %s원 입니다." %(vip,money))
if money=='무료':
    print("감사합니다 즐거운시간 보내세요")
else:
    print("요금을 입력하세요")
    money_str=input()
    money_input=int(money_str)
    if money_input==money:
      print("감사합니다. 티켓을 발행합니다.")
    elif money_input>=money:
      print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다."%(money_input-money))

    
    

