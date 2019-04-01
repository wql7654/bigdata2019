import pytagcloud
import random
import webbrowser
from konlpy.tag import Twitter
from collections import Counter

####################################################
# get_tags 새함수 만듦:
# 기능 1. 댓글별로 명사만 추출
# 기능 2. 명사 빈도수 집계
# 기능 3. 단어구름에 표시할 명사에 3가지 시각화 속성
#        (색상'color', 단어'tag', 크기'size')부여

# 입력변수- text : 댓글, ntags : 표시할 단어수, multiplier : 크기가중치
def get_tags(text, ntags=20, multiplier=2):
    t = Twitter()
    nouns = []

# 모든 댓글에서 명사만 추출하고 nouns변수에 누적해 저장함
    for sentence in text:
        for noun in t.nouns(sentence):
            nouns.append(noun)
            # 각 명사별로 빈도계산
            count = Counter(nouns)
    # n : 명사, c : 빈도
    return [{'color': color(),'tag':n,'size':2*c*multiplier} for n,c in count.most_common(ntags)]

# draw_cloud 새함수 만듦:
# 기능 1. pytagclud 모듈을 사용해 단어구름 이미지를 만듦
# 기능 2. 단어구름 이미지를 파일로 저장함
# 기능 3. 화면에 단어구름을 표시함

# 입력변수 tags : get_tags()에서 리턴되는 color, tag, size(이미지크기) 값이 전달됨.
# fontname : Noto Sans CJK - 한글폰트
def draw_cloud(tags, filename, fontname = 'Neucha',size1 = (600,800)):
    pytagcloud.create_tag_image(tags,filename,fontname=fontname,size=size1)
    # 저장된 단어구름 이미지파일(wc1.png)을 내 컴퓨터에 띄움
    webbrowser.open(filename)

####################################################
# 명사에 적용할 색상 랜덤지정
r = lambda: random.randint(0, 255)
color = lambda: (r(), r(), r())

# 옥자 댓글(okja1.txt) 읽기 전용으로 읽어들임.
okjak = []
file = open('Hong.txt', 'r', encoding ='utf-8')
lines = file.readlines()

for line in lines:
    okjak.append(line)
file.close()

####################################################
# 댓글 명사추출 및 빈도분석(get_tags) 실시
tags = get_tags(okjak)
print(tags)
# 관심명사 단어구름 이미지 파일 저장 및 출력하기
draw_cloud(tags,'wc1.png')

