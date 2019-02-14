class mutiple:
    def __init__(self, num):
        self.view_cnt=[]
        if num == '0':
            quit()
        else:
            self.multiple_num = num.split()
    def common_multiple(self):
        for input_cnt in range(1, int(self.multiple_num[2])):
            if input_cnt % int(self.multiple_num[0]) and input_cnt % int(self.multiple_num[1]) == 0:
                self.view_cnt.append(input_cnt)
        return self.view_cnt

while True:
    multiple_option=mutiple(input("공배수 x와 y 그리고 범위 z를 지정해주세요 (띄어쓰기으로 구분,종료 0): "))
    print(multiple_option.common_multiple())
