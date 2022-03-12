# Leetcode 113
# Top down DFS 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        
        def dfs(node,targetSum,slate):
            if node.left is None and node.right is None:
                if targetSum == node.val:
                    slate.append(node.val)
                    result.append(slate.copy())
                    slate.pop()
            
            slate.append(node.val)
            if node.left is not None:
                dfs(node.left, targetSum - node.val,slate)
            if node.right is not None:
                dfs(node.right, targetSum - node.val,slate)
            slate.pop()
        
        dfs(root,targetSum,[])
        return result
        
        # Time complexity = O(nlogn) = Space complexity
        # Because of the slate.copy, slate can have a max of height of tree ( log n ), and there are n leaf nodes, so n log n.
        
        ######################################## Slight Alternate ##################################################################
        
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        result = []
        self.dfs(root,targetSum,[],result)
        return result
    
    def dfs(self,node,target,slate,result):
        target -= node.val
        slate.append(node.val)
        #basecase
        if node.left is None and node.right is None:
            if target == 0:
                result.append(slate[:])
        if node.left:
            self.dfs(node.left,target,slate,result)
        if node.right:
            self.dfs(node.right,target,slate,result)
        slate.pop()
