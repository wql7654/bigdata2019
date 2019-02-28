import os
import time

import re
num=0
soup=[]

folder_data="V3_BigData"
folder_file="naver_ranking"
extension=".csv"
try:
    if os.listdir('./%s'%folder_data):
        pass
    else:
        os.mkdir("./%s/%s%s"%(folder_data,folder_file,num+1))  # 폴더생성
except Exception:
    os.mkdir("./%s"%(folder_data))
    os.mkdir("./%s/%s%s"%(folder_data,folder_file,num+1))

file_folder=os.listdir("./%s"%(folder_data))
all2 = re.compile('ranking([0-9]+)')
allmain = all2.findall(str(file_folder))
for i in allmain[-1:]:
    ic=int(i)

os.chdir("%s"%folder_data)
if len(os.listdir('./%s%d'%(folder_file,ic))) %3 == 0 and len(os.listdir('./%s%d'%(folder_file,ic))) != 0:
    ic=ic + 1
    os.mkdir('./%s%d'%(folder_file,ic)) # 폴더생성
    os.chdir('./%s%d'%(folder_file,ic))
else:
    os.chdir('./%s%d'%(folder_file,ic))


with open("%s%s"%(time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time())),extension), 'w') as f:
    f.write('res')









