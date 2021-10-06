# Leetcode 257

# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below
# Input: root of the input tree
# Output: A list of integer lists denoting the node values of the paths of the tree

def allPathsOfABinaryTree(root):
    if root is None:
        return []
    result = []
    
    def dfs(node,slate):
        if node.left_ptr is None and node.right_ptr is None:
            slate.append(node.val)
            result.append(slate.copy())
            slate.pop()
            
        slate.append(node.val)
        if node.left_ptr is not None:
            dfs(node.left_ptr,slate)
        if node.right_ptr is not None:
            dfs(node.right_ptr,slate)
        slate.pop()
    
    dfs(root,[])
    return result
  # Time complexity = O(n) -- passing through each node
  # Space complexity = O(n) -- for call stack, implicit and explicit
  #                   worst case = O(n), unbalanced tree, for balanced tree, height = log(n)
