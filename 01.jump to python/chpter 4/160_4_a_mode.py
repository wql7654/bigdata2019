f=open("./file2.txt",'a')

f.write("hello world!\n")
f.write("hello daegu! !!!!!!!!!\n")
#이전 파일의 마지막 위치에서 값을 쓴다
#따라서 줄단위로 입력을 하고 싶으면 메세지의 마지막에 \n을 명시적으로 붙인다.
my_message="""hell seoul!!
hell daegu
helllll nonsan
"""

f.write(my_message)


f.close()