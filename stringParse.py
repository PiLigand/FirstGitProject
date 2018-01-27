#!/usr/bin/python

START = 1;
END = 2;

# ==== returns true if the character passed is one of the 26*2 ASCI english letters. Otherwise false.
def isLetter (char):
    letters = "abcdefghijklmnopqrstuvwxyz";
    Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if char in letters:
        return True;
    if char in Letters:
        return True;
    return False;

# === returns a string array of
def wordsOfString(stringToParse):
    wrdArry = [];
    lastBorder = 0;
    for ct in range(0, len(stringToParse)):
        if isLetter(stringToParse[ct]) and not isLetter(stringToParse[ct+1]):
            wrdArry.append(stringToParse[lastBorder:ct+1]);
            lastBorder = ct+1;
    return wrdArry;



# ================Main Program
testString = "This is my big,: old a !test string."

myArray = wordsOfString(testString);
for wrd in myArray:
    print wrd;
