

ingredient_list=[]
order=0
sandwich_input = []
def input_ingredient() :

    while True:
        sandwich_input=input("안녕하세요. 원하시는 재료를 입력하세요:")
        if sandwich_input=='종료':
            return ingredient_list

        else:
            str(ingredient_list.append(sandwich_input))


def make_sandwiches(make):
    print("샌드위치를 만들겠습니다")
    for make_sand in make:
        print("%s 추가합니다."%make_sand)
    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")


while True:
    order=int(input("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.\n 1.주문 \n 2.종료\n 입력:"))
    if order==2:
        break
    elif order==1:
        make=input_ingredient()
        make_sandwiches(make)
        break
    else:
        continue




