# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    #print(wordlist)
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    l = 0
    for c in secretWord:
        if c in lettersGuessed:
            l+=1   
    if l == len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    l = []
    underscores = []
    underscores =underscores+list((len(secretWord)*"_ ").strip())
    for ch in lettersGuessed:
        if ch in secretWord:
            l = [i for i, letter in enumerate(secretWord) if letter == ch]
            for i in l:
                underscores[2*int(i)] = ch
    word = ''
    for c in underscores:
        word += c
    return word
           
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    char_list = []
    char_list += list(string.ascii_lowercase)
    for c in lettersGuessed:
        if c in char_list:
            char_list.remove(c)
    char_str = ''
    for c in char_list:
        char_str += c
    return char_str

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    numOfGuesses = 8
    lettersGuessed = ''
    print("   Welcome to the game, Hangman!")
    print("   I am thinking of a word that is",len(secretWord),"letters long")
    while(numOfGuesses):
        print("   -------------")
        if isWordGuessed(secretWord, lettersGuessed) :
            print("   Congratulations, you won!")
            break
        print("   You have",numOfGuesses,"guesses left.")
        print("   Available letters:",getAvailableLetters(lettersGuessed))
        print("   Please guess a letter:",end=" ")
        letter = input()
        if letter not in lettersGuessed and letter in secretWord:
            lettersGuessed += letter
            print("   Good guess:",getGuessedWord(secretWord, lettersGuessed))
        elif letter in lettersGuessed and letter in secretWord:
            print("   Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
        
        elif letter in lettersGuessed and letter not in secretWord:
            print("   Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))

        elif letter not in secretWord and letter not in lettersGuessed:
            lettersGuessed += letter
            print("   Oops! That letter is not in my word:",getGuessedWord(secretWord, lettersGuessed))
            numOfGuesses -= 1
        
    if numOfGuesses == 0:
        print("   -------------")
        print("   Sorry, you ran out of guesses. The word was else.")
        print("   ",secretWord)

wordlist = loadWords()
secretWord = chooseWord(wordlist)
hangman(secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
