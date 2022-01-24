# Leetcode 23
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            # say you have four lists A, B, C, D. 
            # Merge A and B to form X and merge C and D to form Y
            # Merge X and Y to form the final merged and sorted LL
            for i in range(0,len(lists),2): # i skips by 2, as I am trying to merge 
                l1 = lists[i]               # every two lists.
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.merge2Lists(l1,l2))
                #print(mergedLists)
            lists = mergedLists
        return lists[0]
    
    def merge2Lists(self, l1,l2):
        prehead = ListNode(-1)
        previous = prehead
        
        while l1 and l2:
            if l1.val <= l2.val:
                previous.next = l1
                l1 = l1.next
            else:
                previous.next = l2
                l2 = l2.next
            previous = previous.next
        if l1:
            previous.next = l1
        if l2:
            previous.next = l2
        return prehead.next
