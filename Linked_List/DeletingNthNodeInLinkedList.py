# Leetcode 19
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode(-1,head)
        left = dummy
        right = head
        i = n
        # Left starts from dummy
        # Right pointer starts from nth node from the begining
        # The distance between left and right pointer is always n
        # Keep moving left and right pointer, until right reaches end of LL
        # The left will be at the node prior to the node that needs to be deleted.
        while i > 0:
            right = right.next
            i -= 1
        
        while right:
            right = right.next
            left = left.next
        
        #delete
        left.next = left.next.next
        
        return dummy.next
  ############################################################################################################################################################
# Convert LL into a list. Remove the element from the last, and convert the list back into linkedlist. 
# Uses auxillary space
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        aux = []
        while head:
            aux.append(head.val)
            head = head.next
        
        #aux.remove(aux[len(aux)-n]) # remove - removes an item based on value
        aux.pop(len(aux)-n) # pop - removes an item based on index
        print(aux)
        dummy = ListNode(-1,head)
        previous = dummy
        for ele in aux:
            previous.next = ListNode(ele)
            previous = previous.next
        return dummy.next
