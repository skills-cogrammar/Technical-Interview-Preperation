def isPalindrome(word: str):
    reversed_word = list(word)
    reversed_word.reverse()    

    return "".join(reversed_word) == word

def getAllPalindromes(words: list[str]):
    output = []
    for word in words:
        if (isPalindrome(word)):
            output.append(word)

    return output

def getPalsFunctionally(words: list[str]):
    return my_filter(words, lambda word: word[::-1] == word)

def my_filter(lst: list, callback):
    output = []

    for item in lst:        
        if (callback(item)):
            output.append(item)

    return output

print(getPalsFunctionally(["aa", "aba", "abc", "abd"]))