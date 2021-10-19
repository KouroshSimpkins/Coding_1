"""An easy way to access all of my programs for Coding1"""

import sys
import Week2
import Week3


def main():
    """Works as main for MainMenu
    Should not be able to run from another file."""

    while True:
        Week2.cls()
        print("Avaliable Weeks ->    2    3")
        userChoice = input("Select a week number > ")
        if userChoice == "2":
            Week2.cls()
            print("1 = ", Week2.threeIntegers.__doc__)
            print()
            print("2 = ", Week2.getCharsInText.__doc__)
            print()
            print("3 = ", Week2.Option3)
            print()
            userChoice = int(input("> "))
        elif userChoice == "3":
            Week2.cls()
            print("4 = ", Week3.greeting.__doc__)
            print()
            print("5 = ", Week3.pygLatinWords.__doc__)
            print()
            userChoice = int(input("> "))
        elif userChoice == "q":
            sys.exit()

        if userChoice == 1:
            print(Week2.threeIntegers())
            input("Press Enter to return to the menu")
        elif userChoice == 2:
            print(Week2.getCharsInText())
            input("Press Enter to return to the menu")
        elif userChoice == 3:
            print(Week2.divisionAsSubtractionSeries())
            input("Press Enter to return to the menu")
        elif userChoice == 4:
            print(Week3.greeting())
            input("Press Enter to return to the menu")
        elif userChoice == 5:
            print(Week3.pygLatinWords())
            input("Press Enter to return to the menu")


if __name__ == '__main__':
    main()
