
# Leetcode 21
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        prehead = ListNode(-1)
        prev = prehead
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev= prev.next
        prev.next = list1 if list1 is not None else list2
        
        return prehead.next
      
      # Time complexity = O(m+n), where m,n are the length of list1, list2
      # Space complexity = O(1), other than few pointers, we didnt use any additional space
