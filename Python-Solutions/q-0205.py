"""
Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/description/

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example:
Input: s = "egg", t = "add"
Output: true
"""


def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    replacements = {}
    bridge = ""

    for ind in range(len(s)):
        if s[ind] not in replacements.keys():
            if t[ind] not in replacements.values():
                replacements[s[ind]] = t[ind]
            else:
                return False
        bridge += replacements[s[ind]]

    if bridge == t:
        return True
    return False


if __name__ == '__main__':
    string1 = "egg"
    string2 = "add"
    output = isIsomorphic(string1, string2)
    print(output)

"""
Intuition
My first thoughts was to create a dictionary with unique characters as the key and it's replacement character as the value. Also if both strings didn't match the length, then it's an automatic False output.

Approach
I named my dictionary 'replacement' and created a temporary string named 'bridge'. I would use a for loop to iterate through each character of string 's'. If a letter wasn't already in the keys of the dicationary, then it would be added as the key and the character of the same index from string 't' would be the key value. Before adding the new dictionary item, the function will check if the character from 't' of the same index is already a key value. This will ensure no two keys will have the same value.
Once the character is either found in dictionary or has been added to the dictionary, the key value of the current letter of the for loop will be added to string 'bridge'. This will build a replica of string 't' if both strings are Isomorphoc and bridge the strings together.

Complexity
Time complexity: O(n)
The time complexity of this code is determined by the for loop iterating over the string 's'. Since the loop iterates once for every character in the string 's', the time complexity is O(n)O(n)O(n), where 'n' is the length of the string 's'.

Space complexity: O(n)
The space complexity of this code is determined by the size of the 'replacements' dictionary and the bridge string. In the worst case, the dictionary could store a mapping for every unique character in the input string 's'. Similarly, the 'bridge' string will have the same length as the input string 's'. Thus, the space complexity is also O(n)O(n)O(n), where 'n' is the length of the string 's'.
"""
