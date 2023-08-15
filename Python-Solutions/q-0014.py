"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


def longestCommonPrefix(strs: list[str]) -> str:
    shortest_string_len = min(len(ele) for ele in strs)
    if shortest_string_len == 0:
        return ""
    common_prefix = ""
    for x in range(shortest_string_len):
        current_letter = strs[0][x]
        for word in strs:
            if word[x] != current_letter:
                return common_prefix
        common_prefix += current_letter
    return common_prefix

if __name__ == '__main__':
    example1 = ["flower","flow","flight"]
    print(longestCommonPrefix(example1))

"""
Intuition:
When determining the longest common prefix among a list of strings, the common prefix can't be longer than the shortest 
string in the list. Thus, finding the length of the shortest string can provide an upper bound for the prefix's length.

Approach:
1. Determine the length of the shortest string in the list `strs` using a list comprehension and the `min` function, 
   and store this length in `shortest_string_len`.
2. If `shortest_string_len` is 0 (meaning there's an empty string in the list), return an empty string as the common 
   prefix.
3. Initialize an empty string `common_prefix` to store the common prefix characters.
4. Loop through each character position `x` in the range of `shortest_string_len`:
   - Get the character at position `x` of the first string in the list (`strs[0][x]`) and store it in `current_letter`.
   - Loop through each `word` in `strs`:
     - If the character at position `x` of `word` is different from `current_letter`, return the current `common_prefix`
       as no further common prefix can exist beyond this point.
   - If all words have the same character at position `x`, append `current_letter` to `common_prefix`.
5. Once the loop is finished, return the `common_prefix`.

Time complexity: O(n*m)
Where `n` is the number of strings in `strs` and `m` is the length of the shortest string. In the worst case, we would 
check each character of the shortest string against every other string.

Space complexity: O(1)
The space used by the algorithm is constant and doesn't increase with the size of the input list `strs` as the 
`common_prefix` can be at most as long as the shortest string in the list.

"""
