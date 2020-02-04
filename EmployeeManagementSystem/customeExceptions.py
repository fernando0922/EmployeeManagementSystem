'''
 All classes are child of Exceptions.
These are custom exceptions
'''


class OptionEntredByUserNotValid(Exception):
    def __init__(self, message):
        self.message = message

    def printException(self):
        return self.message


class InputTypeError(Exception):
    def __init__(self, message):
        self.message = message

    def printException(self):
        return self.message


class InputTypeError_dept(Exception):
    def __init__(self, message):
        self.message = message

    def printException(self):
        return self.message


class dobError(Exception):
    def __init__(self, message):
        self.message = message

    def printException(self):
        return self.message


class userTableCoulmnInputException(Exception):
    def __init__(self, message):
        self.message = message

    def printException(self):
        return self.message


class userTableCoulmnInputExceptionForUpdate(Exception):
    def __init__(self, message):
        self.message = message

    def printException(self):
        return self.message


class userTableCoulmnInputExceptionForSearch(Exception):
    def __init__(self, message):
        self.message = message

    def printException(self):
        return self.message


class searchResultNotFoundForSearching(Exception):
    def __init__(self, message):
        self.message = message

    def printException(self):
        return self.message


class searchResultNotFoundForUpdating(Exception):
    def __init__(self, message):
        self.message = message

    def printException(self):
        return self.message


class searchResultNotFoundForDeletion(Exception):
    def __init__(self, message):
        self.message = message

    def printException(self):
        return self.message


class departmentNameCannotBeSpace(Exception):
    def __init__(self, message):
        self.message = message

    def printException(self):
        return self.message


class duplicateEntryInEmpTable(Exception):
    def __init__(self, message):
        self.message = message

    def printException(self):
        return self.message

class duplicateEntryInDeptTable(Exception):
    def __init__(self, message):
        self.message = message

    def printException(self):
        return self.message