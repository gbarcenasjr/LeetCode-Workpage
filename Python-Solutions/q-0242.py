"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
"""


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    word1, word2 = {}, {}

    for char in s:
        if char not in word1:
            word1[char] = 1
        else:
            word1[char] += 1
    for char in t:
        if char not in word2:
            word2[char] = 1
        else:
            word2[char] += 1

    if word1 != word2:
        return False
    return True

if __name__ == '__main__':
    input1 = "anagram"
    input2 = "nagaram"

    print(isAnagram(input1,input2))


"""
Intuition
My first thought was to see if I can count each letter in the "s" string and "t" string. I would compare the letters and how many instances of each letter and compare if both are the same.

Approach
I first check to make sure that the length of the words are the same. If not, return False. I create two dictionaries "word1" and "word2". The keys are the characters and the values are the number of instances of that character. Using two for loops, the algorithm iterates through both strings, creating a diagram of characters and how many of each. If both dictionaries match, then the function will return true.

Time complexity: O(n)
Since there are two for loops iterating two identically long strings in the worst case scenario, it would create two linear complexities resulting in O(n + n) or can be simplified to O(n).

Space complexity: O(n)
The two dictionaries increases equally to the amount of characters in the string, the space complexity of this function would be O(n + n) or can be simplfied to O(n)
"""
