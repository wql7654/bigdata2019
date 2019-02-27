
import json
import urllib.request

def json_write(json_data):
    with open('naver_test.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)



client_id = "66374c09922ef445bec075a7488b4c20"
client_secret = ""
value="targetDt=20180205"


# encText = urllib.parse.quote("인더타이거")
url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?&"+value+"&key="+client_id
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
data=urllib.request.urlopen(url).read()
j=json.loads(data)
print(j)


# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
#     json_write(response_body.decode('utf-8'))
    # ElementTree(response_body.decode('utf-8')).write("naver_xml.xml")

# else:
#     print("Error Code:" + rescode)