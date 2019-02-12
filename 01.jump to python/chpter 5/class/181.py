class serviec:
    secret = "영구는 배꼽이 두 개다"
    name = "" #가독성을 위한 좋은습관
    def setname(self,name):
        self.name=name
    def sum(self,a,b):
        result= a+b
        print("%s님 %s+%s=%s 입니닷"%(self.name,a,b,result))

pay=serviec()
pay.setname("홍길동")
# print(pay.secret)
# pay.sum(pay,1,1)
pay.sum(1, 1) #pay.sum을 통하여 pay가 호출한지 알기 때문에 pay는 생략가능
# pay.sum("1","1")