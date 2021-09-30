# Leetcode 250

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        globalCount = [0]
        
    
        def dfs(node):
            #Base case left nodes
            if node.left is None and node.right is None:
                globalCount[0] += 1
                return True

            #Recursive case middle nodes
            amiUnival = True
            if node.left is not None:
                isleftsubtreeUnival = dfs(node.left)
                if not isleftsubtreeUnival or node.val != node.left.val:
                    amiUnival = False

            if node.right is not None:
                isrightsubtreeUnival = dfs(node.right)
                if not isrightsubtreeUnival or node.val != node.right.val:
                    amiUnival = False        

            if amiUnival:
                globalCount[0] += 1

            return amiUnival
        
        dfs(root)
        return globalCount[0]
      
      # Time complexity = O(n) = Space complexity. 
      # Each node is doing constant operation and no extra space is being used.
