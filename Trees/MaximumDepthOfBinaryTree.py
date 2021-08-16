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

###########################################################################################################################################################################
############# MINIMUM DEPTH OF A TREE ########################


# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root and (root.left is None and root.right is None):
            return 1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0:
            return right + 1
        elif right == 0:
            return left + 1
        else:
            return min(left,right) + 1
