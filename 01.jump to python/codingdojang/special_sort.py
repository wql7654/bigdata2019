str_num=input("섞인 숫자 배열을 입력하세요(띄어쓰기로 구분)").split()
view_num=[]
view_num2=[]
for cell_num in str_num:
    cell_num=int(cell_num)
    if cell_num < 0:
        view_num.append(cell_num)
    else:
        view_num2.append(cell_num)
print(view_num+view_num2)