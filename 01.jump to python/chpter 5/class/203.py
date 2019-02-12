
class HousePark:
    __last_name__ = "박" #  private 하고싶을때
    full_name= ""  # 바뀔수있으므로
    def __init__(self, name):
        self.full_name=self.__last_name__+name
    def traval(self,where):
        print("%s, %s 여행을 가다"%(self.full_name,where))

pey=HousePark()
#생성자에 인자가 1개 있도록 되어 있는데 없는 생성자를 호출했으므로 에러가 발생
pey.set_name("응용")
pey.traval("부산")
