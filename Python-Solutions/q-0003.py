"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
import collections


def lengthOfLongestSubstring(s: str) -> int:
    letter_history = collections.defaultdict(int)
    longest_count = 0
    longest_sub = ""

    for letter in s:
        longest_sub += letter
        letter_history[letter] += 1

        if letter_history[letter] > 1:
            if longest_count < len(longest_sub) - 1:
                longest_count = len(longest_sub) - 1
            longest_sub = longest_sub[longest_sub.index(letter) + 1:]
            letter_history.clear()
            for letter in longest_sub:
                letter_history[letter] += 1

        if longest_count < len(longest_sub):
            longest_count = len(longest_sub)

    return longest_count

if __name__ == '__main__':
    example_3 = "pwwkew"
    print(lengthOfLongestSubstring(example_3))

"""
Intuition
To find the longest substring without repeating characters, we can use the "sliding window" approach. We expand the window by adding characters to the substring until we encounter a duplicate character. When a duplicate character is encountered, we slide the window by removing characters from the beginning of the substring.

Approach
We keep a record of characters encountered in 'letter_history', a dictionary with characters as keys and their counts as values. We also maintain a variable 'longest_count' to store the length of the longest substring seen so far and 'longest_sub' to keep track of the current substring.
For each character in the string, we append it to 'longest_sub' and increment its count in 'letter_history'. If we encounter a duplicate character (i.e., the count in 'letter_history' exceeds 1), we check if the length of 'longest_sub' minus 1 (excluding the duplicate character) is greater than 'longest_count'. If so, we update 'longest_count'.
Then, we slide the window by removing characters from the beginning of 'longest_sub' up to and including the first occurrence of the current character, and reset 'letter_history'. We then repopulate 'letter_history' based on the new 'longest_sub'.
If 'longest_count' is less than the length of 'longest_sub', we update 'longest_count'. Finally, we return 'longest_count', the length of the longest substring without repeating characters.

Time complexity: O(n)
We iterate over the string once, where n is the length of the string. Although in the worst case we might have to repopulate 'letter_history' for every character, the overall time complexity is still linear.

Space complexity: O(min(m, n))
The size of 'letter_history' and 'longest_sub' can grow up to the size of the alphabet 'm' used in the string. In the worst case scenario, this would be the size of the ASCII character set. The time complexity is therefore O(min(m, n)), where n is the length of the string.
"""