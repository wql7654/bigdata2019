from xml.etree.ElementTree import parse, Element, dump, SubElement, ElementTree
import MySQLdb
import pandas as pd


def sumup_xml():
   tree = parse("students_info_2.xml")  # 생성한 xml 파일 파싱하기
   note = tree.getroot()
   count=0
   sex = []
   lan_cnt=0
   cnt_level=0
   cnt_python=0
   age_20=[]
   age_30=[]
   age_40=[]
   major_cnt=0
   boy=0
   girl=0
   for parent in note.getiterator("student"):
       sex.append(parent.get("sex"))
       if parent.get("sex").find('남') != -1:
           boy += 1
       elif parent.get("sex").find('여') != -1:
           girl += 1

       if int(parent.findtext("age"))<30:
           age_20.append(parent.get("name")+':'+parent.findtext("age"))
       elif int(parent.findtext("age"))<40:
           age_30.append(parent.get("name")+':'+parent.findtext("age"))
       elif int(parent.findtext("age"))<50:
           age_40.append(parent.get("name")+':'+parent.findtext("age"))

       if parent.findtext("major").find("컴퓨터")!=-1 or parent.findtext("major").find("통계")!=-1:
           major_cnt += 1
       for cont in parent.getiterator("practicable_computer_languages"):
          if cont:
               lan_cnt += 1
       for language_value in parent.getiterator("language"):
           if language_value:
               if language_value.get("name").find("python")!=-1:
                   cnt_python+=1
               if language_value.get("level").find("상")!=-1:
                   cnt_level+=1
       count+=1



   print("* 전체 학생수:%d"%count)
   print("* 성별\n - 남학생: %s명(%0.1f%%)\n - 여학생: %s명(%0.1f%%)"%(boy,boy/int(len(sex))*100,girl,girl/int(len(sex))*100))
   print('* 전공여부')
   print("- 전공자(컴퓨터 공학, 통계): %s명 (%0.1f%%)" % (major_cnt,(major_cnt/count)*100))
   print("- 프로그래밍 언어 경험자: %s명 (%0.1f%%)" % (lan_cnt,(lan_cnt/count)*100))
   print("- 프로그래밍 언어 상급자: %s명 (%0.1f%%)" % (cnt_level,(cnt_level/count)*100))
   print("- 파이썬 경험자: %s명 (%0.1f%%)"% (cnt_python,(cnt_python/count)*100))
   print('* 연령대')
   print('- 20대: %s명 (%0.1f%%) %s' %(len(age_20),(len(age_20)/count)*100,age_20))
   print('- 30대: %s명 (%0.1f%%) %s' %(len(age_30),(len(age_30)/count)*100,age_30))
   print('- 40대: %s명 (%0.1f%%) %s' %(len(age_40),(len(age_40)/count)*100,age_40))
   print("")

def search_xml():
    while True:
        print("<조회 서브 메뉴>")
        input_data=input("1.개별 학생 조회 \n2.전체 학생 조회 \n3.상위 메뉴 \n메뉴입력: ")
        if input_data=='3':
            break
        elif input_data=='2':
            whole_xml()
        elif input_data == '1':
            individual_xml()

def individual_xml():
    while True:
        print("<검색 조건>")
        print("1.ID \n2.이름 \n3.나이 \n4.전공 \n5.컴퓨터 언어 명 \n6.컴퓨터 언어 학습 기간 \n7.컴퓨터 언어 레벨 \n8.상위 메뉴 \n")
        input_data = input("메뉴 입력: ")
        if input_data=='1' or input_data == '2' or input_data == '3' or input_data == '4' or input_data == '5' or input_data == '6' or input_data == '7':
            whole_search_xml(input_data)
        elif input_data == '8':
            break


def whole_xml():
   tree = parse("students_info_2.xml")  # 생성한 xml 파일 파싱하기
   note = tree.getroot()
   for parent in note.getiterator("student"):
       print("* %s" % parent.get("name"), end='')
       print("(%s)" % parent.get("ID"))
       print("- 성별: %s"%parent.get("sex"))
       print("- 나이: %s"%parent.findtext("age"))
       print("- 전공: %s"%parent.findtext("major"))
       for language_value in parent.getiterator("language"):
           if language_value:
               for period_value in language_value.getiterator("period"):
                   print("> %s 학습기간:%s,level:%s"%(language_value.get("name"),period_value.get("value"),language_value.get("level")))

   print("")


