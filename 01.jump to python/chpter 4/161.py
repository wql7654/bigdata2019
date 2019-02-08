
f=open("./file3.txt",'w',encoding='UTF-8')
# f.write("hello world!") #글자 수정후 재실행시 overwrite 된다.
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)

f.close()