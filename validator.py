# This module contains Validation Functions
# these are generic validation and can be used with any program


def isNumeric(message):
    value = input("Enter " + message + " ")
    while not(value.isdigit()):
        # print()
        value = input(message + " must be numeric ")
    return value


def getInteger(min, max, message):
    # print("Enter " + message)
    # value =  int(input("Enter " + message + " "))
    value = int(isNumeric(message))
    
    while value < min or value > max:
        # print()
        value = int(input(message + " must be within range of " + str(min) + " to " + str(max) + " "))
    return value


def getFloat(min, max, message):
    # print("Enter " + message)
    value = float(input("Enter " + message + " "))
    while value < min or value > max:
        # print("Enter a Value within range of " + str(min) + " to " + str(max))
        value = float(input(message + " must be within range of " + str(min) + " to " + str(max) + " "))
    return value


def requiredEntry(message):
    value = input("Enter " + message + " ")
    while value == "":
        # print("Enter a Value within range of " + str(min) + " to " + str(max))
        value = input(message + " is required, Please re-enter ")
    
    return value


def isAlphabetic(entry, message):
    # value =  input("Enter " + message + " ")
    while not(entry.isalpha()):
        # print("Enter a Value within range of " + str(min) + " to " + str(max))
        entry = input(message + " must be alphabetic, Please re-enter ")
    
    return entry
