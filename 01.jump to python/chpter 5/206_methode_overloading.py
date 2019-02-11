
class HousePark: # 부모 클래스(super class)
    __last_name__ = "박" #  private 하고싶을때
    full_name= ""  # 바뀔수있으므로
    def __init__(self, name):
        self.full_name=self.__last_name__+name
    def traval(self,where):
        print("%s, %s 여행을 가다"%(self.full_name, where))
    def love(self,other):
        print("%s, %s 사랑에 빠졌네"%(self.full_name, other.full_name))
    def __add__(self, other):
        print("%s, %s 결혼했네"%(self.full_name, other.full_name))


class HouseKim(HousePark): #자식클래스 (Child Class)
    __last_name__ = "김"
    def traval(self,where,day):
        print("%s, %s 여행을 %d일 가다"%(self.full_name,where,day))


pey=HousePark("응용")
juliet=HouseKim("줄리엣")
pey.traval("대구")
juliet.traval("대구",6)
pey.love(juliet)
pey+juliet
