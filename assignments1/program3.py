# Given two strings s and t, print "true" if t is an anagram of s, and "false" otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

str1 = input()
str2 = input()

if set(str1) == set(str2):
    print("true")
else:
    print("false")