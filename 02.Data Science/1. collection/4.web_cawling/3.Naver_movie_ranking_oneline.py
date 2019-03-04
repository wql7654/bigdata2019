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

all3 = re.compile('title="(.*)">.*</a>.*\s+.' #영화이름
                  '*\s+.*\s+.*\s+.*\s+.*\s+alt=\W(.+)" ' #영화업다운
                  'c.*\s+<\w+\s\w+="\w+\s\w+">(\d)+</td>\s{1,5}') #영화 급등락
allline = all3.findall(str(soup), re.MULTILINE | re.DOTALL | re.VERBOSE)
print(allline)
tags=['','','']
list_movie=0
for tag in allline:
    tags=list(tag)
    if tags[0].find(',')!=-1:
        tags[0]='"'+tags[0]+'"'
    if tags[1] == 'na':
        tags[1]=''
    elif tags[1] == 'up':
        tags[1]="+"
    elif tags[1] == 'down':
        tags[1]='-'
    sel_list = []
    sel_list.append(str(list_movie+1))
    sel_list.append(tags[0])
    sel_list.append(tags[1]+tags[2])
    all_list.append(sel_list)
    list_movie+=1

re=[]
res=['순위,영화명,변동폭\n']
for i in all_list:
    re=','.join(i)
    re=re+'\n'
    res.append(re)

with open("./movie_ranking3.csv", 'w') as f:
    f.writelines(res)
