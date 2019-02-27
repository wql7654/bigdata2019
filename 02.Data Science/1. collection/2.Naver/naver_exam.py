import os
import sys
import json
import urllib.request
from xml.etree.ElementTree import parse, Element, dump, SubElement, ElementTree

def json_write(json_data):
    with open('naver_test.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)



client_id = "U0_KuDvTCHfM9ZEHehyJ"
client_secret = "f47t9dpwOF"

encText = urllib.parse.quote("인더타이거")
url = "https://openapi.naver.com/v1/search/blog?query=321" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    json_write(response_body.decode('utf-8'))
    # ElementTree(response_body.decode('utf-8')).write("naver_xml.xml")

else:
    print("Error Code:" + rescode)