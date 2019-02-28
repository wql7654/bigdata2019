import re
import glob


file_folder = glob.glob('./동구*')
# file_folder = os.listdir("./동구*")
all2 = re.compile('_([0-9]+)')
ss = all2.findall(str(file_folder))
print(int(ss[0]))