input_denominatior = int(input("분모를 입력하세요"))
try:
    result = 4/input_denominatior
    print(result)
    f=open("내가없다파일.txt",'r')
    f.close()


except ZeroDivisionError as a:
    print(a)
    print("분모가 0이 되어서는 안됩니다. 다시입력하세요")
except FileNotFoundError as e:
    print(e)
    print("해당 파일이 존재하지 않습니다. 230_6가 있는 경로에 파일이 있는지 확인해주세요")

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

