# Leetcode 429

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = collections.deque([root])
        
        while len(queue) != 0:
            temp = []
            count = len(queue)
            for _ in range(count):
                node = queue.popleft()
                temp.append(node.val)
                
                for child in node.children:
                    queue.append(child)
            result.append(temp)
        return result
                    
  # Time complexity = O(n) == Space complexity
