
class HousePark:
    __last_name__ = "박" #  private 하고싶을때
    full_name= ""  # 바뀔수있으므로
    def __init__(self, name):
        self.full_name=self.__last_name__+name
    def traval(self,where):
        print("%s, %s 여행을 가다"%(self.full_name,where))

pey=HousePark("응용")
pey.traval("부산")
