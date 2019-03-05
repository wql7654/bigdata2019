
import os


# with open("./test.csv", 'r') as f:
#     test=f.read()

b=[]
with open("인공지능모드 저장데이터.csv", 'r') as f:
    line = []
    while True:
        line = f.readline()
        if not line: break
        b=line.split(',')

print(b[6])


