import json


with open("sample.json", encoding='UTF8') as json_file: json_object = json.load(json_file)
json_string = json.dumps(json_object)
g_json_big_data = json.loads(json_string)

print(g_json_big_data)
print(g_json_big_data[0])
#json 데이터 읽기(read)
print(g_json_big_data[0]['레벨 2-1 키'])
#json 데이터 쓰기, 삽입(create)
g_json_big_data.append({"레벨 2-4 키":"수박"})
print(g_json_big_data)
#json 데이터 수정(update)
g_json_big_data[0]['레벨 2-1 키']='체리'
#json 데이터 삭제(Delete)
del g_json_big_data[2]

#자식 레벨의 딕셔너리 값 접근
g_json_big_data[1]['레벨 2-3 키']['레벨 3-1 키'][0]['레벨 4-1 키']='24'
print(g_json_big_data[1]['레벨 2-3 키']['레벨 3-1 키'][0]['레벨 4-1 키'])

pass

with open('ITT_Studenc.json','w',encoding='utf8') as outfile:
        readable_result=json.dumps(g_json_big_data,indent=4,sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
print('ITT_Student.json SAVED')