'''
This file is acts as driver.
This file has main method.
'''

from mainFile import *


# main method ,gets input from user and performs operation across other files.

def main():
    try:
        # input from user to perform operations

        print('To add a Department to the system , press 0')
        print('To add an Employee to the system, Press 1')
        print('To remove an Employee from system, Press 2')
        print('To update an Employee details, Press 3')
        print('To Search and display results, press 4')
        print('To display data of all Employees, Press 5')
        print('To display all departments, press 6')
        print('To remove a department, press 7')
        print('To Update a department ,press 8')
        print('To exit, Press 9')

        optionEnteredByUser = int(input())

        if (optionEnteredByUser > -1 and optionEnteredByUser < 10) == False:
            raise OptionEntredByUserNotValid('Input should be a number with range 0 to 9.Please try again')

        if (optionEnteredByUser == 0):
            call_zero()
            print('Department Added\nOther Operations are\n')
            main()

        if (optionEnteredByUser == 1):
            call_one()
            print('Employee data added. Other operations are below\n')
            main()

        if (optionEnteredByUser == 2):
            call_two()
            print('Employee data deleted. Other operations are below\n')
            main()

        if (optionEnteredByUser == 3):
            call_three()
            print('Employee Details Updated')
            main()

        if (optionEnteredByUser == 4):
            call_four()
            print('Result is Displayed')
            main()

        if (optionEnteredByUser == 5):
            print("Data is extracted from 'employee.txt' :")
            readFromFile('employee.txt')
            print('\nFurther Operations :\n')
            main()

        if (optionEnteredByUser == 6):
            print("Data is extracted from 'department.txt' :")
            readFromFile('department.txt')
            print('\nFurther Operations :\n')
            main()

        if (optionEnteredByUser == 7):
            call_seven()
            print('Department data deleted. Other operations are below\n')
            main()

        if (optionEnteredByUser == 8):
            call_eight()
            print('Department Details Updated')
            main()


        if (optionEnteredByUser == 9):
            print("Thank You For Using Employee Management System.")


    except departmentNameCannotBeSpace as dncbs:
        dncbs.printException()
        print(dncbs.message)
        print('\nTry Again\n')
        main()

    except OptionEntredByUserNotValid as a:
        print(a.message)
        print('\nTry Again\n')
        main()

    except InputTypeError as ie:
        print(ie.message)
        print('\nEnter Values Again\n')
        main()

    except dobError as de:
        print(de.message)
        print('\nTry again\n')
        main()

    except InputTypeError_dept as ied:
        print(ied.message)
        main()

    except duplicateEntryInEmpTable as deit:
        print(deit.message)
        main()

    except duplicateEntryInDeptTable as deidt:
        print(deidt.message)
        main()

    except userTableCoulmnInputException as utc:
        print(utc.message)
        print('\nEnter table heading again\n')
        main()

    except searchResultNotFoundForDeletion as snd:
        print(snd.message)
        print('\nData not found , please try again\n')
        main()

    except userTableCoulmnInputExceptionForUpdate as uip:
        print(uip.message)
        print('\nEnter Valid data and try again\n')
        main()

    except searchResultNotFoundForUpdating as su:
        print(su.message)
        print('\nEnter Valid data and try again\n')
        main()

    except userTableCoulmnInputExceptionForSearch as stc:
        print(stc.message)
        print('\nEnter teable heading again\n')
        main()

    except Exception as e:
        print(e)
        print('\nPlease try again...\n')
        main()


# running of main method

if __name__ == '__main__':
    print('Welcome To Employee Management System')
    print('-------------------------------------')
    main()
