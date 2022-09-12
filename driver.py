#!/bin/python3

#import the code in string1.py

from stringlib import *
from worker import *
import sys

#Function to test the functions in the stringlib module
def testStringLib(inputStr):
    print("  Input string is " + inputStr)
    #Add code to call each of the functions and print the results
    rev = reverseStr(inputStr)
    print("  Reverse of string is " + rev)
    containsApple = containsWord(inputStr, "apple")
    print("  Does string contain apple? " + containsApple)
    containsBanana = containsWord(inputStr, "banana")
    print("  Does string contain banana? " + containsBanana)
    palindrome = isPalindrome(inputStr)
    print("  Is string a palindrome?" + palindrome)
    upperCase = upperCaseStr(inputStr)
    print("  Uppercase of string is " + upperCase)
    return

#Function to test the methods in the Worker class in the worker module
def testWorkerClass(inputStr):
    #Add code to create a Worker object
    #Use the object to call each of the methods in the Worker class
    #Print the result of each call

    worker = Worker(inputStr)
    
    print("  Input string is " + inputStr)

    rev = worker.reverseStr()
    print("  Reverse of string is " + rev)
    containsApple = worker.containsWord("apple")
    print("  Does string contain apple? " + containsApple)
    containsBanana = worker.containsWord("banana")
    print("  Does string contain banana? " + containsBanana)
    palindrome = worker.isPalindrome()
    print("  Is string a palindrome? " + palindrome)
    upper = worker.upperCaseStr()
    print("  Uppercase of string is " + upper)

    return

#check to make sure there is a string command line argument
if (len(sys.argv) < 2):
    print("usage: driver1.py <string>")
else:
    #call the functions that test the library and the Worker class
    print("\nTest stringlib:")
    testStringLib(sys.argv[1])
    print("\nTest Worker class:")
    testWorkerClass(sys.argv[1])




