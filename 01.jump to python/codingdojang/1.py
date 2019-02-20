import os
number=''
cnt=1
while True:
    try:
        f=open("./사본%s.txt"%number ,'r',encoding='UTF-8')
        b=f.readlines()
        f.close()
        data = input("변경된 파일경로를 입력해 주세요: ")
        os.chdir("%s" % data)

    except Exception:
        number='_'+cnt
        cnt+=1
    else:
        f = open("./사본%s.txt" % number,'w', encoding='UTF-8')
        f.write(str(b))
        f.close()

