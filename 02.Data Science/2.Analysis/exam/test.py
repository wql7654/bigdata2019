
import MySQLdb
import time
import csv

con = MySQLdb.connect(host='localhost', port=3306, db='it_student2', user='root', passwd='1111',charset='utf8mb4')
mysql_set = con.cursor()
table_name='student'

output_full=[]

mysql_set.execute(
    "select * from student_info b left outer join student_languages s on b.student_id = s.student_id where b.student_id='ITT002';")
rows = mysql_set.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    output_full.append(output)

output_full.sort()

print(output_full[0][0])