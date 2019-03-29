import urllib.request
import datetime
import json
import time
import os
import re
from bs4 import BeautifulSoup
from xml.etree.ElementTree import parse, Element, dump, SubElement, ElementTree

access_key="YHt09t28DYtoaKEfFxq%2Fjh0lxcidcTTWWywGQYJi1hxqmrOdWQ5hKmxlPYl8pX2Gro6rw96Drd47O%2BKK5vbl0w%3D%3D"

def get_Request_URL(url):                 ## (1) 기상 정보(동네예보정보 조회 서비스) / (2) 통합대기환경 정보(대기오염정보 조회 서비스)
    req = urllib.request.Request(url)     ## request 날리는 함수

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def get_Weather_URL(day_time):       ## (1) 기상 정보(동네예보정보 조회 서비스) request 보내기 전, url 만드는 함수
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + yyyymmdd
    parameters += "&base_time=" + day_time
    parameters += "&nx=" + x_coodinate
    parameters += "&ny=" + y_coodinate
    parameters += "&numOfRows=100"

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def get_Air_URL():
    end_point="http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    #api 주소
    parameters = "?ServiceKey="+access_key #서비스 키
    parameters +="&sidoName="+urllib.parse.quote(sidoName) #파싱할 지역
    parameters +="&ver="+ver_info #api 버전관리

    url = end_point + parameters
    retData = urllib.request.urlopen(url)

    return retData #베이스가 json이라 json데이터로 리턴

def Make_Weather_Json(day_time):     ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 생성하는 함수
    jsonData = get_Weather_URL(day_time)

    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for prn_data in jsonData['response']['body']['items']['item']:
            json_weather_result.append({'baseDate': prn_data.get('baseDate'),
                               'baseTime': prn_data.get('baseTime'),
                               'category': prn_data.get('category'),
                               'fcstDate': prn_data.get('fcstDate'),
                               'fcstTime': prn_data.get('fcstTime'),
                               'fcstValue': prn_data.get('fcstValue'),
                               'nx': prn_data.get('nx'),
                               'ny': prn_data.get('ny')})

    return json_weather_result




def indent(elem, level=0):
    i="\n"+ level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
           elem.tail=i



def Make_Air_XML():
    XMLData=get_Air_URL()

    tree = parse(XMLData)  # 생성한 xml 파일 파싱하기
    note = tree.getroot()
    return_data=[]
    for parent in note.getiterator("body"):
        for items in parent.getiterator("items"):
            for item in items.getiterator("item"):
                station= item.findtext("stationName")
                if station==station_name:
                    return_data.append(item.findtext("stationName"))
                    return_data.append(item.findtext("dataTime"))
                    return_data.append(item.findtext("khaiValue"))
                    return_data.append(item.findtext("khaiGrade"))
                    return_data.append(item.findtext("pm10Value"))
                    return_data.append(item.findtext("pm25Value"))



    response_xml = Element("response")
    body_xml = SubElement(response_xml, "body")
    items_xml = SubElement(body_xml, "items")
    item_xml = SubElement(items_xml, "item")
    SubElement(item_xml, "stationName").text = return_data[0]
    SubElement(item_xml, "dataTime").text = return_data[1]
    SubElement(item_xml, "khaiValue").text = return_data[2]
    SubElement(item_xml, "khaiGrade").text = return_data[3]
    SubElement(item_xml, "pm10Value").text = return_data[4]
    SubElement(item_xml, "pm25Value").text = return_data[5]
    indent(response_xml)


    return response_xml,return_data

