'''
Creation of employee DB and functions related to it.CURD operations are here
'''
from sqlite3 import *

conn = connect('employees.db')

ex = conn.cursor()


# table creation,employes id is auto generated and auto incremented.

def createTabel():
    ex.execute('''CREATE TABLE IF NOT EXISTS emp(emp_id integer primary key autoincrement,first_name text,last_name text,dob text,department text)''')


# insert operations.Employee details will be inserted with help of dictionaries

def insertValues(fn, ln, db, dept):
    with conn:
        ex.execute('''INSERT INTO emp VALUES(Null,:fn,:ln,:db,:dept)''', {'fn': fn, 'ln': ln, 'db': db, 'dept': dept})


# returns list of all rows in db as list.
# employee id is not returned and output of this function will be input for checking duplicate data in employee table

def selectValuesOtherThenId():
    ex.execute('''SELECT * FROM emp''')
    lis = ex.fetchall()
    nlis = list(map(list, lis))
    nwlis = list(map((lambda x: x[1:]), nlis))
    return nwlis


# Returns all rows as a list (lists inside list)

def selectAllValues():
    ex.execute('''SELECT * FROM emp''')
    lis = ex.fetchall()
    nlis = list(map(list, lis))
    return nlis


# removes a row and input is employee id

def removeAnItem(value):
    with conn:
        ex.execute("DELETE from emp WHERE emp_id = (?)", (value,))


# updates existing data

def updateAnItem(updateColumnName, updateValue, conditionColumnName, conditionValue):
    if updateColumnName == 'last_name' and conditionColumnName == 'emp_id':
        with conn:
            ex.execute('''UPDATE emp SET last_name = (?) where emp_id = (?)''', (updateValue, conditionValue))

    if updateColumnName == 'first_name' and conditionColumnName == 'emp_id':
        with conn:
            ex.execute('''UPDATE emp SET first_name = (?) where emp_id = (?)''', (updateValue, conditionValue))

    if updateColumnName == 'dob' and conditionColumnName == 'emp_id':
        with conn:
            ex.execute('''UPDATE emp SET dob = (?) where emp_id = (?)''', (updateValue, conditionValue))

    if updateColumnName == 'department' and conditionColumnName == 'emp_id':
        with conn:
            ex.execute('''UPDATE emp SET department = (?) where emp_id = (?)''', (updateValue, conditionValue))


# assists in searching with employee id and first_name

def selectRequiredValues(type, value):
    if type == 'emp_id':
        ex.execute('''select * from emp where emp_id = (?)''', (value,))
    elif type == 'first_name':
        ex.execute('''select * from emp where first_name = (?)''', (value,))
    lis = ex.fetchall()
    nlis = list(map(list, lis))
    return nlis
