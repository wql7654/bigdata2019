import json



with open("ITT_Student.json",encoding='UTF8') as json_file: json_object = json.load(json_file)
json_string = json.dumps(json_object)
g_json_big_data = json.loads(json_string)

print("z")
print(g_json_big_data[2]['student_ID'])
bcs='0'
bc=0

g_json_big_data.append({"address":"hello"})

# while True:

        # try:
        #         if g_json_big_data[bc]['student_ID']:
        #                 bc += 1
        #         print(bc)
        # except Exception:
        #         break



print(g_json_big_data)

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