import json
import MySQLdb
import pandas as pd


con = MySQLdb.connect(host='localhost', port=3306, db='it_student', user='root', passwd='1111',charset='utf8mb4')
c = con.cursor()

# c.execute("SELECT student_id FROM %s" %'student')
# rows = c.fetchall()
# id_num = int(str(sorted(list(rows), reverse=True)[0])[5:8])
# print(id_num)
search_data=input("dd")
if search_data == '상':
    level = 'High_level'
elif search_data == '중':
    level = 'Middle_level'
elif search_data == '하':
    level = 'Low_level'
try:
    print("SELECT * FROM %s where %s like %%_%%;" % ('student', level))
    c.execute("SELECT * FROM %s where '%s' like '%%_%%';" % ('student', level))
except Exception:
    pass
# c.execute("SELECT * FROM student where student_id='ITT002';")

rows = c.fetchall()
output_full = []
print(rows)

# for row in rows:
#     output = []
#     for column_index in range(len(row)):
#         output.append(str(row[column_index]))
#     output_full.append(output)
# print(output_full)

# mysql_set.execute("SELECT * FROM student where student_id='ITT002';")
# update customer set grade='Gold' where account='bank';


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


# c.execute("""INSERT INTO student VALUES ('%s', '%s', %s, '%s', %s, %s, %s, %s);"""
#           %(ID,name_value,age_value,major_value,language_value,language_level_hi,language_level_mid,language_level_low))
#
# print(int(str(sorted(list(rows),reverse=True)[0])[3:6]))