def data_saved(xml_air,json_weather,day_time):
    ElementTree(xml_air).write('대구_미세먼지_측정조회_%s_%s.xml' % (yyyymmdd, day_time), encoding='UTF-8', xml_declaration=True)
    print('대구_미세먼지_측정조회_%s_%s.xml SAVED' % (yyyymmdd, day_time))

    with open('동구_신암동_초단기예보조회_%s%s.json' % (yyyymmdd, day_time), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_weather, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s.json SAVED\n' % (yyyymmdd, day_time))


def data_saved_csv(day_time):
    all_list=[]
    data_list=[]
    sel_list=[]
    filename="인공지능모드 저장데이터"
    extension="csv"

    json_weather = Make_Weather_Json(day_time)
    xml_air = Make_Air_XML()[1]
    res = ['현재위치','측정일시','측정예상온도','날씨','강수형태','습도','통합대기환경지수','미세먼지농도','초미세먼지농도','통합대기환경수치']
    for data_js in json_weather:
        if data_js['category']=="T1H":
            T1H=str(data_js['fcstValue'])+'℃'
        if data_js['category']=="SKY":
            SKY=data_js['fcstValue']
            if SKY == 1: SKY_info="맑음"
            elif SKY == 2: SKY_info = "구름조금"
            elif SKY == 3: SKY_info = "구름많음"
            elif SKY == 4: SKY_info = "흐림"
        if data_js['category']=="PTY":
            PTY=data_js['fcstValue']
            if PTY == 0: PTY_info="없음"
            elif PTY == 1: PTY_info = "비"
            elif PTY == 2: PTY_info = "비또는눈"
            elif PTY == 3: PTY_info = "눈"
        if data_js['category']=="REH":
            REH=str(data_js['fcstValue'])+'%'

    air_info=''
    if xml_air[3]== '1': air_info="좋음"
    elif xml_air[3] == '2': air_info = "보통"
    elif xml_air[3] == '3': air_info = "나쁨"
    elif xml_air[3] == '4': air_info = "매우나쁨"

    file_system=os.listdir('./')
    resc = ','.join(file_system)
    if resc.find(filename)==-1:
        all_list.append(res)

    data_list.append(xml_air[0])
    data_list.append(xml_air[1])
    data_list.append(T1H)
    data_list.append(SKY_info)
    data_list.append(PTY_info)
    data_list.append(REH)
    data_list.append(air_info)
    data_list.append(xml_air[4]+'㎍/㎥')
    data_list.append(xml_air[5]+'㎍/㎥')
    data_list.append(xml_air[2])
    all_list.append(data_list)
    for i in all_list:
        clear_code = ','.join(i)
        clear_code = clear_code + '\n'
        sel_list.append(clear_code)


    with open("./%s.%s"%(filename,extension), 'a') as f:
        f.writelines(sel_list)


def get_Realtime_Weather():        ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 만들기 전, 실시간 업데이트 확인 함수
    day_min_int = int(day_min)        ##참고사항임!!
    day_time=''
    if 30 < day_min_int <= 59:      ## 실시간 업데이트가 있는지 없는지 확인,, 30분부터 59분까지는 실시간 정보 업데이트 됨
        day_time = time.strftime("%H%M", time.localtime(time.time()))
        print("\n<<실시간 기상정보 업데이트를 실시합니다!!>>\n".center(30))


    elif 0 <= day_min_int <= 30:        ## 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전껄로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        revised_min = 60 + (day_min_int-30) # 정확히 30분을 뺀다.
        day_time = "{0:0>2}".format(day_hour_int) + str(revised_min)      ## 시간이 한 자리 수일 때 930 되는 것을 0930으로 바꿔 줌

        print("\n<<가장 최신 기상정보 업데이트를 실시합니다!!>>\n".center(30))

    json_weather=Make_Weather_Json(day_time)
    xml_air=Make_Air_XML()[0]
    data_saved(xml_air,json_weather,day_time)
    data_saved_csv(day_time)


    return day_min_int

def crawring_data():
    html = urllib.request.urlopen('http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=102&date=%s' % time.strftime("%Y%m%d"))
    soup = BeautifulSoup(html, 'html.parser')

    num=0
    while True:
        num+=1
        today_news_info=soup.find('li', attrs={'class': 'ranking_item is_num%s'%num})
        name_new = re.compile('.+lede">\s+(.+).*\s+.*</div>') #요약뉴스를 정규식으로 정리
        tags = name_new.findall(str(today_news_info), re.MULTILINE | re.DOTALL)
        print("제목:%s"%today_news_info.a['title'])
        print("뉴스요약:%s"%tags)
        herf_today_news_info="http://news.naver.com" + today_news_info.a['href']
        print("바로가기:%s"%herf_today_news_info)


        if num == 10:
            break


def main_weather():
    global json_weather_result
    global yyyymmdd
    global day_time
    global day_hour
    global day_min
    global x_coodinate
    global y_coodinate

    global sidoName
    global ver_info
    global station_name


    json_weather_result = []
    yyyymmdd = time.strftime("%Y%m%d")
    day_time = time.strftime("%H%M")
    day_hour = time.strftime("%H")
    day_min = time.strftime("%M")
    x_coodinate = "89"
    y_coodinate = "91"

    sidoName='대구'
    ver_info='1.3'

    station_name='신암동'


    get_Realtime_Weather()

# main_weather()
# crawring_data()

