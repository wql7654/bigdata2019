# coding: cp949

print("나이를 입력하세요")
year_str=input()
year=int(year_str)

if year>=0 and year<=3:
    print("요금은 무료 입니다")
elif year>=4 and year<=13:
    print("요금은 2000원 입니다")
elif year>=14 and year<=18:
    print("요금은 3000원 입니다")
elif year>=19 and year<=65:
    print("요금은 5000원 입니다")
elif year>=66:
    print("요금은 무료 입니다")



