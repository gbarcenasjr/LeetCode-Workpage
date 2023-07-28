"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/description/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

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
    def inorderTraversal(root: Optional[TreeNode]) -> list[int]:
        traversal = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            traversal.append(node.val)
            dfs(node.right)

        dfs(root)
        return traversal

if __name__ == '__main__':
    example1 = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
    print(Solution.inorderTraversal(example1))

"""
Intuition
In a binary tree, in-order traversal visits the left subtree first, then the root node, and finally the right subtree. The intuition here is to use a recursive helper function that traverses the tree in this order.

Approach
The 'inorderTraversal' function first initializes an empty list 'traversal'. Then it defines a helper function 'dfs' (depth-first search), which takes a node as an argument. If the node is not None, it recursively calls 'dfs' on the left child, adds the value of the node to the 'traversal' list, and then recursively calls 'dfs' on the right child.
The 'dfs' function is initially called with the root node. Finally, 'inorderTraversal' returns the 'traversal' list, which contains the values of the nodes in in-order.

Time complexity: O(n)
Since every node in the binary tree is visited once, the time complexity is linear in the number of nodes, denoted as O(n).

Space complexity: O(n)
In the worst case, the maximum depth of the recursive call stack is n (for a skewed tree), hence the space complexity is O(n). Additionally, we are storing the values of the nodes in the 'traversal' list, which can also hold up to n values, so the overall space complexity remains O(n).
"""