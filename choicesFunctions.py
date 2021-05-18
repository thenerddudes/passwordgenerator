# Choices Functions
# Written by arathalion and andrewmeyerle
# 05/16/2021
# Function for choices

import validator

LETTERS = 1
NUMBERS = 2
SYMBOLS = 3
ONLYNUMBS = 4
QUIT = 5

print('Here are your options:')
print('Option 1: upper and lowercase letters')
print('Option 2: uppercase, lowercase, and numbers')
print('Option 3: uppercase, lowercase, numbers, and symbols')
print('Option 4: Numbers')
print('Option 5: Quit')
choice = input('What option do you want')

while choice != QUIT:

    choice = displayMenu(options)

    if choice == 1:
        inputFunctions.passGen(scores)
    elif choice == 2:
        dispResults(scores)
    elif choice == 3:
        bkup = sortScores(scores)
    elif choice == 4:
        removeHighLow(scores)
    else:
        choice = getConf(choice)