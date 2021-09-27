# Leetcode 199


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = collections.deque([root])
        result = []
        while len(queue) != 0:
            temp = []
            count = len(queue)
            for _ in range(count):
                node = queue.popleft()
                temp.append(node.val)
                #or temp = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(temp[-1])
            # or result.append(temp)
        return result
      
      # Time complexity = O(n) = Space complexity
