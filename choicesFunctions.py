# Choices Functions
# Written by arathalion
# 05/16/2021
# Function for choices

import validator

PASS_GEN = 1
PASS_CRACK = 2
SORT_SCORES = 3
LOW_HIGH = 4
RESET_ORDER = 5
CLEAR_SCORES = 6
QUIT = 7

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
    elif choice == 5:
        scores = resetOrder(bkup)
    elif choice == 6:
        clearScores(scores)
    else:
        choice = getConf(choice)