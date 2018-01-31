#!/usr/bin/python

# ==== returns true if the character passed is one of the 26*2 ASCI english letters. Otherwise false.
def isLetter (char):
    letters = "abcdefghijklmnopqrstuvwxyz";
    Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if char in letters:
        return True;
    if char in Letters:
        return True;
    return False;

# ==== returns a string array of
def wordsOfString(stringToParse):
    wrdArry = [];
    lastBorder = 0;
    stringToParse += " ";
    for ct in range(1, len(stringToParse)):
        if isLetter(stringToParse[ct]) and not isLetter(stringToParse[ct-1]):
            lastBorder = ct;
        if ct < len(stringToParse):
            if isLetter(stringToParse[ct]) and not isLetter(stringToParse[ct+1]):
                wrdArry.append(stringToParse[lastBorder:ct+1]);
    return wrdArry;
