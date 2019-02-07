# 입력(parameter)이 있고, 출력(return) 이 없는 함수

def sum_type():
    # 함수 정의(define)
    num1=num1+10000 # 여기서 num1 과 10번 라인의 num1 은 다르다
    num2=num2+10000 # 여기서 num2 과 10번 라인의 num2 은 다르다
    print("num1+num2="+str(int(num1)+int(num2)))

num1, num2= input("두 수를 입력하세요").split()
num1=int(num1)
num2=int(num2)
sum_type()


