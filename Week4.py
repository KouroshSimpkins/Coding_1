"""Week 4 of Introduction to creative computing and coding practice"""

import os
import sys
import textwrap as tr


def cls():
    """Improves readability of Text interfaces by clearing the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def getList():

    listComplete = False
    outputArray = []
    info_str = "Press 'd' when you have entered all the values for your array"
    print(tr.fill(info_str, width = 30))

    while not listComplete:
        tmp = input("> ")

        if tmp == "d":
            listComplete = True
        else:
            outputArray.append(tmp)

    return(outputArray)


def multiplyList(arrayToMultiply):

    tmp = 1

    for i in range(len(arrayToMultiply)):
        tmp = tmp*int(arrayToMultiply[i])

    return(tmp)


def wordList(arrayOfWords):

    outputArray = []

    for i in range(len(arrayOfWords)):
        for j in range(len(arrayOfWords)):
            if i == j:
                pass
            else:
                outputArray.append(arrayOfWords[i]+" "+arrayOfWords[j])

    return(outputArray)


def main():
    """Main function acts as a menu"""

    while True:
    # cls clears the terminal window, makes readability better
        cls()

        # Just a basic menu layout
        print("Press 1 for list of numbers")
        print("Press 2 for list of words")
        print("Press q to quit")
        choice = input("> ")

        # choice allows the user to select which program they would like to run,
        # instead of running each program in order.
        if choice.lower() == "1":
            cls()
            arrayToMultiply = getList()
            print("Answer is:", multiplyList(arrayToMultiply))
            input("Press Enter to return to the menu")
        elif choice.lower() == "2":
            cls()
            arrayOfWords = wordList(getList())
            print("final array of words is:")
            for i in range(len(arrayOfWords)):
                print(arrayOfWords[i])
            input("Press Enter to return to the menu")
        elif choice.lower() == "q":
            sys.exit()
        else:
            print("Not a valid choice")


if __name__ == '__main__':
    main()
