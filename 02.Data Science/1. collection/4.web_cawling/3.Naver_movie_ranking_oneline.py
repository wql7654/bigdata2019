import urllib.request
from bs4 import BeautifulSoup
import re

html=urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup=BeautifulSoup(html,'html.parser')

name_list=[]
up_down_list=[]
up_down_num=[]
all_list=[]
up_downs=''

all3 = re.compile('<a \w+="/\w+/\w+/\w+/\w+.\w+[?]\w+=\d+" title="(.*)">.*</a>.*\s+.*\s+.*\s+.*\s+.*\s+.*\s+alt=\W(.+)" c.*\s+<\w+\s\w+="\w+\s\w+">(\d)+</td>\s{1,5}</tr>')
allline = all3.findall(str(soup), re.MULTILINE | re.DOTALL)

tags=['','','']
for tag in allline:
    tags=list(tag)
    if tags[0].find(',')!=-1:
        tags[0]='"'+tags[0]+'"'
    name_list.append(tags[0])
    if tags[1] == 'na':
        tags[1]=''
    elif tags[1] == 'up':
        tags[1]="+"
    elif tags[1] == 'down':
        up_downs='-'
    up_down_list.append(tags[1])

    up_down_num.append(tags[2])




for list_movie in range(0,len(name_list)):
    sel_list = []
    sel_list.append(str(list_movie+1))
    sel_list.append(name_list[list_movie])
    sel_list.append(up_down_list[list_movie]+up_down_num[list_movie])
    all_list.append(sel_list)


re=[]
res=['순위,영화명,변동폭\n']
for i in all_list:
    re=','.join(i)
    re=re+'\n'
    res.append(re)

with open("movie_ranking3.csv", 'w') as f:
    f.writelines(res)
