# 입력(parameter), 출력(return) 이 없는 함수

def sum_type():
    # 함수 정의(define)
    num1, num2=input("두수를 입력하세요:").split()

    print("num1+num2="+str(int(num1)+int(num2)))

sum_type()

