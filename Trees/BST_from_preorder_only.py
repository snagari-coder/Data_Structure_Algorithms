# Leetcode 1008
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        idx = 0
        MIN_INTEGER = float('-infinity')
        MAX_INTEGER = float('infinity')
        
        def helper(preorder,mini,maxi):
            nonlocal idx
            
            if idx >= len(preorder):
                return None
            
            if preorder[idx] < mini or preorder[idx] > maxi:
                return None
            
            
            root = TreeNode(preorder[idx])
            idx += 1
            root.left = helper(preorder,mini,root.val)
            root.right = helper(preorder,root.val,maxi)
            return root
        
        return helper(preorder,MIN_INTEGER,MAX_INTEGER)
        
        # Time complexity = O(n), for n nodes doing constant job
        # space complexity = O(log n) - implicit for call stack
        #                   = O(n) - explicit for n nodes
