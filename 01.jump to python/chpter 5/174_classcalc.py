

class Cauculator: #사용자 정의 클래스
    def __init__(self): #클래스의 생성자(constructor) 객체 생성시 최초로 수행되는 함수
        self.result=0 #클래스의 멤버 변수 (전역변수global 클래스전역변수 self(클래스에적용)
    def adder(self,num): #멤버 함수(member function)
        print("%d값을 입력 받았습니다"%num)
        self.num1=100 #멤버 변수로 등록은 가능하나 가독성은 떨어진다.
        self.result += num
        return self.result

cal1=Cauculator()
cal2=Cauculator()
cal3=Cauculator()


print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))
print(cal3.adder(3))
print(cal3.adder(7))

