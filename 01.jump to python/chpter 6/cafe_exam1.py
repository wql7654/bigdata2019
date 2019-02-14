

copy_data=[]
def read_data(read_data,option):
    for reserve_data in read_data:
        if reserve_data == '\n':
            pass
        elif option==1:
            reserve_data = reserve_data.replace("python", "C")
            print(reserve_data, end='')
            copy_data.append(reserve_data)
        else:
            print(reserve_data, end='')

f= open("learning_python.txt",'r',encoding="UTF-8")
input_data=f.readlines()
f.close()
read_data(input_data,0)
read_data(input_data,1)
f=open("learn_python_copyed.txt",'w',encoding='UTF-8')
f.writelines(copy_data)
f.close()
