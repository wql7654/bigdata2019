

class Restaurant:
    def __init__(self, name):
        self.number_served = 0
        self.sel_name=name.split()
        self.restaurant_name=self.sel_name[0]
        self.cuisine_type=self.sel_name[1]


    def open_restaurant(self):
        open_count = (str(input("레스토랑을 오픈하시겠습니까?(y/n)")))
        if open_count=='y':
            print("저희 '%s' 레스토랑이 오픈했습니다."%self.restaurant_name)
        elif open_count=='n':
            quit()
    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 '%s' 이고 %s 전문점입니다"%(self.restaurant_name,self.cuisine_type))
    def __del__(self):
        print("%s 레스토랑 문닫습니다"%self.restaurant_name)


class Restaurant_count:

    def __init__(self, num):
        self.todays_customer = 0
        self.number_served = int(num)
        self.f = open("./고객서빙현황로그.txt", 'w', encoding="UTF-8")
    def reset_number_served(self, number):
        print("손님 %s명 들어오셨습니다. 자리를 안내해 드리겠습니다."%number)

    def increment_number_served(self, number):
        self.todays_customer  += number

    def check_customer_number(self):
        print("지금까지 총 %s명 손님께서 오셨습니다." % self.todays_customer )

    def zero_number_served(self):
        self.todays_customer =0
        print("손님 카운팅을 0으로 초기화 하였습니다")
    def __del__(self):
        self.f.write(str(self.number_served+self.todays_customer))
        self.f.close()

class Restaurant_choice(Restaurant):
    def __init__(self,name):
        super().__init__(name)

    def describe_restaurant(self):
        if self.cuisine_type in "초밥" or self.cuisine_type in "덮밥" or self.cuisine_type in "소바":
            self.cuisine_type='일식'
        elif self.cuisine_type in "국밥" or self.cuisine_type in "김치" or self.cuisine_type in "비빔밥":
            self.cuisine_type='한식'
        super().describe_restaurant()



name_food=Restaurant_choice(str(input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ")))
name_food.describe_restaurant()
name_food.open_restaurant()


f = open("./고객서빙현황로그.txt", 'r', encoding="UTF-8")
backup_number=f.read()
f.close()
count_class=Restaurant_count(backup_number)
while True:
    number_sev = (input("어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) : "))
    if number_sev == 'p':
        count_class.check_customer_number()
    elif number_sev == '-1':
        quit()
    elif number_sev == '0':
        count_class.zero_number_served()
    else:
        count_class.reset_number_served(int(number_sev))
        count_class.increment_number_served(int(number_sev))


