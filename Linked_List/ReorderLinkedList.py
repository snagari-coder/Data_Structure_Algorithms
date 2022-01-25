# Leetcode 143
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        
        # Step 1: split the LL into two halves, find the middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #Step 2: Reverse the second part of the LL
        prev = None
        current = slow
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        #Step 3: Merge the two linked list
        first = head
        second = prev
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp
            
            tmp = second.next
            second.next = first
            second = tmp
