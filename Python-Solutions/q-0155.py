"""
155. Min Stack
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimumStack) == 0 or val < self.minimumStack[-1]:
            self.minimumStack.append(val)
        else:
            self.minimumStack.append(self.minimumStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minimumStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumStack[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())

"""
Intuition
Stacks are a useful data structure that operate based on the Last-In-First-Out (LIFO) principle. However, a common task can be to find the minimum value in a stack, which can be time-consuming if we need to search through it every time. An efficient solution is to track the minimum value as we push and pop elements.

Approach
We maintain two stacks: 'stack' for storing all elements, and 'minimumStack' for tracking the current minimum value. When pushing a value onto the 'stack', we compare it to the current minimum value on top of 'minimumStack'. If it's less, we push it onto 'minimumStack'. If it's more, we push the current minimum value again onto 'minimumStack'. When popping, we pop from both stacks to keep them in sync. The 'top' operation retrieves the top of 'stack', and 'getMin' retrieves the top of 'minimumStack', which is always the current minimum value in 'stack'.

Time complexity:O(1) for all operations
All operations (push, pop, top, getMin) are constant time as they involve only a couple of steps. These operations do not depend on the size of the stack.

Space complexity:O(n)
We use O(n) space, where n is the number of elements in the stack. Each element gets stored once in 'stack' and once in 'minimumStack', so we use 2n spaces. However, since we ignore constants in Big O notation, we say the space complexity is O(n).
"""
