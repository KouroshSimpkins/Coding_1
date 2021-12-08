"""Hangman project created in class for week 10 Kourosh Simpkins"""

import random
import Week2
LIVES = 10
GUESSED_LETTERS = []

def wordPick():
    # Randomly pick a word from dictionary.txt
    with open("dictionary.txt", mode='r') as dictionary:
        words = [word for lines in dictionary for word in lines.split()]
        wordNum = random.randint(0, len(words))
        chosenWord = words[wordNum]

    return(chosenWord)


# Create a list of letters in the word
def wordList(word):
    wordList = []
    for letter in word:
        # If the value of letter is not actually a letter, do not add it to the list
        if letter.isalpha():
            letter = letter.lower()
            wordList.append(letter)
    return(wordList)


# Create a list of blanks for the word using wordList
def Blanks(word):
    blanks = []
    for letter in word:
        blanks.append("_")
    return(blanks)


# Ask the user for a letter input
def userInput(wordlist, blanks):
    global LIVES
    # Ask user for a letter
    letter = input("Please enter a letter: ")
    if guessedLetters(letter):
    # Check if the letter is in the word
        if letter in wordlist:
            # If the letter is in the word, replace the blank with the letter
            for i in range(len(wordlist)):
                if wordlist[i] == letter:
                    blanks[i] = letter
        else:
            # If the letter is not in the word, subtract a life
            LIVES -= 1
    else:
        pass
    return(blanks)


# Check if the user has won
def win(wordlist, blanks):
    if blanks == wordlist:
        return(True)
    else:
        return(False)


# Check if the user has lost
def lose(LIVES):
    if LIVES == 0:
        return(True)
    else:
        return(False)


# Run the game logic
def game(word):
    wordlist = wordList(word)
    blanks = Blanks(wordlist)
    while LIVES > 0 and win(wordlist, blanks) == False:
        Week2.cls()
        print(blanks)
        print("lives: ", LIVES)
        print("guessed letters: ", GUESSED_LETTERS)
        blanks = userInput(wordlist, blanks)
        print(blanks)
        input("Press Enter to return to continue...")
    if win(wordlist, blanks) == True:
        print("You win!")
    else:
        print("You lose!")
        print("The word was {}".format(word))


# letters that have already been guessed
def guessedLetters(letterGuessed):
    global GUESSED_LETTERS
    if letterGuessed in GUESSED_LETTERS:
        print("You already guessed that letter!")
        return(False)
    else:
        GUESSED_LETTERS.append(letterGuessed)
        print("You guessed {}".format(letterGuessed))
        return(True)


# Run the game
def main():
    word = wordPick()
    game(word)


if __name__ == "__main__":
    main()
