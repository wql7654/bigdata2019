# coding: cp949

ticket_count=0
free_ticket=3
sale_ticket=5
while True:
   age_str=input("나이를 입력하세요:")
   age=int(age_str)
   
   if age>=0 and age<=3:
       money='무료'
       vip='유아'
   elif age>3 and age<=13:
       money=2000
       vip='어린이'
   elif age>13 and age<=18:
       money=3000
       vip='청소년'
   elif age>20 and age<=65:
       money=5000
       vip='성인'
   elif age>65:
       money='무료'
       vip='노인'
   else:
       print("다시입력하세요")
       continue

   if money=='무료':
       print("귀하의 %s 등급이며 요금은 %s 입니다." %(vip,money))
       print("감사합니다 즐거운 시간 보내세요")
       #exit()
   elif money!='무료':
       print("귀하의 %s 등급이며 요금은 %s원 입니다." %(vip,money))
       money_type_str=input("요금 유형을 선택하세요.(1:현금, 2:공원 전용 신용 카드):")
       money_type=int(money_type_str)
       if(money_type==1):
           print("요금을 입력하세요")
           money_str=input()
           money_input=int(money_str)
           if money_input==money:
               print("감사합니다. 티켓을 발행합니다.")
               ticket_count+=1
           elif money_input>=money:
               print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다."%(money_input-money))
               ticket_count+=1
           elif money_input<money:
               print("금액이 부족합니다 투입한금액 %s원을 반환합니다."%(money_input))
               continue
				
       elif(money_type==2):
           if(age<=65 and age>=60):
               money_card=(((money*90)/100)*95)/100
           else:
               money_card=(money*90)/100
           print("%d원 결재 되었습니다. 티켓을 발행합니다."%money_card)
           ticket_count+=1

       if(ticket_count%8==0 and free_ticket>0):
           free_ticket-=1
           ticket_count+=1
           print("축하합니다. 1주년 이벤트에 당첨되었습니다 여기 무료티켓을 발행합니다. 잔여 무료티켓 %d장"%free_ticket)
       elif(ticket_count%5==0  and sale_ticket>0):
           sale_ticket-=1
           ticket_count+=1
           print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장"%sale_ticket)
       
   # modify1
