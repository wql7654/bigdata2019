class Restaurant:

    def __init__(self, name):
        self.sel_name=name.split()
        self.restaurant_name=self.sel_name[0]
        self.cuisine_type=self.sel_name[1]
    def open_restaurant(self):
        print("저희 '%s' 레스토랑이 오픈했습니다."%self.restaurant_name)
    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 '%s' 이고 %s 전문점입니다"%(self.restaurant_name,self.cuisine_type))
    def close_time(self):
        print("저녘 10시가 되었습니다.")
    def __del__(self):
        print("%s 레스토랑 문닫습니다"%self.restaurant_name)

n=0
name_food=[]
for n in range(0, 3):
    name_food.append(Restaurant(str(input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분)"))))
    name_food[n].describe_restaurant()
    name_food[n].open_restaurant()

name_food[0].close_time()



