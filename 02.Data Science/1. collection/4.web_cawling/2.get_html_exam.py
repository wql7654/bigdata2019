import requests
from bs4 import BeautifulSoup
from xml.etree.ElementTree import parse, Element, dump, SubElement, ElementTree


response =requests.get('http://www.weather.go.kr/weather/observation/currentweather.jsp')
soup=BeautifulSoup(response.content,'html.parser')

table=soup.find('table', {'class':'table_develop3'})
data=[]

def data_correction(org_text):
    if org_text == '\xa0':
        return 'N/A'
    return org_text

for tr in table.find_all('tr'):
    tds=list(tr.find_all('td'))

    for td in tds:
        if td.find('a'):
            point =data_correction(td.find('a').text)
            cloud = data_correction(tds[1].text)
            visibility = data_correction(tds[2].text)
            temperature=data_correction(tds[5].text)
            wd_temp=data_correction(tds[7].text)

            humidity=data_correction(tds[10].text)
            wdirection_wind=data_correction(tds[11].text)
            wind_speed=data_correction(tds[12].text)
            wind_speed=wind_speed.split("'")[1]

            data.append([point, cloud,visibility,temperature,wd_temp,humidity,wdirection_wind,wind_speed])

weather_list = Element("html")
weather=SubElement(weather_list,"table")
SubElement(weather,"tr")
SubElement(weather,"td").text="지점"
SubElement(weather,"td").text="현재일기"
SubElement(weather,"td").text="시정"
SubElement(weather,"td").text="현재기온"
SubElement(weather,"td").text="체감온도"
SubElement(weather,"td").text="습도"
SubElement(weather,"td").text="풍향"
SubElement(weather,"td").text="풍속"

for data_insert in data:
    SubElement(weather, "tr")
    for data_insert2 in range(0,len(data_insert)):
        SubElement(weather, "td").text = data_insert[data_insert2]


ElementTree(weather_list).write("weather.html",encoding='UTF-8',xml_declaration=True)

