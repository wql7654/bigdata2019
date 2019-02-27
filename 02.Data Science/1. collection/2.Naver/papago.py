import os
import sys
import urllib.request
client_id = "NADxMDXvTe3NS1FpMO14" # 개발자센터에서 발급받은 Client ID 값
client_secret = "SMaMyJYTOM" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote("나는 정헌킴 이라고 합니다 당신은 누구신지 알고싶습니다")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)