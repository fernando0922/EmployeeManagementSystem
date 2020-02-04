'''
This file has methods relating to reading from file and writing to file.
'''

from dbrelated import *
from deptdbrelated import *


# this function reads from file and displays in terminal or console

def readFromFile(filePath):
    try:
        fout = open(filePath, 'r')
        print(fout.read())
        fout.close()
    except FileNotFoundError:
        print(filePath + ' File is not present.')
        f = open(filePath, 'w')
        f.close()
        print('File Created,Kindly Repeat this operation')


# this functions reads from db and writes to text file

def writeToFile(filePath):
    fin = open(filePath, 'w')
    wtr = selectAllValues()  # data from DB coming as list whose elements are also lists
    for i in wtr:
        fin.write('Employee ID : ' + str(i[0]) + '\n')
        fin.write('First Name : ' + i[1] + '\n')
        fin.write('Last Name : ' + i[2] + '\n')
        fin.write('DOB : ' + i[3] + '\n')
        fin.write('Department : ' + i[4] + '\n')
        fin.write('----------------------------------\n')
    fin.close()

#this function writes data to department.txt

def writeToFileDept(filePath):
    finDept = open(filePath, 'w')
    nlis_dept = selectAllvalues_dept()  # data from dept DB coming as list whose elements are also lists
    for i in nlis_dept:
        finDept.write('department id : ' + str(i[0])+'\n')
        finDept.write('department name : ' + i[1]+'\n')
        finDept.write('-------------------------'+'\n')
