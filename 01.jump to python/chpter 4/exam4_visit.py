
def search_visitor(name):
    f = open("./방명록.txt", 'r', encoding="UTF-8")
    ser_name=f.readlines()
    f.close()


    for name_list in ser_name:
        if name in name_list[:-7]:
            return name


name_vister=input("이름을 입력하세요:")
search_user=search_visitor(name_vister)
if search_user:
    print("%s님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요."%search_user)
else:
    age_input=input("생년월일을 입력하세요 (예:801212):")
    f=open("./방명록.txt", 'a', encoding="UTF-8")
    f.write("%s %s\n"%(name_vister,age_input))
    f.close()
    print("%s님 환영합니다.아래 내용을 입력하셨습니다."%name_vister)
    print("%s %s\n" % (name_vister, age_input))

