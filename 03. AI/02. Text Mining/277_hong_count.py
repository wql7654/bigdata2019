import codecs
from konlpy.tag import Okt

fp = codecs.open('test.txt', 'r', encoding='utf-8')
text = fp.read()
# 텍스트를 한 줄씩 처리하기
twitter = Okt()
word_dic = {}
lines = text.split('\r\n')
for line in lines:
    malist = twitter.pos(line)
    for word in malist:
        if word[1] == 'Noun':
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1 #카운트하기
# 많이 사용된 명사 출력하기
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print('{0}({1}) '.format(word, count), end='')
print()