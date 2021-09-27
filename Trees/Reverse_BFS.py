# Leetcode 107

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = collections.deque([root])
        if root is None:
            return []
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
        #print(result[::-1])
        #print(result.reverse())
        return result[::-1]
      
      # Time complexity = O(n) = Space complexity
