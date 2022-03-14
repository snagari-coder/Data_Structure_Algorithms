# Leetcode 160
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointA = headA
        pointB = headB
        while pointA != pointB:
            pointA = headB if pointA is None else pointA.next
            pointB = headA if pointB is None else pointB.next
        return pointA
        
# Time = O(N+M), where N = length of A LL, M = length of B LL
# Space = O(1)
