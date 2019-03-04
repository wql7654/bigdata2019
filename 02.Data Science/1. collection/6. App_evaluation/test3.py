import urllib.request
from bs4 import BeautifulSoup
import requests
import datetime
import json
import time
import glob


html=urllib.request.urlopen('https://gall.dcinside.com/board/lists/?id=bitcoins') #게시판조회
soup=BeautifulSoup(html,'html.parser')

response_all = urllib.requests.urlopen("https://api.upbit.com/v1/market/all") # 종목조회

# market 업비트에서 제공중인 시장 정보.
# korean_name 거래 대상 암호화폐 한글명
# english_name 거래 대상 암호화폐 영문명

url = "https://api.upbit.com/v1/ticker"
querystring = {"markets":"markets"}
response_ticket = requests.request("GET", url, params=querystring)


print(response_all.text)

access_key="KCTLlGysZ9ZhXhXnxLxCh1Mqnxv9JRDvoF8PPwhO"
pass_key="rdWgfDQbVt1EfoAHbuWPsJprNDmm5bygRgrv5Brp"


