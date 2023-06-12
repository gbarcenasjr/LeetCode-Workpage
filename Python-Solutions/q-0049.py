"""
Group Anagrams
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    collection = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in collection:
            collection[sorted_word] = [word]
        else:
            collection[sorted_word].append(word)
    return list(collection.values())


if __name__ == '__main__':
    bunch_of_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(bunch_of_words))

"""Intuition
My first approach was to reduce each character of each word in the list "strs" into ASCII values using the ord() method. Using the values, I would add them all together and compare if other words had equal sum values. However, it was a naive approach as some words of the same length can be wrongly matched with another different word. I then though of if the word characters were sorted, I could make a list of all words with the matching sorted character.

Approach
In this function, we loop through each word in our list, and for each word, we rearrange its letters in order. We use this sorted version of the word as a key to store our original word in a dictionary. If we encounter another word that sorts to the same key, we know it's an anagram of the first, so we add it to the same group in our dictionary.
At the end, we return all the groups of anagrams that we've found, which are the values in our dictionary.

Complexity
Time complexity:O(mn logm)
The time complexity of the groupAnagrams function is O(NM log M), where N is the number of words and M is the maximum length of a word in the list. This is because for each word in the list (N words), we perform a sort operation (which takes M log M time) on the letters of the word.

Space complexity:O(mn)
The space complexity of the groupAnagrams function is O(NM), where N is the number of words and M is the maximum length of a word in the list. This is because we're storing all the words in a dictionary and the total space used is proportional to the total length of the words, which is equivalent to the number of words times the maximum length of a word."""
