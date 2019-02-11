
class HousePark:
    __last_name__ = "박" #  private 하고싶을때

    #def setname(self,name):
    #def SetName(self, name):
    def set_name(self, name):
        self.full_name=self.__last_name__+name

pey=HousePark()
pes=HousePark()
print(pey.__last_name__)
print(pes.__last_name__)
