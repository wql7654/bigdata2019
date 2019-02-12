class serviec:
    secret = "영구는 배꼽이 두 개다"
    def sum(self,a,b):
        result= a+b
        print("%s+%s=%s 입니닷"%(a,b,result))

pay=serviec()

print(pay.secret)
# pay.sum(pay,1,1)
pay.sum(1, 1) #pay.sum을 통하여 pay가 호출한지 알기 때문에 pay는 생략가능
pay.sum("1","1") #선언을딱히안해서 정수던 변수던 상관없음
