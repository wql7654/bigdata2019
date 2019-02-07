# coding: cp949

a="201901300915-0175440.002"
year=a[:4]
month=a[4:6]
day=a[6:8]
time=a[8:10]
minute=a[10:12]
temp=a[12:15]
dust=a[15:17]
u_dust=a[17:19]
ozon=a[-5:]

print("year:" +year+  "\nmonth:" +month+ "\n" "day:"+day+ "\n" "time:"+time+ "\n")
print("minute:"+minute+"\n" "temp:"+temp+ "\n" "dust:"+dust+ "\n" "u+dust:"+u_dust+"\n" "ozon:"+ozon+"\n")
