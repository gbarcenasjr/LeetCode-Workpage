"""
145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/description/

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(root: Optional[TreeNode]) -> list[int]:
        traversal = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            traversal.append(node.val)

        dfs(root)
        return traversal

if __name__ == '__main__':
    example1 = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))

    print(Solution.postorderTraversal(example1))

"""
Intuition
In a binary tree, post-order traversal visits the left subtree first, then the right subtree, and finally the root node. The intuition here is to use a recursive helper function that traverses the tree in this order.

Approach
The 'postorderTraversal' function first initializes an empty list 'traversal'. Then it defines a helper function 'dfs' (depth-first search), which takes a node as an argument. If the node is not None, it recursively calls 'dfs' on the left child, then the right child, and then adds the value of the node to the 'traversal' list.
The 'dfs' function is initially called with the root node. Finally, 'postorderTraversal' returns the 'traversal' list, which contains the values of the nodes in post-order.

Time complexity: O(n)
Since every node in the binary tree is visited once, the time complexity is linear in the number of nodes, denoted as O(n).

Space complexity: O(n)
In the worst case, the maximum depth of the recursive call stack is n (for a skewed tree), hence the space complexity is O(n). Additionally, we are storing the values of the nodes in the 'traversal' list, which can also hold up to n values, so the overall space complexity remains O(n).
"""
