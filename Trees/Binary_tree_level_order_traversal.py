# Leetcode 107
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        q = collections.deque([root])
        while len(q) != 0:
            temp = []
            nodes_per_layer = len(q)
            for _ in range(nodes_per_layer):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                temp.append(node.val)
            result.append(temp)
        return reversed(result)
        
# Time = O(n), for n nodes
# space = O(n) for queue
