import json

def json_read():
    try:
        with open("ITT_Student.json", encoding='UTF8') as json_file:
            json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_data = json.loads(json_string)
        return json_data
    except Exception:
        json_write('')

def json_write(json_data):
    with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)

def insert_update(json_data,line_cnt):
    class_code_value = []
    class_name_value = []
    teacher_name_value = []
    open_value = []
    close_value = []
    value_count = 0
    while True:
        value_count += 1
        class_code_value.append(input("강의코드 (예: IB171106, OB0104 ..): "))
        class_name_value.append(input("강의명 (예: IOT 빅데이터 실무반): "))
        teacher_name_value.append(input("강사 (예: 이현구): "))
        open_value.append(input("개강일 (예 2017-11-06):"))
        close_value.append(input("종료일 (예 2018-09-05):"))
        continue_value = (input("현재 수강하는 과목이 더 있습니까? (y/n):"))
        if continue_value == 'n':
            break
    for i in range(0, value_count):
        json_data[line_cnt]["total_course_info"]["learning_course_info"].append({"close_date": close_value[i],
                                                                                 "course_code": class_code_value[i],
                                                                                 "course_name": class_name_value[i],
                                                                                 "open_date": open_value[i],
                                                                                 "teacher": teacher_name_value[i]})


    json_write(json_data)

def insert_json():
    while True:
        class_code_value = []
        class_name_value = []
        teacher_name_value = []
        open_value = []
        close_value = []
        id=[]
        print("<신규 학생 정보 입력>")
        value_count=0
        name_value2=input("이름 (예: 홍길동) (종료:'enter'): ")
        if name_value2=="":
            break
        else :
            name_value = name_value2
        age_value=int(input("나이 (예:29): "))
        address_value=input("주소 (예: 대구광역시 동구 아양로 135):")
        class_count=int(input("과거 수강 횟수 (예:1): "))
        class_value=str(input("현재 수강 과목이 있습니까? (예:y/n): "))
        if class_value=='y':
            while True:
                value_count += 1
                class_code_value.append(input("강의코드 (예: IB171106, OB0104 ..): "))
                class_name_value.append(input("강의명 (예: IOT 빅데이터 실무반): "))
                teacher_name_value.append(input("강사 (예: 이현구): "))
                open_value.append(input("개강일 (예 2017-11-06):"))
                close_value.append(input("종료일 (예 2018-09-05):"))
                continue_value = (input("현재 수강하는 과목이 더 있습니까? (y/n):"))
                if continue_value == 'n':
                    break

        json_data = json_read()

        line_cnt=0
        while True:
            try:
                if json_data[line_cnt]['student_ID']:
                    id.append(json_data[line_cnt]['student_ID'])
                    line_cnt += 1
            except Exception:
                break
        id.sort()
        for i in id:
            id_num=int(i[-3:])

        if id_num<10:
            id_append='00'+str(id_num+1)
        elif id_num<100:
            id_append = '0'+str(id_num+1)
        elif id_num<1000:
            id_append=id_num+1
        ID="ITT"+id_append

        json_data.append({"address": address_value, "student_ID": ID, "student_age": age_value, "student_name": name_value,
                          "total_course_info": {"learning_course_info": [], "num_of_course_learned": class_count}})

        for i in range(0,value_count):
            json_data[line_cnt]["total_course_info"]["learning_course_info"].append({"close_date": close_value[i],
                                                                               "course_code": class_code_value[i],
                                                                               "course_name": class_name_value[i],
                                                                               "open_date": open_value[i],
                                                                               "teacher": teacher_name_value[i]})

        json_write(json_data)

