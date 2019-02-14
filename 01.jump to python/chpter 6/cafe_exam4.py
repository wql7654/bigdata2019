def error_data(input_num,number):
    try:
        input_num = int(input_num)
    except Exception :
        print("%s 번째 입력이 [%s]입니다. 숫자를 입력하세요" % (number+1,input_num))
    return input_num

while True:
    input_diffent_num = input('두 수를 입력하세요 ("종료" 입력시 프로그램 종료): ')
    if input_diffent_num == "종료":
        quit()
    list_num=input_diffent_num.split()
    for cnt in range(0,len(list_num)):
        list_num[cnt]=error_data(list_num[cnt],cnt)

