def error_data(input_num,number):
    try:
        input_num = int(input_num)
    except Exception :
        print("%s 번째 입력이 [%s]입니다. 숫자를 입력하세요" % (number+1,input_num))

    return input_num

def calculation_num(number1,number2,fig):
    try:
        number1=int(number1)
        number2=int(number2)
        if fig == '+':
            return number1 + number2
        elif fig == '-':
            return number1 - number2
        elif fig == '*':
            return number1 * number2
        elif fig == '/':
            return number1 / number2
        else:
            print("두 수 사이에 식을 넣어주세요.")
    except ZeroDivisionError:
        print("죄송합니다. 두 번쨰 입력에서 0을 입력하셨습니다. 분모는 0이 되어서는 않됩니다.")
    except Exception:
        pass



while True:
    input_diffent_num = input('두 수를 입력하세요 ("종료" 입력시 프로그램 종료, 띄어쓰기로 구분하고 숫자사이에 식을넣어주세요): ')
    if input_diffent_num == "종료":
        quit()
    try:
       list_num=input_diffent_num.split()
       list_num[0] =error_data(list_num[0], 0)
       list_num[2] =error_data(list_num[2], 1)
       if calculation_num(list_num[0], list_num[2], list_num[1]):
           print(calculation_num(list_num[0],list_num[2],list_num[1]))
    except Exception:
        print("숫자가 부족합니다 숫자를 입력해주세요")

