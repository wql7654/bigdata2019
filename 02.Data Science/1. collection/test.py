import json



with open("ITT_Student.json",encoding='UTF8') as json_file: json_object = json.load(json_file)
json_string = json.dumps(json_object)
g_json_big_data = json.loads(json_string)
print(g_json_big_data[1]["total_course_info"]["learning_course_info"][1]["course_name"])
print(g_json_big_data)
# g_json_big_data[0]['total_course_info']['num_of_course_learned']='ㄴ'
g_json_big_data[1]["total_course_info"]["learning_course_info"][1]["close_date"] = 2121212
# del g_json_big_data[1]["total_course_info"]["learning_course_info"][2]
print(g_json_big_data[1]["total_course_info"]["learning_course_info"])
# g_json_big_data[0]["total_course_info"]["learning_course_info"][0]["teachers"]="hi"
# g_json_big_data.dumps({"teachers":"njo"})

# json 데이터 읽기(read)
# print(g_json_big_data[0]['레벨 2-1 키'])
#json 데이터 쓰기, 삽입(create)
# g_json_big_data.append({"레벨 2-4 키":"수박"})
#json 데이터 수정(update)
# g_json_big_data[0]['레벨 2-1 키']='체리'

# print(dict.keys())
print("z")
# print(g_json_big_data[2]['student_ID'])
bcs='0'
bc=0
print(g_json_big_data)
# g_json_big_data.append({"address":"hello"})

# while True:

        # try:
        #         if g_json_big_data[bc]['student_ID']:
        #                 bc += 1
        #         print(bc)
        # except Exception:
        #         break



#

# for parent in g_json_big_data[0]['student_ID']:
#         print(parent)
#         id.append(parent)

print(id)
# id.sort()
# for i in id:
#         id_num = int(i[-3:])


# with open('ITT_Studenc.json','w',encoding='utf8') as outfile:
#         readable_result=json.dumps(g_json_big_data,indent=4,sort_keys=True, ensure_ascii=False)
#         outfile.write(readable_result)
# print('ITT_Student.json SAVED')