def insert_xml():

    id=[]
    id_append=''
    value_count=0
    language_value=[]
    period_value=[]
    language_level=[]
    language_level_hi = []
    language_level_mid = []
    language_level_low = []

    while True:
        id = []
        language_value = []
        period_value = []
        language_level = []
        print("<신규 학생 정보 입력>")
        value_count=0
        name_value2=input("- 이름을 입력하세요 (종료는 'Enter' 입력): ")
        if name_value2=="":
            break
        else :
            name_value = name_value2
        sex_value=input("- 성별을 입력하시요: ")
        age_value=input("- 나이를 입력하세요: ")
        major_value=input("- 전공을 입력하세요: ")
        print("- 사용 가능한 컴퓨터 언어를 입력하세요 ")
        while True:
            language_value2=(str(input(" > 언어 이름(종료는 'Enter' 입력): ")))
            if language_value2=="":
                break
            else:
                language_value.append(language_value2)
            period_value.append(str(input(" > 학습 기간(년/개월 단위) : ")))
            language_levels=(str(input(" > 수준(상,중,하): ")))
            if language_levels=='상':
                language_level_hi.append(language_value[value_count])
            elif language_levels=='중':
                language_level_mid.append(language_value[value_count])
            elif language_levels=='하':
                language_level_low.append(language_value[value_count])

            value_count += 1



        try:
            mysql_set.execute("SELECT student_id FROM student")
            rows = mysql_set.fetchall()
            id_num=int(str(sorted(list(rows),reverse=True)[0])[4:7])
        except Exception:
            id_num=1

        if id_num<10:
            id_append='00'+str(id_num+1)
        elif id_num<100:
            id_append = '0'+str(id_num+1)
        elif id_num<1000:
            id_append=id_num+1
        ID="ITT"+id_append


        mysql_set.execute("""INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""%(ID,name_value,age_value,major_value,language_value,language_level_hi,language_level_mid,language_level_low))



def whole_search_xml(num_data): ## c검색 안되는거  추가해야함

   overlap_data=0
   search_data = input("검색어를 입력하세요: ")
   count_ex=0
   value_count=0
   search_input=['','','','','','','','','','','','','','','','','']
   search_input2 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
   ex_parent=[]

   tree = parse("students_info_2.xml")  # 생성한 xml 파일 파싱하기
   note = tree.getroot()

   for parent in note.getiterator("student"):


       for language_value in parent.getiterator("language"):
           if language_value:
               value_count2=0
               for period_value in language_value.getiterator("period"):
                value_count2 += 1
                if num_data == '5':
                    search_input2[value_count2] = language_value.get("name")

                elif num_data == '6':
                    search_input2[value_count2] = period_value.get("value")

                elif num_data == '7':
                    search_input2[value_count2] = language_value.get("level")

                if search_input2[value_count2].find(search_data)!=-1 and int(num_data)>=5:
                    ex_parent.append(parent)


       if num_data == '1':
           search_input[value_count] = parent.get("ID")
       elif num_data == '2':
           search_input[value_count] = parent.get("name")
           if search_input[value_count].find(search_data)!=-1:
                overlap_data+=1

       elif num_data == '3':
           search_input[value_count] = parent.findtext("age")
       elif num_data == '4':
           search_input[value_count] = parent.findtext("major")
       value_count += 1




   value_count=0
   for parent in note.getiterator("student"):

       try:
           ex_parent.index(parent)
           count_ex=1
       except Exception:
           count_ex=0
       if (search_input[value_count].find(search_data)!=-1 or count_ex==1) and overlap_data<=1 :
            overlap_data=0
            print("* %s"%parent.get("name"),end='')
            print("(%s)" % parent.get("ID"))
            print("- 성별: %s"%parent.get("sex"))
            print("- 나이: %s"%parent.findtext("age"))
            print("- 전공: %s"%parent.findtext("major"))

            for language_value in parent.getiterator("language"):
                if language_value:
                    for period_value in language_value.getiterator("period"):
                        print("> %s 학습기간:%s,level:%s"%(language_value.get("name"),period_value.get("value"),language_value.get("level")))

       if search_input[value_count].find(search_data)!=-1 and overlap_data >1:
            print("%s (%s, %s, %s)"%(parent.get("ID"),parent.get("name"),parent.findtext("age"),parent.get("sex")))
            # overlap_data=0
       value_count += 1

   print("")



def del_xml():
    del_id=input("삭제할 ID를 입력하세요: ")
    tree = parse("students_info_2.xml")  # 생성한 xml 파일 파싱하기
    note = tree.getroot()
    # dump(note)
    for parent in note.getiterator("student"):
        if parent.get("ID") == del_id:
            note.remove(parent)
            ElementTree(note).write("students_info_2.xml", encoding='UTF-8', xml_declaration=True)


def update_xml():
    update_id=input("수정할 ID를 입력하세요: ")
    tree = parse("students_info_2.xml")  # 생성한 xml 파일 파싱하기
    note = tree.getroot()
    num=1
    value_count=0
    count=1



    for parent in note.getiterator("student"):
        if update_id == parent.get("ID"):
            print("%d.이름: %s"%(num,parent.get("name")))
            name_value=parent.get("name")
            num += 1
            print("%d.성별: %s"%(num,parent.get("sex")))
            sex_value=parent.get("sex")
            num += 1
            print("%d.나이: %s"%(num,parent.findtext("age")))
            age_value=parent.findtext("age")
            num += 1
            print("%d.전공: %s"%(num,parent.findtext("major")))
            major_value=parent.findtext("major")
            num += 1
            print("사용 가능한 컴퓨터 언어")
            for language_value in parent.getiterator("language"):
                if language_value:
                    for period_value in language_value.getiterator("period"):
                        value_count+=1
                        print("%d.언어: %s"%(num,language_value.get("name")))
                        lang_value=language_value.get("name")
                        num += 1
                        print("%d.학습기간: %s"%(num,period_value.get("value")))
                        per_value=period_value.get("value")
                        num += 1
                        print("%d.레벨: %s"%(num,language_value.get("level")))
                        level_value=language_value.get("level")
                        num += 1


    update_info=input("수정할 항목의 번호를 입력하세요: ")
    update_data=input("수정할 값을 입력하세요: ")

    for parent in note.getiterator("student"):
        if (parent.get("ID") == update_id):
            # dump(parent)

            if update_info =='1':
                parent.set('name', update_data)
            elif update_info == '2':
                parent.set('sex', update_data)
            elif update_info == '3':
                parent.find('age').text = update_data
            elif update_info == '4':
                parent.find('major').text = update_data
            for language_value in parent.getiterator("language"):
                count+=3
                if (int(update_info)<=count+3 and int(update_info)>count):
                    for i in range(4,num):
                        if int(update_info)%3==2:
                            language_value.set('name', update_data)
                        if int(update_info)%3==0:
                            sh =language_value.find('period')
                            sh.set('value', update_data)
                        if int(update_info)%3==1:
                            language_value.set('level', update_data)

            print("* %s" % parent.get("name"), end='')
            print("(%s)" % parent.get("ID"))
            print("- 성별: %s" % parent.get("sex"))
            print("- 나이: %s" % parent.findtext("age"))
            print("- 전공: %s" % parent.findtext("major"))
            for language_value in parent.getiterator("language"):
                if language_value:
                    for period_value in language_value.getiterator("period"):
                        print("> %s 학습기간:%s,level:%s" % (
                        language_value.get("name"), period_value.get("value"), language_value.get("level")))

    ElementTree(note).write("students_info_2.xml", encoding='UTF-8', xml_declaration=True)


def indent(elem, level=0):
    i="\n"+ level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
           elem.tail=i


con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='bigdata', passwd='1111')
mysql_set = con.cursor()


while True:
    print("학생정보 XML데이터 분석 시작..")
    input_data=input("1.요약정보 \n2.입력 \n3.조회 \n4.수정 \n5.삭제 \n6.종료 \n메뉴 입력: ")
    if input_data=='6':
        print("학생 정보 분석 완료!")
        quit()
    elif input_data=='1':
        sumup_xml()
    elif input_data == '2':  # 입력
        insert_xml()
    elif input_data == '3':  # 조회
        search_xml()
    elif input_data == '4':  # 수정
        update_xml()
    elif input_data == '5':  # 삭제
        del_xml()