class serviec:
    __secret__ = "영구는 배꼽이 두 개다" #클래스가 가지는 고유의 공통 속성(스트링)
    name = "" #가독성을 위한 좋은습관
    def __init__(self,name):
        # __ xx __ 예약이되어있는 변경이되어서 재정의 되어서 안되는 함수
        self.name=name
    def sum(self,a,b):
        result= a+b
        print("%s님 %s+%s=%s 입니닷"%(self.name,a,b,result))
    def get_secret(self):
        return self.secret

pay=serviec("홍길동")
print(pay.get_secret())

