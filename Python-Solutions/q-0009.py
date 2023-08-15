"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is a
palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""


def isPalindrome(x: int) -> bool:
    input_string = str(x)
    i = 0
    j = len(input_string) - 1

    while i <= j:
        if input_string[i] != input_string[j]:
            return False
        i += 1
        j -= 1

    return True


"""
Intuition
To determine if an integer is a palindrome, one approach is to convert the number into a string and then check if the 
string reads the same backward as forward.

Approach
1. Convert the integer `x` to a string and store it in the variable `input_string`.
2. Initialize two pointers, `i` and `j`, to the start and end of the `input_string`, respectively.
3. Loop while `i` is less than or equal to `j`:
   - If the characters at positions `i` and `j` of `input_string` are different, return `False` as this means the number
     is not a palindrome.
   - Increment `i` and decrement `j` to continue checking the next set of characters.
4. If the loop completes without returning `False`, then the number is a palindrome, so return `True`.

Time complexity: O(n)
Where `n` is the number of digits in `x`. In the worst case, we need to check half of the digits of the number (i.e., 
until `i` meets or passes `j`).

Space complexity: O(n)
The space used is proportional to the number of digits in `x` because we are converting the integer to a string. If we 
don't consider the space used for the input representation, the space complexity can be seen as O(1) since we only use 
a constant amount of extra space (for the pointers and a few other variables).

"""
