'''
Used in creation of department Database,CURD operations are here
'''
from sqlite3 import *

conn_dept = connect('depatrment.db')

ex_dept = conn_dept.cursor()


# creating department table .I dis auto generated and auto incremented

def createTabelDeptTable():
    ex_dept.execute('''CREATE TABLE IF NOT EXISTS dept(dept_id integer primary key autoincrement,dept_name text)''')


# Insertion of data to DB

def insertValuesDeptTable(dept_name):
    with conn_dept:
        ex_dept.execute('''INSERT INTO dept VALUES(Null,?)''', (dept_name,))


# Removing Data from DB

def deleteValuesDeptTable(value):
    with conn_dept:
        ex_dept.execute("DELETE from dept WHERE dept_id = (?)", (value,))


# update operation in DB

def updateDatainDeptTable(name, id):
    with conn_dept:
        ex_dept.execute('''UPDATE dept SET dept_name = (?) where dept_id = (?)''', (name, id))


# selecting only dept names

def selectValuesOtherThenId_dept():
    ex_dept.execute('''SELECT * FROM dept''')
    lis_dept = ex_dept.fetchall()
    nlis_dept = list(map(list, lis_dept))
    nwlis_dept = list(map((lambda x: x[1:]), nlis_dept))
    return nwlis_dept


# selecting all values

def selectAllvalues_dept():
    ex_dept.execute('''SELECT * FROM dept''')
    lis_dept = ex_dept.fetchall()
    nlis_dept = list(map(list, lis_dept))
    return nlis_dept
