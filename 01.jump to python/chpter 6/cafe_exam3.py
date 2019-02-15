import os
class why_program():
    save_poll = []
    def __init__(self):
        self.f = open("./poll.txt", 'a', encoding="UTF-8")
    def save_data(self,input_name,input_why):
        self.data = '[' + input_name + '] ' + input_why +'\n'
        self.save_poll.append(self.data)
        self.wirte_data = "".join(self.save_poll)
        return self.wirte_data

    def __del__(self):
        try:
            self.f.write(str(self.wirte_data))
            self.f.close()
        except Exception:
            pass

def read_content_ext():
    print("기존 poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요.")
    data = input("1. 종료 2.새로운 파일 생성 3. 변경된 파일 경로 입력: ")
    if data == '1':
        quit()
    elif data == '2':
        read_data()
        read_content()
    elif data == '3':
        c = ''
        data = input("변경된 파일경로를 입력해 주세요: ")
        try:
            os.chdir("%s" % data)
        except Exception:
            print("지정한경로를 찾을수없습니다")
        else:
            read_data()
            read_content()


def read_data():
    try:
         f = open("./poll.txt", 'r', encoding="UTF-8")
         print("<현재 누적 응답 현황>")
         lines=f.readlines()
         for line in lines:
             print(line,end='')
         f.close()
    except Exception:
         print("poll.txt 파일을 생성합니다")

def read_content():
    add_class = why_program()
    while True:
        input_why = input("프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료): ")
        if input_why == "종료":
            quit()
        input_name = input("이름을 입력해주세요: ")
        print("[%s] %s" % (input_name, input_why))
        print("설문에 응해주셔서 감사합니다.\n", end='\n')
        input_data=add_class.save_data(input_name, input_why)
        read_data()
        print(input_data)


try:
    f = open("./poll.txt", 'r', encoding="UTF-8")
    f.close()
except FileNotFoundError :
    while True:
        read_content_ext()
else:
    read_data()
    read_content()









