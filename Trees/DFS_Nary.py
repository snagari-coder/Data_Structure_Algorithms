"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
######################### POSTORDER ###############################
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = [root]
        result = []
        while len(stack) != 0:
            root = stack.pop()
            result.append(root.val)
            for child in root.children:
                stack.append(child)
        return result[::-1]
        
  # Time = O(N) = Space
  
  ######################### PREORDER ###############################
  class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = [root]
        result = []
        while len(stack) != 0:
            root = stack.pop()
            result.append(root.val)
            stack.extend(root.children[::-1])

        return result
