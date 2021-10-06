# Kourosh Simpkins

import os
import time
# increases legibility of my info page
import textwrap as tr


'''quick function to improve readability'''
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


Option1 = '''Given 3 positive integers, find the sum of all numbers
between the first two that are a multiple of the third'''
def threeIntegers():
    cls()

    try:
        # Get the input for each number
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: "))
        third_num = int(input("Enter your third number: "))

        # Call on other definitions to
        sizes = findLarger(first_num, second_num)
        larger = sizes[0]
        smaller = sizes[1]
        third_num_arr = findMultiples(larger, smaller, third_num)

        # Temp will hold the sum, intialised it here outside the for loop
        temp = 0

        #iterate through array, pulling += on each and storing in temp
        for i in range(len(third_num_arr)):
            temp += third_num_arr[i]

        return temp

    except ValueError:
        # In the case that a user decides to enter a non integer, catch the error here and return to main menu
        print("The values you enter must be integers")
        time.sleep(1.5)


# finds the largest of two numbers and returns them as an array
def findLarger(num1, num2):
    # temporary vars
    larger = 0
    smaller = 0

    if num1 > num2:
        larger = num1
        smaller = num2
    elif num2 > num1:
        larger = num2
        smaller = num1

    sizes = [larger, smaller]

    return sizes


# finds values between first and second numbers that the third number goes into
def findMultiples(larger, smaller, numToEvaluate):
    # array of numbers that will be returned
    third_num_arr = []

    # loops through each number between two given, and adds to array
    for i in range(larger - smaller):
        if (i + smaller) % numToEvaluate == 0:
            third_num_arr.append(i + smaller)

    return third_num_arr


Option2 = '''Given a string of text, print the number of times each letter
in the alphabets a-z appear.'''
def getCharsInText():
    cls()
    # Create a dictionary which stores the alphabet alongside a value, which will change depending on the number of times a letter appears.
    alphabet = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

    text = str(input("Please enter some text to evaluate: "))
    # .lower ensures entire input string is stored as lowercase values, makes it easier to operate on.
    text = text.lower()

    # loops through each item in the input string, and checks against the dictionary
    for i in range(len(text)):
        # as long as the string is within the dictionary (as a key), then it should be possible to increment it's associated value, as is assumed here.
        # (This is a really shit implementation, it doesn't take into accont any possible garbage that is put in)
        # i.e. if the user enters anything that is not in the dictionary, the loop breaks and the entire thing returns to the main menu
        # not sure why it's not printing my exception command, which was the whole point of this try except block
        # all in all, might come back to this, but the logic works, it's just my error catching that seems to be crap.
        try:
            key = text[i]
            if key in alphabet:
                alphabet[key] += 1
        # TODO: #1 Fix this stupid error catcher
        except:
            print("an exception has occurred")
            time.sleep(3)
            break

    # Inline for statement, to print the dictionary in a more pleasing format
    [print(key,"appeared", value, "times") for key, value in alphabet.items()]


Option3 = '''Implemnt division as a series of subtraction. The program should only deal
with integers and report a remainder if there is one.'''
def divisionAsSubtractionSeries():
    cls()
    # initialise isRemainder to determine if there is or isn't a remainder at the end of the function
    isRemainder = False

    # try except to ensure the user only inputs integer values
    try:
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: "))

        temp = first_num
        i = 0

        while temp > 0:
            temp -= second_num
            i += 1

        # Inline if checking if temp is 0, if it is then isRemainder remains False, otherwise isRemainder will return True
        isRemainder = True if temp != 0 else False

        # Couldn't get this to work inline, not sure why but it was rather complex.
        # Might have another look at it later
        if isRemainder == False:
            print(first_num, "/", second_num, "=", i)
        elif isRemainder == True:
            print(first_num, "/", second_num, "=", i, "remainder", (first_num%second_num))

    # Throws an error message and then returns to the main menu
    except ValueError:
        print("The values you enter must be integers")
        time.sleep(1.5)


'''main function, just acts as a menu'''
def main():
    while True:
    # cls clears the terminal window, makes readability better
        cls()

        # Just a basic menu layout
        print("Press 1 for option 1 of the task")
        print("Press 2 for option 2")
        print("Press 3 for option 3")
        print("Enter q to quit, or i for info")
        choice = input("> ")

        # choice allows the user to select which program they would like to run, instead of running each program in order.
        if choice.lower() == "1":
            print("Value is", threeIntegers())
            input("Press Enter to return to the menu")
        elif choice.lower() == "2":
            getCharsInText()
            input("Press Enter to return to the menu")
        elif choice.lower() == "3":
            divisionAsSubtractionSeries()
            input("Press Enter to return to the menu")
        elif choice.lower() == "q":
            quit()
        elif choice.lower() == "i":
            cls()
            # Just a basic information screen
            # Uses the textwrap module to make sure everything remains legible
            info_str = "This program was written as a solution for Week 2 of the University of the Arts London's BSc in creative computing by Kourosh Simpkins."
            print(tr.fill(info_str, width=50))
            print("")
            print("Option 1: ", tr.fill(Option1, width=50))
            print("")
            print("Option 2: ", tr.fill(Option2, width=50))
            print("")
            print("Option 3: ", tr.fill(Option3, width=50))
            print("")
            input("Press Enter to return to the menu")
        else:
            print("Not a valid choice")


if __name__ == '__main__':
    main()
