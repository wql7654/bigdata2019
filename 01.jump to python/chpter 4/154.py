a=99 # 전역변수(global variable)
# 전역변수는 힙(heap)에 저장되며 프로그램이 끝날때 까지 유효하다.
# 어디에서도 접근 가능하다.
def vartest(a):
    a=a+1 # 지역변수(local variable)
    # 지역변수는 (stack)에 저장되며 함수호출이 끝나면 사라진다.
    # 해당 함수에서만 접근 가능하다.

vartest(a)
print(a)
