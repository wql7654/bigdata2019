f=open("./file3.txt",'r',encoding='UTF-8')

while True:
    line = f.readline()
    if not line:
        break
    print(line,end='')

    #원본에 \n이 존재하고있고 print 함수에도 문장하나끝날때
    #줄바꿈이있기때문에 원본그대로 나오지가않아서 end추가

f.close()