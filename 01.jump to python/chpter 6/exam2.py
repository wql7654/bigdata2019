

def char_num(input_data):
    for num in input_data.split():
        if len(num) == 10:
            num = set(num)
            if len(num) == 10:
                print("True")
            else:
                print("False")
        else:
            print("False")

while True:
    char_num(str(input("0~9 까지를 포함하는 숫자를 적어주세요: ")))

