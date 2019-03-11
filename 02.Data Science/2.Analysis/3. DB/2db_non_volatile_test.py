import csv
import sqlite3
import sys

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
#전체 레코드 조회 readlines()
#열 필터링 하는 조건
# output = c.execute("SELECT * FROM Suppliers")
# output = c.execute("SELECT Supplier_Name FROM Suppliers")
output = c.execute("SELECT Supplier_Name,cost FROM Suppliers")

rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)