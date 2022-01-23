# Leetcode 142
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    
    # method to find the starting point of the cycle
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        intersect = self.getIntersect(head)
        if intersect is None:
            return None
        pointer1 = head
        pointer2 = intersect
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1
    
    # method to find if cycle exists or not
    def getIntersect(self,head):
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
     # Time = O(n)
     # space = O(1)

#######################################################################################################################################
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashmap = {}
        counter = 0
        if head is None:
            return None
        while head is not None:
            if head in hashmap:
                return head
            hashmap[head] = counter
            counter += 1
            head = head.next
        return None

# Time = space = O(n)

################################################################################################################################################
################################################################################################################################################


#Leetcode 6645
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
# Time = O(n), space = O(1), using two pointer method, one is running fast, other is running slow.
######################################################################################
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_seen = set()
        if head is None:
            return False
        while head is not None:
            if head in node_seen:
                return True
            node_seen.add(head)
            head = head.next
        return False
 # Time = space = O(n), using aux space for storing the visited elements of LL

