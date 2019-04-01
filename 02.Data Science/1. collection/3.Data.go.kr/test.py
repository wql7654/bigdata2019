import json



with open("대구광역시_관광지입장정보_2011_2016.json", encoding="utf-8") as json_data:
    json_data_load = json.load(json_data)
    json_data_string = json.dumps(json_data_load)
    jsonResult = json.loads(json_data_string)

list=[]
for i in range(len(jsonResult)):
    list.append(jsonResult[i]['resNm'])

list=set(list)
print(list)