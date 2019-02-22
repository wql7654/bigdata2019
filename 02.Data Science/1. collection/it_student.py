import json


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
        name_value2=input("이름 (예: 홍길동): ")
        if name_value2=="":
            break
        else :
            name_value = name_value2
        age_value=input("나이 (예:29): ")
        address_value=input("주소 (예: 대구광역시 동구 아양로 135):")
        class_count=input("과거 수강 횟수 (예:1): ")
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


        with open("ITT_Student.json", encoding='UTF8') as json_file:
            json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_data = json.loads(json_string)


        line_cnt=0
        while True:
            try:
                if json_data[line_cnt]['student_ID']:
                    id.append(json_data[line_cnt]['student_ID'])
                    line_cnt += 1
            except Exception:
                break

        print(id)
        id.sort()
        for i in id:
            id_num=int(i[-3:])

        print(i)
        line_cnt-=1

        if id_num<10:
            id_append='00'+str(id_num+1)
        elif id_num<100:
            id_append = '0'+str(id_num+1)
        elif id_num<1000:
            id_append=id_num+1
        ID="ITT"+id_append

        #
        json_data.append({"address":address_value})
        json_data.append({"student_ID":ID})
        json_data.append({"student_age": age_value})
        json_data.append({"name":name_value})

        # json_data["total_course_info":{"learning_course_info":]
        json_first=[] =
        for i in range(0,value_count):
            json_first[i].append({"close_date":close_value[i]})
            json_first[i].append({"course_code": class_code_value[i]})
            json_first[i].append({"course_name": class_name_value[i]})
            json_first[i].append({"open_date": open_value[i]})
            json_first[i].append({"teacher": teacher_name_value[i]})

        json_data["total_course_info"].append({"num_of_course_learned":class_count})

        # with open('ITT_Studenc.json', 'w', encoding='utf8') as outfile:
        #     readable_result = json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False)
        #     outfile.write(readable_result)


insert_json()
# while True:
#     print("   << json기반 주소록 관리 프로그램 >>")
#     input_data=input("1.학생 정보입력 \n2.학생 정보조회 \n3.학생 정보수정 \n4.학생 정보삭제 \n5.프로그램 종료 ")
#     if input_data=='5':
#         print("학생 정보 분석 완료!")
#         quit()
#     elif input_data=='1':  # 입력
#         insert_json()
#     elif input_data == '2':  # 조회
#         search_json()
#     elif input_data == '3':  # 수정
#         update_json()
#     elif input_data == '4':  # 삭제
#         del_json()
