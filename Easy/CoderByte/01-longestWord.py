# Using the Python language, have the function LongestWord(sen) take the sen parameter being passed
# and return the largest word in the string. If there are two or more words that are the same length,
# return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.


def longestWord(sentence):
    words = sentence.split(" ")
    thelongestword = ""
    for word in words:
        if len(word) > len(thelongestword):
            thelongestword = word
    return thelongestword

print(longestWord("Hello World Singapore"))