# Leetcode 112
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        Flag = [False]
        
        def dfs(node,targetSum):
            if node.left is None and node.right is None:
                if targetSum == node.val:
                    Flag[0] = True
                    

            if node.left is not None:
                dfs(node.left,targetSum-node.val)

            if node.right is not None:
                dfs(node.right,targetSum-node.val)
                
        dfs(root,targetSum)
        return Flag[0]
      
      # Time complexity = O(n) = space complexity

    ################## ALTERNATE ##############################
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return None
        result = [False]
        self.top_down_dfs(root,targetSum,result)
        return result[0]
    
    def top_down_dfs(self,node,targetSum,result):
        targetSum -= node.val
        #Base case if leaf node
        if node.left is None and node.right is None:
            if targetSum == 0:
                result[0] = True
        
        #intermediate nodes
        if node.left is not None:
            self.top_down_dfs(node.left,targetSum,result)
        if node.right is not None:
            self.top_down_dfs(node.right,targetSum,result)
            
            
        
