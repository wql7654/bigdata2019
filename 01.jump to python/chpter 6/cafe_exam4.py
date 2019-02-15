def error_data(input_num,number):
    try:
        input_num = int(input_num)
    except Exception :
        print("%s 번째 입력이 [%s]입니다. 숫자를 입력하세요" % (number+1,input_num))
    return input_num

def data_sum(input_data,total_sum):
    try:
        total_sum += input_data
    except Exception:
        pass
    else:
        return total_sum


while True:
    input_diffent_num = input('숫자를 입력하세요 ("종료" 입력시 프로그램 종료): ')
    if input_diffent_num == "종료":
        quit()
    list_num=input_diffent_num.split()
    total_sum=0

    for cnt in range(0,len(list_num)):
        list_num[cnt]=error_data(list_num[cnt],cnt)
        total_sum=data_sum(list_num[cnt],total_sum)
    print(total_sum)