def search_all():
    json_data = json_read()
    line_cnt=0

    while True:
        try:
            if json_data[line_cnt]['student_ID']:
                print("ID: %s \n이름: %s \n나이: %s \n주소: %s" % (
                json_data[line_cnt]["student_ID"], json_data[line_cnt]["student_name"],
                json_data[line_cnt]["student_age"], json_data[line_cnt]["address"]))
                print("과거 수강횟수 : %s"%json_data[line_cnt]['total_course_info']['num_of_course_learned'])
                # print(json_data[line_cnt]['total_course_info']['learning_course_info'][0])
                line_cnt2 = 0
                while True:
                    try:

                        if json_data[line_cnt]['total_course_info']['learning_course_info']==[]:
                            break

                        elif json_data[line_cnt]['total_course_info']['learning_course_info']:
                            print("강의코드:%s \n강의명:%s \n강사명:%s"%(
                                json_data[line_cnt]['total_course_info']['learning_course_info'][line_cnt2]["course_code"],
                                json_data[line_cnt]['total_course_info']['learning_course_info'][line_cnt2]["course_name"],
                                json_data[line_cnt]['total_course_info']['learning_course_info'][line_cnt2]["teacher"],))
                            print("강의시작일시:%s \n강의종료일시:%s " %(
                            json_data[line_cnt]['total_course_info']['learning_course_info'][line_cnt2]["open_date"],
                            json_data[line_cnt]['total_course_info']['learning_course_info'][line_cnt2]["close_date"]))

                        line_cnt2 += 1
                    except Exception:
                        break
                line_cnt += 1
                print("---------------------------------")
        except Exception:
            break

def search_choice(line_all,mode):
    json_data = json_read()

    for line_cnt in line_all:
        line_cnt=int(line_cnt)
        try:
            if json_data[line_cnt]['student_ID'] and mode==0:
                print("ID: %s \n이름: %s \n나이: %s \n주소: %s" % (
                json_data[line_cnt]["student_ID"], json_data[line_cnt]["student_name"],
                json_data[line_cnt]["student_age"], json_data[line_cnt]["address"]))
                print("과거 수강횟수 : %s"%json_data[line_cnt]['total_course_info']['num_of_course_learned'])
                # print(json_data[line_cnt]['total_course_info']['learning_course_info'][0])
                line_cnt2 = 0
                while True:
                    try:
                        if json_data[line_cnt]['total_course_info']['learning_course_info']==[]:
                            break
                        elif json_data[line_cnt]['total_course_info']['learning_course_info']:
                            print("강의코드:%s \n강의명:%s \n강사명:%s"%(
                                json_data[line_cnt]['total_course_info']['learning_course_info'][line_cnt2]["course_code"],
                                json_data[line_cnt]['total_course_info']['learning_course_info'][line_cnt2]["course_name"],
                                json_data[line_cnt]['total_course_info']['learning_course_info'][line_cnt2]["teacher"],))
                            print("강의시작일시:%s \n강의종료일시:%s " %(
                            json_data[line_cnt]['total_course_info']['learning_course_info'][line_cnt2]["open_date"],
                            json_data[line_cnt]['total_course_info']['learning_course_info'][line_cnt2]["close_date"]))
                        line_cnt2 += 1
                    except Exception:
                        break


                print("---------------------------------")
        except Exception:
            break
        if mode==1:
            print(">> 학생 ID: %s, 학생 이름: %s"%( json_data[line_cnt]["student_ID"], json_data[line_cnt]["student_name"]))

def search_json():
    while True:
        json_data=json_read()
        print("1. 전체 학생정보 조회 \n검색 조건 선택 \n2. ID 검색 \n"
              "3. 이름 검색 \n4. 나이 검색 \n5. 주소 검색 \n6. 과거 수강 횟수 검색 \n"
              "7. 현재 강의를 수강중인 학생 \n8. 현재 수강 중인 강의명 \n9. 현재 수강 강사 \n0. 이전 메뉴")
        search_type=input("메뉴를 선택하세요: ")
        if search_type =='0':
            break
        elif search_type=='1':
            search_all()
        elif search_type=='2':
            search_data(json_data,"student_ID",0)
        elif search_type=='3':
            search_data(json_data,"student_name",0)
        elif search_type == '4':
            search_data(json_data,"student_age",1)
        elif search_type == '5':
            search_data(json_data,"address",0)
        elif search_type == '6':
            search_data(json_data,"num_of_course_learned",2)
        elif search_type == '7':
            search_data(json_data,"course_code",4)
        elif search_type == '8':
            search_data(json_data,"course_name",3)
        elif search_type == '9':
            search_data(json_data,"teacher",3)


