import json

def json_read():
    with open("ITT_Student.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_data = json.loads(json_string)
    return json_data

def json_write(json_data):
    with open('ITT_Studenc.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)

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

        json_data.append({"address": address_value, "student_ID": ID, "student_age": age_value, "name": name_value,
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
                        if json_data[line_cnt]['total_course_info']['learning_course_info']:
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

def search_json():
    while True:
        json_data=json_read()
        print("1. 전체 학생정보 조회 \n검색 조건 선택 \n2. ID 검색 \n3. 이름 검색 \n4. 나이 검색 \n5. 주소 검색 \n6. 과거 수강 횟수 검색 \n7. 현재 강의를 수강중인 학생 \n8. 현재 수강 중인 강의명 \n9. 현재 수강 강사 \n0. 이전 메뉴")
        search_type=input("메뉴를 선택하세요: ")
        if search_type =='0':
            break
        elif search_type=='1':
            search_all()
        elif search_type=='2':
            pass




def update_json():
    while True:
        line_cnt=0
        id_date=[]
        json_data = json_read()

        update_id=input("수정할 학생 ID를 입력하세요:  ")

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
            while True:
                try:
                    if json_data[line_cnt]["total_course_info"]["learning_course_info"][line_cnt2]:
                        line_cnt2 += 1
                except Exception:
                    break
            for count_into in range(0,line_cnt2):
                if json_data[line_cnt]["total_course_info"]["learning_course_info"][count_into]:
                    print("%s.%s"%(count_into+1,json_data[line_cnt]["total_course_info"]["learning_course_info"][count_into]['course_name']))

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
        break

def del_json():
    while True:
        json_data = json_read()
        line_cnt = 0
        id_date=[]
        del_id=input("삭제할 학생 ID를 입력하세요:  ")
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

            for count in range(0,line_cnt):
                if json_data[count]["student_ID"]==del_id:
                    del json_data[count]
                    print("삭제가 완료되었습니다.")
                    json_write(json_data)
                    break

        elif del_type=='2':
            line_cnt=0
            line_cnt2=0
            while True:
                try:
                    if json_data[line_cnt]['student_ID']:
                        line_cnt += 1
                        if json_data[line_cnt]["student_ID"] == del_id:
                            break
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



# json_first[0]["total_course_info"]["learning_course_info"][i]["learning_course_info"]=close_value[i]
# json_first[0]["total_course_info"]["learning_course_info"][i]["course_code"]=class_code_value[i]
# json_first[0]["total_course_info"]["learning_course_info"][i]["course_name"]=class_name_value[i]
# json_first[0]["total_course_info"]["learning_course_info"][i]["open_date"]=open_value[i]
# json_first[0]["total_course_info"]["learning_course_info"][i]["teacher"]=teacher_name_value[i]

search_all()
# search_json()
# while True:
#     print("   << json기반 주소록 관리 프로그램 >>")
#     input_data=input("1.학생 정보입력 \n2.학생 정보조회 \n3.학생 정보수정 \n4.학생 정보삭제 \n5.프로그램 종료 ")
#     if input_data=='5':
#         print("학생 정보 관리 프로그램을 종료합니다.")
#         quit()
#     elif input_data=='1':  # 입력
#         insert_json()
#     elif input_data == '2':  # 조회
#         search_json()
#     elif input_data == '3':  # 수정
#         update_json()
#     elif input_data == '4':  # 삭제
#         del_json()
