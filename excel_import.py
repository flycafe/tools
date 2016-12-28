#!/usr/bin/env python

import xlrd
import MySQLdb

#open workbook and sheet
book = xlrd.open_workbook("Workbook1.xls")
sheet = book.sheet_by_name("Sheet1")

#create connection to mysql
conn = MySQLdb.connect(host = "192.168.56.95", user = "test", passwd = "test1234", db = "test")

#create cursor object to 
cursor = conn.cursor()

#create insert sql
query = "insert into sheet1 (id,name) values (%s, %s)"

#read & insert each row in sheet(if have title, need to skip and start from second row)
for r in range(0, sheet.nrows):
        id = sheet.cell(r,0).value
        name = sheet.cell(r,1).value
        values = (id, name)
        cursor.execute(query, values)

cursor.close()
conn.commit()
conn.close()

columns = sheet.ncols
rows = sheet.nrows

print "Done! %s columns, %s rows impported." %(columns, rows)
