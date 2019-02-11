
# coding: cp949
count_null=0
view_star=0
count_star=0
count_star_info=int(input("홀수를 입력하세요(0 <- 종료): "))

if count_star_info == 0 or count_star_info%2==0:
    exit()
count_star=int((count_star_info+1)/2)
while count_star>0:
    count_null=(count_star-1)
    view_star=int(count_star_info-(count_null*2))
   # print(count_star,count_null,view_star)
    while count_null>0:
        print(' ',end='')
        count_null-=1;
    while view_star>0:
        print('*',end='')
        view_star-=1;

    print(' ')
    count_star-=1
    
    