def search_data(json_data,search_data,search_mod):
    if search_mod != 4:
        input_data =input("검색할 값을 입력하세요: ")
    name_cnt = []
    count = 0
    while True:

        if search_mod == 0:
            try:
                if json_data[count][search_data].find(input_data) != -1 :
                    name_cnt.append(str(count))
            except Exception:
                pass
        elif search_mod == 1:
            try:
                if json_data[count][search_data] == int(input_data):
                    name_cnt.append(str(count))
            except Exception:
                pass
        elif search_mod == 2:
            try:
                if json_data[count]["total_course_info"][search_data] == int(input_data):
                    name_cnt.append(str(count))
            except Exception:
                pass
        elif search_mod == 3:
            line_cnt2=0
            while True:
                try:
                    if json_data[count]["total_course_info"]["learning_course_info"][line_cnt2]:
                        line_cnt2 += 1
                except Exception:
                    break
            try:
                for count_into in range(0, line_cnt2):
                    if json_data[count]["total_course_info"]["learning_course_info"][count_into][search_data].find(input_data) != -1 :
                        name_cnt.append(str(count))
                        name_cnt=list(set(name_cnt))
                        name_cnt.sort()
            except Exception:
                pass
        elif search_mod == 4:
            try:
                if json_data[count]["total_course_info"]["learning_course_info"][0][search_data]:
                    name_cnt.append(str(count))
            except Exception:
                pass
        try:
            if json_data[count]["student_name"]:
                count += 1
        except Exception:
            break

    # print(count)
    if len(name_cnt) > 1:
        print("복수 개의 결과가 검색되었습니다. \n  ----- 요약 결과 -----  ")
        search_choice(name_cnt, 1)
    else:
        search_choice(name_cnt, 0)

def update_json():
    while True:
        line_cnt=0
        id_date=[]
        json_data = json_read()

        update_id2=input("수정할 학생 ID를 입력하세요 (종료:'enter'): ")

        if update_id2=="":
            break
        else :
            update_id = update_id2

        while True:
            try:
                if json_data[line_cnt]['student_ID']:
                    id_date.append(json_data[line_cnt]['student_ID'])
                    if json_data[line_cnt]["student_ID"] == update_id:
                        break
                    line_cnt += 1
            except Exception:
                break
        try:
            id_date.index(update_id)
        except Exception:
            print("해당 ID의 학생이 없습니다")
            continue
        update_type = input("1. 학생 이름 \n2. 나이 \n3. 주소 \n4. 과거 수강 횟수 \n5. 현재 수강 중인 강의 정보 \n0. 이전 메뉴 \n메뉴 번호를 입력하세요: ")
        if update_type=='0':
            break
        elif update_type=='1':
            json_data[line_cnt]['student_name'] = input("변경할 값을 입력하세요: ")
        elif update_type=='2':
            json_data[line_cnt]['student_age'] = int(input("변경할 값을 입력하세요: "))
        elif update_type == '3':
            json_data[line_cnt]['address'] = input("변경할 값을 입력하세요: ")
        elif update_type == '4':
            json_data[line_cnt]['total_course_info']['num_of_course_learned'] = int(input("변경할 값을 입력하세요: "))
        elif update_type == '5':
            line_cnt2=0
            sel_update = ''
            while True:
                try:
                    if json_data[line_cnt]["total_course_info"]["learning_course_info"][line_cnt2]:
                        line_cnt2 += 1
                except Exception:
                    break
            for count_into in range(0,line_cnt2):
                if json_data[line_cnt]["total_course_info"]["learning_course_info"][count_into]:
                    print("%s.%s"%(count_into+1,json_data[line_cnt]["total_course_info"]["learning_course_info"][count_into]['course_name']))

            # print(line_cnt2)
            if line_cnt2==0:
                sel_point=input("과목이 존재하지않습니다 추가하실려면 'y'을 눌러주세요':")
                if sel_point == 'y':
                    insert_update(json_data,line_cnt)
                else:
                    break
            else:
                sel_update=input("변경할 과목을 선택해주세요(없다면 'enter'): ")

            if sel_update=='' or int(sel_update)-1>line_cnt2 :
                break
            else:
                print("1. 강의 코드 \n2. 강의명 \n3. 강사 \n4. 개강일 \n5. 종료일 \n0. 취소")
                sel_update2 = input("메뉴 번호를 입력하세요: ")
                if sel_update2 =='0':
                    break
                elif  sel_update2 =='1':
                    json_data[line_cnt]["total_course_info"]["learning_course_info"][int(sel_update)-1]["course_code"] = input("변경할 값을 입력하세요: ")
                elif  sel_update2 =='2':
                    json_data[line_cnt]["total_course_info"]["learning_course_info"][int(sel_update)-1]["course_name"] = input("변경할 값을 입력하세요: ")
                elif  sel_update2 =='3':
                    json_data[line_cnt]["total_course_info"]["learning_course_info"][int(sel_update)-1]["teacher"] = input("변경할 값을 입력하세요: ")
                elif  sel_update2 =='4':
                    json_data[line_cnt]["total_course_info"]["learning_course_info"][int(sel_update)-1]["open_date"] = input("변경할 값을 입력하세요: ")
                elif  sel_update2 =='5':
                    json_data[line_cnt]["total_course_info"]["learning_course_info"][int(sel_update)-1]["close_date"] = input("변경할 값을 입력하세요: ")
                else:
                    break

        json_write(json_data)
        search_choice(str(line_cnt),0)
        break

