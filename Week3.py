"""Week3.py"""

import re
import Week2


def getInput():
    """Get the input from the user, as well as clearing the console before asking for an input."""
    Week2.cls()
    value = str(input("Please provide an Input: "))
    return value


def greeting():
    """Make a function that takes two arguments, the second of which is optional.
    Print a greeting that varies depending on how many arguments are provided."""

    name = getInput()

    if re.search(r'[\s]', name):
        tmp = name.split()
        output = "Hello there, " + tmp[0] + " of " + tmp[1]
    else:
        output = "hello, " + name

    return output


def pygLatinWords(original):
    """Write a function that takes in any English word and turns it into pig latin.
    Extra if you can write another function that converts a whole sentence"""

    vowels = ['a','e','i','o','u']

    first = original[0]

    if first in vowels:
        original = original.lower()
        original += "way"

    else:
        original = original.lower()

        for letter in original:
            if letter in vowels:
                index_value = original.index(letter)
                break

        original = original[index_value:] +original[:index_value]+ "ay"

    return original


def pygLatinSentence():
    """take input of sentence to be converted to pygLatin"""

    original = getInput()

    originalList = original.split()
    outputList = []

    for i, word in enumerate(originalList):     # pylint: disable=unused-variable
        # removing i causes this to break, even though we never use i. No idea why
        # Easier to just leave i here.
        outputList.append(pygLatinWords(word))

    return outputList


def main():
    """main function, if program is run from this file"""
    print(*pygLatinSentence())

if __name__ == '__main__':
    main()
