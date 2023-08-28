"""
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


def strStr(haystack: str, needle: str) -> int:
    for index in range(len(haystack) - len(needle) + 1):
        if haystack[index] == needle[0] and haystack[index:len(needle) + index] == needle:
            return index
    return -1

if __name__ == '__main__':
    example1_haystack = "sadbutsad"
    example1_needle = "sad"
    print(strStr(example1_haystack, example1_needle))
    example2_haystack = "leetcode"
    example2_needle = "leeto"
    print(strStr(example2_haystack, example2_needle))

"""
Intuition
The goal is to find the first occurrence of the string `needle` in `haystack` or return -1 if `needle` isn't found.
We can approach this by iterating over `haystack` and, for each position, checking if the substring of `haystack`
starting at that position matches `needle`.

Approach
1. Iterate over `haystack` using an index `index`. The iteration should only go up to `len(haystack) - len(needle) + 1`
   to avoid unnecessary checks since `needle` couldn't fit in the remaining positions anyway.
2. For each `index`, if the current character in `haystack` at position `index` matches the first character of `needle`
   and the substring from `index` to `index + len(needle)` is equal to `needle`, we found our match and can return 
   `index`.
3. If no match is found after iterating over `haystack`, we return -1.

Time Complexity: O(n*m)
Where `n` is the length of `haystack` and `m` is the length of `needle`. For each of the `n` positions in `haystack`, 
we might do a comparison with all `m` characters of `needle`.

Space Complexity: O(1)
The space used by the algorithm itself (excluding the input) is constant since we only use a few variables and 
perform in-place checks.
"""