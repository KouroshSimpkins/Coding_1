"""Week 5 of coding 1, part of creative computing year 1 at the Creative Computing institute"""


def NATOAlpha():
    """Convert an input from chars to the related NATO phonetic word.
    returns the output as a string, takes no inputs within code."""

    alphabet = {"a":"alfa","b":"bravo","c":"charlie","d":"delta","e":"echo","f":"foxtrot","g":"golf","h":"hotel","i":"india","j":"juliett","k":"kilo","l":"lima","m":"mike","n":"november","o":"oscar","p":"papa","q":"quebec","r":"romeo","s":"sierra","t":"tango","u":"uniform","v":"victor","w":"whiskey","x":"xray","y":"yankee","z":"zulu"} #pylint: disable=line-too-long

    value = input("> ")
    output = ""

    for i in range(len(value)): #pylint: disable=consider-using-enumerate
        if value[i] in alphabet:
            output += alphabet[value[i]] + " "

    return output


def caesarShift(text,s):
    """implement a caesar shift, taking 2 inputs, a shift amount and a string.
    returns the output as a string. Takes no arguments."""
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result
#check the above function
text = "CEASER CIPHER DEMO"
s = 4

#print("Plain Text : " + text)
#print("Shift pattern : " + str(s))
#print("Cipher: " + caesarShift(text, s))

print(NATOAlpha())