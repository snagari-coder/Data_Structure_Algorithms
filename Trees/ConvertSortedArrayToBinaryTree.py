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
        
####################################################################################################################################

# If linked list is given instead of array, convert the linked list to array first and then operate on the array as mentioned above:

"""
    For your reference:
    class SinglyLinkedListNode:
        def __init__(self, node_data):
            self.data = node_data
            self.next = None

    class TreeNode():
        def __init__(self, val=None, left_ptr=None, right_ptr=None):
            self.val = val
            self.left_ptr = left_ptr
            self.right_ptr = right_ptr

    Complete the function below.
"""


def sorted_list_to_bst(head):
    """
        Args:
         head(SinglyLinkedListNode_int32)
        Returns:
         TreeNode_in32
    """
    array = []
    def convert_ll_to_array(head):
        while head is not None:
            array.append(head.data)
            head = head.next
        return array
    convert_ll_to_array(head)
    #print('array = ',array)
    
    def helper(array,start,end):
        #base case
        if start > end:
            return None
        elif start == end:
            return TreeNode(array[start])
        else:
            mid = start + int((end-start)/2)
            subtree_rootnode = TreeNode(array[mid])
            subtree_rootnode.left_ptr = helper(array,start,mid-1)
            subtree_rootnode.right_ptr = helper(array,mid+1,end)
            
        return subtree_rootnode
            
    return helper(array,0,len(array)-1)    
        
            
    
            
