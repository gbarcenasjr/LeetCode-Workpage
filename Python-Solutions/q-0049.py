"""
Group Anagrams
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""


def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    value_list = []
    for word in strs:
        ascii_count = 0
        for letter in word:
            ascii_count += ord(letter)
        value_list.append(ascii_count)
    # print(value_list)

    list_of_lists = []
    for current_value in value_list:
        new_list = []
        for index, referencing_value in enumerate(value_list):
            if referencing_value == current_value:
                new_list.append(strs[index])
        if new_list not in list_of_lists:
            list_of_lists.append(new_list)
    return list_of_lists
