# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    ### TODO.
    if aStr=="" or len(aStr)==1:
        return aStr
    return aStr[-1]+reverseString(aStr[1:-1])+aStr[0]
print reverseString("")==""
print reverseString("a")=="a"
print reverseString("adb")=="bda"
print reverseString("ad")=="da"
#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    ###TODO.
    if x=="" :
        return True
    if len(x)==1:
        return word.find(x)!=-1
    if len(x)==2:
        return word.find(x[0])!=-1 and word.find(x[1])!=-1 and word.find(x[0])<word.find(x[1]) 
    mid=len(x)/2
    return x_ian(x[0:mid], word) and x_ian(x[mid:], word) and x_ian(x[mid-1:mid+1], word)

                 


print x_ian('eric', 'meritocracy')==True
print x_ian('eric', 'cerium')==False
print x_ian('john', 'mahjong')==False
#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    ### TODO.
