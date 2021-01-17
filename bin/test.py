
import pyodbc
from pyodbc import Error
import os
DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'
MDB = f'{os.getcwd()}\\data\\alphaData.accdb'
PWD = 'An23011997'
for drivers in pyodbc.drivers():
    print(drivers)
conn = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
cursor = conn.cursor()
cursor.execute('select * from users')
a = []
for row in cursor.fetchall():
    try:
        if len(a==1):
            break
    except:
        pass
    a.append(row)
print(len(a), a)
