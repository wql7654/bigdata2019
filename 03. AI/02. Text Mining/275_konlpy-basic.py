from konlpy.tag import Okt
# from konlpy.tag import Twitter
##이전버전은 twitter 신버전은 Okt
twitter = Okt()
# twitter2 = Twitter()

malist = twitter.pos('아버지 가방에 들어가신다.', norm=True, stem=True)

print(malist)

malist = twitter.pos('아버지가 방에 들어가신다.', norm=True, stem=True)

print(malist)

malist = twitter.pos('당근당근당근당근', norm=True, stem=True)

print(malist)