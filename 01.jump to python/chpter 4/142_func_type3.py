# 입력(parameter)이 없고, 출력(return) 이 있는 함수

def sum_type(num1,num2):
    # 함수 정의(define)

    num1, num2 = input("두 수를 입력하세요").split()
    num1=int(num1)
    num2=int(num2)

    return num1+num2

result= sum_type()

print("num1+num2=" + str(result))

