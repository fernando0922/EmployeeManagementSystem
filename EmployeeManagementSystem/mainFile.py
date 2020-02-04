'''
All methods are called from driver.py
'''
from fileReadWrite import *
from validations import *
from dbrelated import *
from deptdbrelated import *


# Add a department to Department table

def call_zero():
    print('Enter Department Name')
    dept = setDeptName(input().upper())
    createTabelDeptTable()
    if (dept.isspace() or dept == ''):
        raise departmentNameCannotBeSpace('Department Name Cannot Be Space or empty')

    if [dept] in selectValuesOtherThenId_dept():
        raise duplicateEntryInDeptTable('This is a Duplicate Entry, Enter Department name again')
    insertValuesDeptTable(dept)
    writeToFileDept('department.txt')


# Add an employee to employee table

def call_one():
    print('Enter First Name')
    fn = setFirstName(input().upper())
    print('Enter Last Name')
    ln = setLastName(input().upper())
    print('Enter DOB in DD/MM/YYYY')
    db = setDob(str(input()))
    print('Enter Department')
    dept = setDepartment(input().upper())
    createTabel()
    if [fn, ln, db, dept] in selectValuesOtherThenId():
        raise duplicateEntryInEmpTable('\nThis is a Duplicate Entry,Please Try Again\n')
    insertValues(fn, ln, db, dept)
    writeToFile('employee.txt')


# search for a record using regex and remove an item from employee table

def call_two():
    print('Enter Employee ID, so that employee details can be deleted')
    print('Enter Employee ID.')
    userTableCloumnData = input()

    if searchForRecord('emp_id', userTableCloumnData):
        removeAnItem(userTableCloumnData)
        writeToFile('employee.txt')
    else:
        raise searchResultNotFoundForDeletion('\nData does not Exists in DB,enter valid data\n')


# search for a record or row item and if present , update it

def call_three():
    print('Enter column name which has to be updated')
    print('enter "first_name" or "last_name" or "dob" or "department"')
    userTableCoulmnInputOne = input()

    if (
            userTableCoulmnInputOne == 'first_name' or userTableCoulmnInputOne == 'last_name' or userTableCoulmnInputOne == 'dob' or userTableCoulmnInputOne == 'department') == False:
        raise userTableCoulmnInputExceptionForSearch(
            '\nInput should be "emp_id" or "first_name" or "last_name" or "dob" or "department", kindly try again\n')

    print('Enter new column data.')

    if userTableCoulmnInputOne == 'first_name':
        userInputNewData = setFirstName(input().upper())
    elif userTableCoulmnInputOne == 'last_name':
        userInputNewData = setLastName(input().upper())
    elif userTableCoulmnInputOne == 'dob':
        userInputNewData = setDob(str(input()))
    elif userTableCoulmnInputOne == 'department':
        userInputNewData = setDepartment(input().upper())

    userTableCoulmnInputTwo = 'emp_id'

    print('ENTER Employee Id')

    userTableDataInputTwo = int(input())

    if searchForRecord(userTableCoulmnInputTwo, userTableDataInputTwo):
        updateAnItem(userTableCoulmnInputOne, userInputNewData, userTableCoulmnInputTwo, userTableDataInputTwo)
        writeToFile('employee.txt')
    else:
        raise searchResultNotFoundForUpdating('\nData does not Exists in DB,enter valid data\n')


# searching for a record in employee table with employee id or first name as key

def call_four():
    print('Enter a column name and data , so that employee detail can be Fetched')
    print('enter "emp_id" or "first_name"')
    userTableCoulmnInput = input()

    if (userTableCoulmnInput == 'emp_id' or userTableCoulmnInput == 'first_name') == False:
        raise userTableCoulmnInputExceptionForSearch('\nInput should be "emp_id" or "first_name" , kindly try again\n')
    print('Enter a column data.')

    if userTableCoulmnInput == 'emp_id':
        userTableCloumnData = int(input())
    elif userTableCoulmnInput == 'first_name':
        userTableCloumnData = input().upper()

    if searchForRecord(userTableCoulmnInput, userTableCloumnData):
        resultList = selectRequiredValues(userTableCoulmnInput, userTableCloumnData)
    else:
        raise searchResultNotFoundForSearching('\nData does not Exists in DB,enter valid data\n')

    for i in resultList:
        print('Employee ID : ' + str(i[0]))
        print('First Name : ' + i[1])
        print('Last Name : ' + i[2])
        print('DOB : ' + i[3])
        print('Department : ' + i[4])
        print('--------------------------')


# search a record in department table and delete if present

def call_seven():
    print('Enter Department ID, so that Department details can be deleted')
    print('Enter Department ID.')
    userTableCloumnDataDept = input()

    if searchForRecordDept(userTableCloumnDataDept):
        deleteValuesDeptTable(userTableCloumnDataDept)
        writeToFileDept('department.txt')
    else:
        raise searchResultNotFoundForDeletion('\nData does not Exists in DB,enter valid data\n')


# search a record in department DB and update same record if present

def call_eight():
    userTableCoulmnInputOneDept = 'dept_name'
    print('Enter New DepartMent name')
    userInputNewDataDept = setDeptName(input().upper())
    userTableCoulmnInputTwoDept = 'dept_id'
    print('ENTER DEPARTMENT Id')
    userTableDataInputTwoDept = int(input())
    if searchForRecordDept(userTableDataInputTwoDept):
        updateDatainDeptTable(userInputNewDataDept, userTableDataInputTwoDept)
        writeToFileDept('department.txt')
    else:
        raise searchResultNotFoundForUpdating('\nData does not Exists in DB,enter valid data\n')
