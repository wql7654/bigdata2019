class serviec:
    secret = "영구는 배꼽이 두 개다" #클래스가 가지는 고유의 공통 속성(스트링)
    name = "" #가독성을 위한 좋은습관
    def __init__(self,name):
        # __ xx __ 예약이되어있는 변경이되어서 재정의 되어서 안되는 함수
        self.name=name
    def sum(self,a,b):
        result= a+b
        print("%s님 %s+%s=%s 입니닷"%(self.name,a,b,result))

pay=serviec("홍길동") #객체만이 가지는 고유의 초기값을 설정하고 싶을 때 생성자를 통하여 설정한다.
pay.sum(1, 1)
