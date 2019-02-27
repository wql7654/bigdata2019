
import json
import urllib.request

def json_write(json_data):
    with open('naver_test.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)



money="KRW"
coin="BTC"


# encText = urllib.parse.quote("인더타이거")
url = "https://api.upbit.com/v1/ticker?markets="+money+'-'+coin
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