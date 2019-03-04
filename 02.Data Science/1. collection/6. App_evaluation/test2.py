import urllib.request
from bs4 import BeautifulSoup
import re

html=urllib.request.urlopen('https://gall.dcinside.com/board/lists/?id=bitcoins')
soup=BeautifulSoup(html,'html.parser')

name_list=[]
up_down_list=[]
up_down_num=[]
all_list=[]
up_downs=''

all3 = re.compile('''icon_\w+"></\w+>(.+)</a>\s+</td>''') #영화 급등락
allline = all3.findall(str(soup), re.MULTILINE | re.DOTALL | re.VERBOSE)
print(allline)
# tags=['','','']
# list_movie=0
# for tag in allline:
#     tags=list(tag)
#     sel_list = []
#     sel_list.append(str(list_movie+1))
#     sel_list.append(tags[0])
#     sel_list.append(tags[1]+tags[2])
#     all_list.append(sel_list)
#     list_movie+=1
#
# re=[]
# res=['순위,영화명,변동폭\n']
# for i in all_list:
#     re=','.join(i)
#     re=re+'\n'
#     res.append(re)
#
# with open("./movie_ranking3.csv", 'w') as f:
#     f.writelines(res)
