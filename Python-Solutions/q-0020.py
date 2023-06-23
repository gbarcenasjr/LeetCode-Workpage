"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true
Example 2:

Example 2:
Input: s = "()[]{}"
Output: true
Example 3:

Example 3:
Input: s = "(]"
Output: false
"""

def isValid(s: str) -> bool:
        stack = []
        for charater in s:
            if charater == "(" or charater == "[" or charater == "{":
                stack.append(charater)
            else:
                if len(stack) == 0:
                    return False

                match charater:
                    case ")":
                        if stack[-1] == "(":
                            stack.pop()
                            continue
                    case "]":
                        if stack[-1] == "[":
                            stack.pop()
                            continue
                    case "}":
                        if stack[-1] == "{":
                            stack.pop()
                            continue

                stack.append(charater)

        if len(stack) == 0:
            return True
        return False

if __name__ == '__main__':
    example_3= "(]"
    print(isValid(example_3))

"""
Intuition:
The problem requires a mechanism to keep track of the last unmatched opening bracket with a time complexity of O(n). A stack data structure, which follows the Last-In-First-Out (LIFO) principle, seems an ideal fit for this task.

Approach:
We initialize an empty stack. As we iterate over each character in the string, if we encounter an opening bracket, we push it onto the stack. If we encounter a closing bracket, we check if the stack is empty (which means there's no corresponding opening bracket for this closing bracket). If it is empty, we return False. If the stack is not empty, we compare the top of the stack with the current closing bracket. If they form a pair, we pop the opening bracket from the stack and continue to the next character. If they don't form a pair, it means the string is not valid, so we append the closing bracket to the stack. After iterating through all characters, if there are no more elements left in the stack, we return True (valid string), otherwise, we return False (invalid string).

Time complexity: O(n)
Since we're processing each character in the string exactly once, the time complexity is linear, or O(n), where n is the length of the string.

Space complexity:O(n)
In the worst-case scenario, all characters in the string are opening brackets, so we would push all of them onto the stack. Therefore, the space complexity is also O(n).
"""