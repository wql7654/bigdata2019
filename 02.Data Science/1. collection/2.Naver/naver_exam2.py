import os
import sys
import json
import urllib.request
from xml.etree.ElementTree import parse, Element, dump, SubElement, ElementTree

def json_write(json_data):
    with open('naver_test.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)



client_id = "702ad957-403d-4370-9d8e-10c36a86e621"
client_secret = ""

# encText = urllib.parse.quote("인더타이거")
url = "http://tools.kinds.or.kr:8888/today_category_keyword"  # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("access_key",client_id)
request.add_header("argument",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    json_write(response_body.decode('utf-8'))
    # ElementTree(response_body.decode('utf-8')).write("naver_xml.xml")

else:
    print("Error Code:" + rescode)