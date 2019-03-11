import json
import MySQLdb

con = MySQLdb.connect(host='localhost', port=3306, db='itstudent', user='root', passwd='1111' ,charset='utf8mb4')
c = con.cursor()



c.execute("SELECT * FROM Suppliers")

rows = c.fetchall()
print(rows)

ID='ITT001'
name_value='c'
age_value=25
major_value='s'
v=['c","c++']
h=''
m='cㄴz'
l='c++'

# language_value=set(language_value)
# language_level_hi=set(language_level_hi)
# language_level_mid=set(language_level_mid)
# language_level_low=set(language_level_low)
print(v)
v=''.join(v)
print(v)

c.execute("""INSERT INTO Suppliers VALUES ('%s', '%s', %s, '%s', '%s', '%s', '%s', '%s');"""
          %(ID,name_value,age_value,major_value,v,h,m,l))
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
print(rows)

con.commit()

# print(int(str(sorted(list(rows),reverse=True)[0])[3:6]))

