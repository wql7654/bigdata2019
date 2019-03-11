import json
import MySQLdb
import pandas as pd


con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', passwd='1111')
c = con.cursor()



c.execute("SELECT student_id FROM student")
print(c)
rows = c.fetchall()

ID='ITT001'
name_value='윤민선'
age_value=25
major_value='컴퓨터공학과'
language_value='c,c++'
language_level_hi='c'
language_level_mid=''
language_level_low='c++'

# language_value=set(language_value)
# language_level_hi=set(language_level_hi)
# language_level_mid=set(language_level_mid)
# language_level_low=set(language_level_low)


c.execute("""INSERT INTO student VALUES %s, %s, %s, %s, %s, %s, %s, %s;"""
          %(ID,name_value,age_value,major_value,language_value,language_level_hi,language_level_mid,language_level_low))

print(int(str(sorted(list(rows),reverse=True)[0])[3:6]))

