
try:
    result = 4/0
    print(result)

except ZeroDivisionError as e:
    print("비정상 종료")

print("Program End")

