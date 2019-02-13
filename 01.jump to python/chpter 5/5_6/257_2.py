import time

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())

print(time.strftime('%Z', time.localtime(time.time())) )