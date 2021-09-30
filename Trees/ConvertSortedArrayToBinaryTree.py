# Leetcode 108

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums,start,end):
            if start > end:
                return None
            elif start == end:
                return TreeNode(nums[start])
            
            else:
                mid = int(start + (end-start)/2)
                subtreeroot = TreeNode(nums[mid])
                subtreeroot.left = helper(nums,start,mid-1)
                subtreeroot.right = helper(nums,mid+1,end)
                return subtreeroot
        
        return helper(nums,0,len(nums)-1)
                
        # Time complexity = O(n) - n nodes are performing constant time operations
        # Space complexity = O(n) for the output array. 
        #                    O(height) = O(log n ) for the stack space