def del_json():
    while True:
        json_data = json_read()
        line_cnt = 0
        id_date=[]
        del_id2=input("삭제할 학생 ID를 입력하세요 (종료:'enter'):  ")
        if del_id2=="":
            break
        else :
            del_id = del_id2
        while True:
            try:
                if json_data[line_cnt]['student_ID']:
                    id_date.append(json_data[line_cnt]['student_ID'])
                    if json_data[line_cnt]["student_ID"] == del_id:
                        break
                    line_cnt += 1
            except Exception:
                break
        try:
            id_date.index(del_id)
        except Exception:
            print("해당 ID의 학생이 없습니다")
            continue


        print("삭제 유형을 선택하세요.")
        del_type=input("1. 전체 삭제 \n2. 현재 수강 중인 특정 과목정보 삭제 \n3. 이전 메뉴 \n메뉴 번호를 선택하세요: ")
        if del_type=='3':
            break
        elif del_type=='1':
            for count in range(0,line_cnt+1):
                try:
                    if json_data[count]["student_ID"]==del_id:
                        del json_data[count]
                        print("삭제가 완료되었습니다.")
                        json_write(json_data)
                        break
                except Exception:
                    pass

        elif del_type=='2':
            line_cnt=0
            line_cnt2=0
            while True:
                try:
                    if json_data[line_cnt]['student_ID']:
                        if json_data[line_cnt]["student_ID"] == del_id:
                            break
                        line_cnt += 1
                except Exception:
                    break
            while True:
                try:
                    if json_data[line_cnt]["total_course_info"]["learning_course_info"][line_cnt2]:
                        line_cnt2 += 1
                except Exception:
                    break
            for count_into in range(0,line_cnt2):
                if json_data[line_cnt]["total_course_info"]["learning_course_info"][count_into]:
                    print("%s.%s"%(count_into+1,json_data[line_cnt]["total_course_info"]["learning_course_info"][count_into]['course_name']))

            sel_del=input("삭제할 과목을 선택해주세요(없다면 'enter'): ")
            if sel_del=='':
                break
            else:
                del json_data[line_cnt]["total_course_info"]["learning_course_info"][int(sel_del)-1]
                print("삭제가 완료되었습니다")
                json_write(json_data)
                break

while True:
    print("   << json기반 주소록 관리 프로그램 >>")
    input_data=input("1.학생 정보입력 \n2.학생 정보조회 \n3.학생 정보수정 \n4.학생 정보삭제 \n5.프로그램 종료 ")
    if input_data=='5':
        print("학생 정보 관리 프로그램을 종료합니다.")
        quit()
    elif input_data=='1':  # 입력
        insert_json()
    elif input_data == '2':  # 조회
        search_json()
    elif input_data == '3':  # 수정
        update_json()
    elif input_data == '4':  # 삭제
        del_json()
