"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""


def generateParenthesis(n: int) -> list[str]:
    paranthesis_combinations = []

    def nextValid(combo: str, opening: int, closing: int):
        if (closing > opening) or opening > n:
            return
        if opening == n and closing == n:
            paranthesis_combinations.append(combo)
            return
        nextValid(combo + "(", opening + 1, closing)
        nextValid(combo + ")", opening, closing + 1)

    nextValid("", 0, 0)

    return paranthesis_combinations

if __name__ == '__main__':
    example_1 = 3
    print(generateParenthesis(3))

"""
Intuition:
I noticed that a program can choose to either enter an opening or closing parenthesis. Only having two choices, I
treated the solution like a binary tree where a valid sequence (whether complete or not) can split between having an
opening parenthesis or a closing parenthesis inserted until there is 'n' amount of both types of parentheses.

Approach:
The 'generateParenthesis' function will initialize a list called 'parenthesis_combinations' where it will store all
valid and complete parentheses combinations. The start of a valid parenthesis starts with an opening one so to have a
closing one before an opening would invalidate the combination. So, the 'nextValid' function will check if there are
more closing parenthesis than openings, or if there are too many opening parentheses, and will return and do nothing.
However, if the function finds an equal amount of opening and closing parentheses after the validation, it will be
appended to the combinations list. Similar to a binary tree, the function is called within itself but to test if adding
an opening parenthesis or a closing parenthesis to the current string would be valid.

Time complexity: O(4^n / sqrt(n))
The time complexity for generating all well-formed parentheses is exponential, given by Catalan number [4^n / sqrt(n)].

Space complexity: O(n)
The maximum depth of the recursive call stack would be equal to the length of the longest possible string, i.e., 2n. As 
such, the space complexity is linear. Also, the space required to store all combinations will depend on the number of 
valid combinations, which in worst-case is exponential. However, in this context, it's often considered part of the 
problem's output size and is therefore not counted in the space complexity analysis.

"""
