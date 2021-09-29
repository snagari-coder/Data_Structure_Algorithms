# Leetcode 543

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        treeDiameter = [0]
        self.dfs(root,treeDiameter)
        return treeDiameter[0]
        
        
    def dfs(self,node,treeDiameter):
        myHeight = 0
        myDiameter = 0
        if node.left is None and node.right is None:
            return 0
        
        if node.left is not None:
            leftsubtreeHeight = self.dfs(node.left,treeDiameter)
            myHeight = leftsubtreeHeight + 1
            myDiameter += leftsubtreeHeight + 1
        if node.right is not None:
            rightsubtreeHeight = self.dfs(node.right,treeDiameter)
            myHeight = max(myHeight, rightsubtreeHeight+1)
            myDiameter += rightsubtreeHeight + 1
            
        treeDiameter[0] = max(treeDiameter[0],myDiameter)
        return myHeight
      
      # Time complexity = O(n) = Space complexity
