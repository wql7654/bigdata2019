def sum(a,b):
    return a+b


def safe_sum(a, b):
    if type(a) != type(b):
        print("두 인자의 형이 다릅니다.")
        return
    else:
        result = sum(a, b)
    return result
if __name__ == "__main__":
    # 모듈로 사용할때 이 파일안에서만 구동되게하는 문법
    # __name__ 에들어가는건 프로그램이 수행한 모듈이름이 들어간다
    # 프로그램이 수행한 모듈에는 name 에__main__ 이 들어간다
    print(sum(1,2))
    print(safe_sum(1,2))
    print(safe_sum(1,"2"))