import os
import glob
import re
num=0
soup=[]


folder_data="V2_BigData"
folder_file="naver_ranking"
file_name="movie_ranking"
extension=".csv"

try:
    if os.listdir('./%s'%folder_data):
        pass
    else:
        os.mkdir("./%s/%s%s"%(folder_data,folder_file,num+1))  # 폴더생성
except Exception:
    os.mkdir('./%s'%folder_data)
    os.mkdir("./%s/%s%s"%(folder_data,folder_file,num+1))

file_folder=os.listdir('./%s'%folder_data)
all2 = re.compile('([0-9]+)')
allmain = all2.findall(str(file_folder))
while True:
    if glob.glob('./%s/%s%d/*'%(folder_data,folder_file,num)) != '':
        num+=1
        soup.append(glob.glob('./%s/%s%d/*'%(folder_data,folder_file,num)))
    if glob.glob('./%s/%s%d/*'%(folder_data,folder_file,num)) == []:
        break

all3 = re.compile('([0-9]+)')
allline = all3.findall(str(soup))

for i in allmain[-1:]:
    ic=int(i)

for i in allline[-1:]:
    ib=int(i)

os.chdir("%s"%folder_data)

try:
    if ib%3==0:
        ic = ic + 1
        os.mkdir('./%s%d' % (folder_file, ic))  # 폴더생성
        os.chdir('./%s%d' % (folder_file, ic))
    else:
        os.chdir('./%s%d' % (folder_file, ic))
except Exception:
    os.chdir('./%s%d' % (folder_file, ic))
    ib=0


with open("%s%d%s"%(file_name,ib+1,extension), 'w') as f:
    f.write('res')


