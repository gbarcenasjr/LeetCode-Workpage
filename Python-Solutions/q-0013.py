"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/description/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is
simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is
not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction
is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


def romanToInt(s: str) -> int:
    value = 0
    ROMAN_VALUE = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    value += ROMAN_VALUE[s[0]]
    if len(s) == 1:
        return value
    for index in range(1, len(s)):
        value += ROMAN_VALUE[s[index]]
        if ROMAN_VALUE[s[index - 1]] < ROMAN_VALUE[s[index]]:
            value -= ROMAN_VALUE[s[index - 1]] * 2
    return value


if __name__ == '__main__':
    example3 = "MCMXCIV"
    print(romanToInt(example3))

"""
Intuition
Roman numerals use a specific combination of letters to represent numbers. The primary principle is to add or subtract 
based on the letters' order. If a smaller numeral appears before a larger numeral, you subtract the smaller numeral. 
If it appears after, you add. Given this principle, the algorithm checks each numeral and adds its corresponding value 
to a total sum. Additionally, when a smaller numeral is encountered before a larger one, the algorithm subtracts twice 
the value of the smaller numeral (since we've added it once before).

Approach
1. Initialize `value` to 0. This variable will store the integer representation of the given Roman numeral string `s`.
2. Create a dictionary `ROMAN_VALUE` which maps each Roman numeral to its corresponding integer value.
3. Add the value of the first character of the string `s` to `value`.
4. If `s` has only one character, return`value`.
5. Loop through the string `s` from the second character if `s` is greater than 1:
    -  For each character, add its corresponding value from `ROMAN_VALUE` to value.
    - Check if the previous character's value is less than the current character's value. If so, subtract twice the 
      previous character's value from value. This is done to correct for the earlier addition of the smaller numeral.
6. After processing all characters in the string `s`, return `value`.

Complexity
Time complexity: O(n)
The algorithm loops through the string s once, where "n" is the length of s. Therefore, the time complexity is linear.

Space complexity: O(1)
The space used by the algorithm does not increase with the size of the input string s. The ROMAN_VALUE dictionary uses 
constant space, regardless of the input size. Thus, the space complexity is constant.
"""