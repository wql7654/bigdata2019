print("실행초기화")

def simple_func1():
    print("simple func1 초기화") #디버깅하지 않고 빠져나올려면 shift+f8
    print("simple func1 로직 수행중")
    #______
    print("simple func1 실행완료")

print("함수 호출 준비 완료")
simple_func1()#함수 안으로 디버깅 하려면 f7로 한다
print("프로그램 종료")