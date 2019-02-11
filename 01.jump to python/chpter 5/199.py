
class HousePark:
    __last_name__ = "박" #  private 하고싶을때
    full_name= ""  # 바뀔수있으므로
    def set_name(self, name):
        self.full_name=self.__last_name__+name
    def traval(self,where):
        print("%s, %s 여행을 가다"%(self.full_name,where))

pey=HousePark()
pey.set_name("응용")
pey.traval("부산")
