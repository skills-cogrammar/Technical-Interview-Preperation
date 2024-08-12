"""
Given a list of strings, return a list of strings that are palindromes.
A palindrome is a word or phrase that is the same forwards and backwards.
For example, “radar” is a palindrome, but “fish” is not.

Example 1:
Input: ["abc", "cba", "abab"]
Output: ["abc", "abab"]

Example 2:
Input: ["a", "b", "ab"]
Output: ["ab"]

Example 3:
Input: ["abc", "cba", "abab", "baba"]
Output: ["baba", "abab"]

Constraints:
1 <= list.length <= 100
1 <= list[i].length <= 100
list[i] consists of lowercase English letters.a
"""

from time import time
from generatePalindrome import getWordList

def isPalindromeReverse(word: str):
    reversed_word = list(word)
    reversed_word.reverse()    


    return "".join(reversed_word) == word

def isPalindromeReverseLoop(word: str):
    charList = list(word)
    reversed_word = []

    for char in charList[::-1]:
        reversed_word.append(char)

    return "".join(reversed_word) == word

def isPalindomeWindow(word: str):
    left = 0
    right = len(word) - 1

    output = False

    while (True):
        if left >= right:
            output = True
            break

        if word[left] != word[right]:
            output = False
            break

        left += 1
        right -= 1

    return output

def getAllPalindromes(words: list[str], isPalindome):
    output = []
    for word in words:
        if (isPalindome(word)):
            output.append(word)

    return output

def runTest(func, name):
    words_list = getWordList()
    start = time()
    
    for i in range(10000):
        getAllPalindromes(words_list, func)
    end = time()

    print(name, end - start)

runTest(isPalindromeReverse, "Using reverse")
runTest(isPalindomeWindow, "Using window")
runTest(isPalindromeReverseLoop, "Loop to Reverse")