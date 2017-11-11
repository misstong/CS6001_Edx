def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for c in secretWord:
        if c not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    ret=[]
    for c in secretWord:
        if c not in lettersGuessed:
            ret.append("_ ")
        else:
            ret.append(c)
    return "".join(ret)

import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s=string.ascii_lowercase
    l=list(s)
    for c in lettersGuessed:
        l.remove(c)
    return "".join(l)
        
    
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print isWordGuessed(secretWord, lettersGuessed)
print getGuessedWord(secretWord, lettersGuessed)
print getAvailableLetters(lettersGuessed)
