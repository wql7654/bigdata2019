a=1 # 전역변수(global variable)
def global_var_read():
    print(a)


def global_var_write():
   a+=2 # 변수의 값을 쓰려는 순간 파이썬에서는 변수를 지역변수로 인식한다.
        # 따라서 a+=2 는 문법적으로 오류를 발생한다.
def global_var_write2():
   global a # 전역변수 a를 함수 안에서 값을 쓰고자 할때 문법상 선언해 준다.
   a+=2

global_var_read()
print(a)
# global_var_write() # 호출하면 에러를 발생한다.
global_var_write2()
print(a)
#c는 컴파일형 에러 파이선은 인터프리터 언어라서 호출하는것만 에러를 잡음
