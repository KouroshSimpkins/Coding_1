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


def pygLatinWords():
    """Write a function that takes in any English word and turns it into pig latin.
    Extra if you can write another function that converts a whole sentence"""

    original = getInput()

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
