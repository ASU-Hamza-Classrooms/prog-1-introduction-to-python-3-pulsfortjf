#!/bin/python3

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
#
def reverseStr(inputStr):
    """Reverse an input string"""
    rev = ""
    i = ''
    #iter_str = iter(str)
    for i in inputStr:
        rev = i + rev
    return rev

#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
#
def containsWord(containingStr, containedStr):
    """Check if containedStr is anywhere in containingStr"""
    if containedStr in containingStr:
        return "Yes"
    else:
        return "No"

#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
#
def isPalindrome(inputStr):
    """Check if input string is a palindrome"""
    if str == reverseStr(inputStr):
        return "Yes"
    else:
        return "No"

#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
#
def upperCaseStr(inputStr):
    """Returns uppercase version of the input string"""
    bigStr = ""
    for i in inputStr:
        charNum = ord(i)
        if charNum >= 97 & charNum <= 122:
            charNum = charNum - 32
        bigStr = bigStr + chr(charNum)
    return bigStr

