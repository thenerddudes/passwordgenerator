# Main Function
# Written by arathalion
# 05/16/2021
# Main Password generator function

import inputFunctions
import validator


def main():

def displayMenu(option):  # Menu Display
    print(f"\n Score Calculator Menu \n")

    for o in option:
        print(o)
    print()

    return validator.getInteger(1, 7, "Option")