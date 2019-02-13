try:

    f=open("새 파일.txt",'r')
except FileNotFoundError as e:
    print(str(e))

else:
    print("b")
    data=f.read()
    f.close()


print("s")
