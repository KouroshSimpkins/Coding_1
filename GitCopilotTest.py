def getCharsInText(text):
    """Given a string of text, print the number of times each letter
    in the alphabets a-z appear."""
    chars = {}
    for char in text:
        if char.isalpha():
            if char.lower() in chars:
                chars[char.lower()] += 1
            else:
                chars[char.lower()] = 1
    return chars

print(getCharsInText("Hello, world!"))

def caesarShift(text, shift):
    """Given a string of text, and a shift amount of an integer, perform a ceasar shift"""
    shifted = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                shifted += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                shifted += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            shifted += char
    return shifted

print(caesarShift("Hello, world!", 3))


def NATOAlpha(text):
    """Given a string of text, print the NATO alphabet equivalent."""
    NATO = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-ray",
        "Y": "Yankee",
        "Z": "Zulu"
    }
    NATOString = ""
    for char in text:
        if char.isalpha():
            NATOString += NATO[char.upper()] + " "
        else:
            NATOString += char
    return NATOString

