
class why_program():
    save_poll = []
    def __init__(self):
        self.f = open("./poll.txt", 'a', encoding="UTF-8")
    def save_data(self,input_name,input_why):
        self.data = '[' + input_name + '] ' + input_why +'\n'
        self.save_poll.append(self.data)
        self.wirte_data = "".join(self.save_poll)

    def __del__(self):
        self.f.write(str(self.wirte_data))
        self.f.close()

add_class=why_program()
while True:
    input_why = input("프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료): ")
    if input_why == "종료":
        quit()
    input_name = input("이름을 입력해주세요: ")
    print("[%s] %s" % (input_name, input_why))
    print("설문에 응해주셔서 감사합니다.")
    add_class.save_data(input_name,input_why)





