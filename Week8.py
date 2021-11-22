"""Implementation of a rudimentary spell checker, using the python levenshtein module.
Given a text file as a command line argument, read the text file and do spell checks
on individual words in the file. A list of English words are provided as another
command line argument.
output the corrected spell checked file to another location specified by another
command line argument.
Print to the console any relevant information you deem necessary (i.e. optional)

Example command: python3 Week8.py -i cyberspace.txt -o cyberspace_corrected.txt -d dictionary.txt

© 2021 Kourosh Simpkins
"""

import Levenshtein
import argparse
import sys


def getArgs():
    """Get the command line arguments."""
    parser = argparse.ArgumentParser(description="Spell checker")
    parser.add_argument("-i", "--input", help="input file", required=True)
    parser.add_argument("-o", "--output", help="output file", required=True)
    parser.add_argument("-d", "--dictionary", help="dictionary file", required=True)
    return parser.parse_args()


def getWords(file):
    """Read the input file and return a list of words."""
    words = []
    with open(file, "r") as f:
        for line in f:
            words += line.split()
    return words


def getDictionary(file):
    """Read the dictionary file and return a list of words."""
    words = []
    with open(file, "r") as f:
        for line in f:
            words += line.split()
    return words


def getCorrectedWords(words, dictionary):
    """Given a list of words and a list of dictionary words, return a list of corrected words."""
    correctedWords = []
    for word in words:
        correctedWords.append(getCorrectedWord(word, dictionary))
    return correctedWords


def getCorrectedWord(word, dictionary):
    """Given a word and a list of dictionary words, return the corrected word."""
    minDistance = sys.maxsize
    minWord = ""
    for dictionaryWord in dictionary:
        distance = Levenshtein.distance(word, dictionaryWord)
        if distance < minDistance:
            minDistance = distance
            minWord = dictionaryWord
    return minWord


def writeCorrectedWords(words, file):
    """Write the corrected words to the output file."""
    with open(file, "w") as f:
        for word in words:
            f.write(word + " ")


def main():
    """Main function."""
    args = getArgs()
    words = getWords(args.input)
    dictionary = getDictionary(args.dictionary)
    correctedWords = getCorrectedWords(words, dictionary)
    writeCorrectedWords(correctedWords, args.output)


if __name__ == "__main__":
    main()