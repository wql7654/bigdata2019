import json

print("========== 빅데이터 분석기 =================")
search_data_info=input("분석하실 데이터를 입력해주세요:")
# search_data_info='이명박'

with open("%s_naver_news.json"%search_data_info, encoding="utf-8") as json_data:
    json_data_load = json.load(json_data)
    json_data_string = json.dumps(json_data_load)
    jsonResult = json.loads(json_data_string)


print("데이터 분석을 시작합니다..")

all_data=0
err_data=0
domein_data=0
alldomein_data=[]
alldomein_count=[]
while True:
    try:
        if jsonResult[all_data]:
            all_data+=1
    except Exception:
        break

for count in range(0,all_data):

    if jsonResult[count]['org_link'].find("http") == -1:
        print("org_link'가 없는 기사를 발견했습니다.")
        err_data+=1
    else:
        alldomein_data.append(jsonResult[count]['org_link'].split('/')[2])



print("<네이버 검색 빅데이터 분석>")
print("검색어: %s"%search_data_info)
print("전체 도메인 수: %s"%len(set(alldomein_data)))
print("전체 건수: %s"%(all_data-err_data))
print("부정확한 데이터 수: %s"%err_data)

print("- 도메인 별 뉴스 기사 분석")
alldomein_data_pix=set(alldomein_data)
count_append=[]

for count in alldomein_data_pix:
    lists = []
    res = list(filter(lambda x: x==count, alldomein_data))
    lists.append(len(res))
    lists.append(count)
    count_append.append(lists)


count_append=sorted(count_append,reverse=True)

for count in count_append:
    print(">> %s : %s건" % (count[1], count[0]))


