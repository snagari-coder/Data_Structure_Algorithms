# Leetcode 102
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return []
        queue = collections.deque([root])
        while len(queue) != 0:
            temp = []
            count = len(queue)
            for _ in range(count):
                node = queue.popleft()
                temp.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(temp)
            
        return result
    
        # Time complexity = O(n) for visiting each node
        # Space complexity = O(n) for queue
