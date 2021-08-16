# Leetcode 124
# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = float('-inf')
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.findsum(root)
        return self.max_sum
        
    def findsum(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        left = max(self.findsum(root.left),0) # We are making bounding the negatuve number to 0. 10 + max(-5,0) = 10, instead of 10 + (-5) = 5
        right = max(self.findsum(root.right),0)
        self.max_sum = max(self.max_sum, left + right + root.val)
        return (max(left,right)+root.val)
            
