"""
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
import collections


def evalRPN(tokens: list[str]) -> int:
    rpn = collections.deque()
    for i in range(len(tokens)):
        match tokens[i]:
            case '+':
                second, first = rpn.pop(), rpn.pop()
                rpn.append(first + second)
            case '-':
                second, first = rpn.pop(), rpn.pop()
                rpn.append(first - second)
            case '*':
                second, first = rpn.pop(), rpn.pop()
                rpn.append(first * second)
            case '/':
                second, first = rpn.pop(), rpn.pop()
                rpn.append(int(first / second))
            case _:
                rpn.append(int(tokens[i]))
    return rpn.pop()


"""
Intuition
We are given a list of Reverse Polish Notation (RPN) tokens and the task is to evaluate this RPN expression. RPN, 
also known as postfix notation, is a mathematical notation in which every operator follows all of its operands. It 
is a stack-based evaluation.

Approach
1. Create an empty stack (`rpn`).
2. Iterate over each token in `tokens`:
   - If the token is an operand (numbers), push it to the stack.
   - If the token is an operator, pop the required number of operands from the stack (2 in this case for binary 
     operators), perform the operation, and push the result back to the stack.
3. By the end of the iteration, the stack will have a single element which is the result of the RPN expression.

Implementation Notes
- Using `collections.deque()` as a stack provides fast appends and pops from both ends.
- The Python `match` case is being utilized (similar to a switch case in other languages). The `_` is a wildcard that 
  matches everything, so it's used to match all numbers.
- Division is a special case. Since division between two integers in Python might produce a float, we use `int` to 
  convert it to an integer. The problem specifies "truncate towards zero", which means Python's default behavior of 
  integer division (using the int typecast) is appropriate.

Time Complexity: O(n)
The program goes through each of the n tokens once.

Space Complexity: O(n)
In the worst case, all tokens are numbers, so the stack (`rpn`) will contain all n numbers.
"""