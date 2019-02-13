

try:
    denominator = int(input("분모를 입력하세요:"))
    print("Progress 1")
    f=open("새파일.txt", 'r')
    print("Progress 2")
    result = 4/denominator
    print("Progress 3")
    f.close()
    print("Progress 4")

except Exception as e:
    print(e)

finally:
    print("Finally 블록 수행")


