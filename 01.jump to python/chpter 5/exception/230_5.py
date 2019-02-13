
try:
    result = 4/2
    print(result)
    f=open("내가없다파일.txt",'r')
    f.close()


except Exception as a :
    # 모든 Failure을 동일하게 처리하고 싶을때 Exception의 유형을 정확히 모를때 유용하다.
    # 일반적인 상황에서 적용할수있는 상황.
    print(a)

print("Program End")



# exam:
#
# result = system_cal()
# if result == -1
#     print("xxx 에러를 발생했습니다.")
#     exit()
# else
#     print(result)

# result = system_utill()
#
# if result == -1
#     print("xxx 에러를 발생했습니다.")
#     exit()
# else
#     print(result)
#
# print("Program End")

