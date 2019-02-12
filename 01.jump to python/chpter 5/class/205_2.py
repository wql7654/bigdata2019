
class HousePark: # 부모 클래스(super class)
    __last_name__ = "박" #  private 하고싶을때
    full_name= ""  # 바뀔수있으므로
    def __init__(self, name):
        self.full_name=self.__last_name__+name
    def traval(self,where):
        print("%s, %s 여행을 가다"%(self.full_name,where))


class HouseKim(HousePark): #자식클래스 (Child Class)
    __last_name__ = "김"
    pass

kitty=HouseKim("만복")
print(kitty.__last_name__)
kitty.traval("제주")
