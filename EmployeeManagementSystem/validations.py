'''
All business logic and other depadent logics are present in this file
'''
from customeExceptions import *
from time import ctime
from dbrelated import *
from deptdbrelated import *
import re


# validation of first name, should be only alphabets

def setFirstName(firstname):
    if (str(firstname).isalpha()):
        return firstname
    else:
        raise InputTypeError('\nFirst Name Should be Alphabetic, Kindly provide Proper input\n')


# validation of last name, should be only alphabets

def setLastName(lastname):
    if (str(lastname).isalpha()):
        return lastname
    else:
        raise InputTypeError('\nLast Name Should be Alphabetic, Kindly provide Proper input\n')


# validation of dob and check for 25 years or more

def setDob(dob):
    if (str(dob).replace('/', '').isnumeric()):
        pass
    else:
        raise InputTypeError('\ndob Should be Numaric, Kindly provide Proper input\n')

    dobYear = str(dob).split('/')[-1]
    nowYear = str(ctime()).split(' ')[-1]

    if int(nowYear) - int(dobYear) >= 25:
        return dob
    else:
        raise dobError('\nAge should be 25 years or more to add into system\n')


# validation of department. Department name should be in Department table

def setDepartment(department):
    if ([department] in selectValuesOtherThenId_dept()):
        return department
    else:
        raise InputTypeError_dept(
            '\nDepartment Should be in Department Table, Kindly Enter Department Name and try again\n')

#validation for department name in department table

def setDeptName(deptName):
    if (str(deptName).isspace() or deptName==''):
        raise InputTypeError('\nDepartment Name Should be Alphabetic, Kindly provide Proper input\n')
    else:
        return deptName


# logic for searching data based on employee id or first_name by using regex

def searchForRecord(type, value):
    dbList = selectAllValues()
    reqList = []

    if (type == 'emp_id'):
        reqList = [i[0] for i in dbList]
        reqListStr = list(map(str, reqList))
        strReqListStr = ' '.join(reqListStr)
        strValue = str(value)
        if (re.search(strValue, strReqListStr)):
            return True
        else:
            return False

    if (type == 'first_name'):
        reqList = [i[1] for i in dbList]
        strReqListStr = ' '.join(reqList)
        strValue = str(value)
        if (re.search(strValue, strReqListStr)):
            return True
        else:
            return False

# search in Database of department

def searchForRecordDept(value) :
    dbListDept = selectAllvalues_dept()
    reqList = []
    reqList = [i[0] for i in dbListDept]
    reqListStr = list(map(str, reqList))
    strReqListStr = ' '.join(reqListStr)
    strValue = str(value)
    if (re.search(strValue, strReqListStr)):
        return True
    else:
        return False
