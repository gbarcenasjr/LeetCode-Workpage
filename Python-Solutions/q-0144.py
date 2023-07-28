"""
144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/description/

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

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
    def preorderTraversal(root: Optional[TreeNode]) -> list[int]:
        traversal = []

        def dfs(node):
            if not node:  # is None
                return
            traversal.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return traversal


if __name__ == '__main__':
    example1 = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))

    print(Solution.preorderTraversal(example1))

"""
Intuition
In a binary tree, pre-order traversal visits the root node first, then the left subtree, and finally the right subtree. So the intuition here is to use a recursive helper function that traverses the tree in this order.

Approach
The 'preorderTraversal' function first initializes an empty list 'traversal'. Then it defines a helper function 'dfs' (depth-first search), which takes a node as an argument. If the node is not None, it adds the value of the node to the 'traversal' list, then recursively calls 'dfs' on the left and right children of the node.
The 'dfs' function is initially called with the root node. Finally, 'preorderTraversal' returns the 'traversal' list, which contains the values of the nodes in pre-order.

Time complexity: O(n)
Since every node in the binary tree is visited once, the time complexity is linear in the number of nodes, denoted as O(n).

Space complexity: O(n)
In the worst case, the maximum depth of the recursive call stack is n (for a skewed tree), hence the space complexity is O(n). Additionally, we are storing the values of the nodes in the 'traversal' list, which can also hold up to n values, so the overall space complexity remains O(n).
"""