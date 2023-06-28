"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""


def isPalindrome(s: str) -> bool:
    # Convert to lowercase, alphanumerical string
    s = s.lower()
    s = ''.join(filter(str.isalnum, s))

    # Initialize Two Pointers
    i = 0
    j = len(s) - 1

    # Iterate towards the middle from both sides of the string
    while i < len(s) and j >= 0 and i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


if __name__ == '__main__':
    example = "1 Haannaah 1"
    print(isPalindrome(example))

"""
Intuition
The property of a palindrome is that it reads the same from both ends towards the middle. This can be leveraged by using two pointers, one starting from the beginning of the string and one from the end. If we can meet in the middle without finding any mismatched characters, we can conclude the string is a palindrome.

Approach
First, we convert the entire string to lowercase and filter out non-alphanumeric characters. We then initialize two pointers, one at the start of the string and one at the end. We increment the first pointer and decrement the second pointer, comparing the characters at these two positions in each step. If the characters are not the same at any point, we return False, indicating that the string is not a palindrome. If we've iterated over all characters and found no mismatches, we return True, indicating the string is a palindrome.

Time complexity:O(n)
We process each character in the string exactly once, where n is the length of the string, resulting in a linear time complexity.

Space complexity:O(n)
We replace the string s with a string that contains only the alphanumeric characters from the original string, in the worst case, it could be as long as the original string. Thus, the space complexity is linear.
"""
