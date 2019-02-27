import urllib.request
from bs4 import BeautifulSoup

html=urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup=BeautifulSoup(html,'html.parser')


# print(soup)
# print(soup.prettify())  # 인덴테이션 구조에 맞춰서 만들어줌

tags=soup.findAll('div', attrs={'class':'tit3'})
tagss=soup.findAll('div', attrs={'title':'사바하'})
up_down=soup.find('img',attrs={'src':'https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif'})

print(tags)
print(up_down)
print(tagss)

# with open("movie_ranking.cav", 'wb') as f:
#     f.write()


