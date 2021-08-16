# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left) # At every node, we check left and right height and return to parent node.
        right = self.maxDepth(root.right) # Recursively the height is calculated
        if left > right:
            height = 1 + left
        else:
            height = 1 + right

        return height
# Time complexity = O(n), n is number of nodes
# Space complexity = O(1), without considering the stack space for recursive action
