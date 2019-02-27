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
up_down_rank = all3.findall(str(soup), re.MULTILINE | re.DOTALL)

print(up_down_rank)


name_mov = re.compile('<a \w+="/\w+/\w+/\w+/\w+.\w+[?]\w+=\d+" title="(.*)">.*</a>')
tags = name_mov.findall(str(soup), re.MULTILINE | re.DOTALL)
for tag in tags:
    if tag.find(',')!=-1:
        tag='"'+tag+'"'
    name_list.append(tag)


all = re.compile(r'''alt=\W(.+)" c''')

up_down_info = all.findall(str(soup), re.MULTILINE | re.DOTALL)
# print(up_down_info)
for up_down in up_down_info:
    if up_down == 'na':
        up_downs=''
    elif up_down == 'up':
        up_downs="+"
    elif up_down == 'down':
        up_downs='-'
    up_down_list.append(up_downs)

all2 = re.compile(r'''<\w+\s\w+="\w+\s\w+">(\d)+</td>\s{1,5}</tr>''')
up_down_rank = all2.findall(str(soup), re.MULTILINE | re.DOTALL)
for up_down in up_down_rank:
    up_down_num.append(up_down)





for list_movie in range(0,len(name_list)):
    sel_list = []
    sel_list.append(str(list_movie+1))
    sel_list.append(name_list[list_movie])
    sel_list.append(up_down_list[list_movie]+up_down_num[list_movie])
    all_list.append(sel_list)


# print(all_list)
re=[]
res=['순위,영화명,변동폭\n']
for i in all_list:
    re=','.join(i)
    re=re+'\n'
    res.append(re)


# print(res)


with open("movie_ranking2.csv", 'w') as f:
    f.writelines(res)

