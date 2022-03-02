# 4 questions here


def merge_sorted_no_duplicates(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    i, j = 0, 0
    aux = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            aux.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            aux.append(l2[j])
            j += 1
        else:
            aux.append(l1[i])
            i += 1
            j += 1

    return aux

print(merge_sorted_no_duplicates([2, 3, 5, 6, 7, 8, 12], [5, 6, 8, 9, 10])) # [2, 3, 5, 6, 7, 8, 9, 10]

def merge_sorted(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    i, j = 0, 0
    aux = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            aux.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            aux.append(l2[j])
            j += 1
        else:
            aux.append(l1[i])
            i += 1
            j += 1

    return aux
print(merge_sorted([2, 3, 5, 6, 7, 8, 12], [5, 6, 8, 9, 10])) # [2, 3, 5, 5, 6, 6, 7, 8, 8, 9, 10]

def intersect(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    i, j = 0, 0
    aux = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            aux.append(l1[i])
            i += 1
            j += 1

    return aux
print(intersect([2, 3, 5, 6, 7, 8, 12], [5, 6, 8, 9, 10])) # [5, 6, 8]

##############################################################################################
# Leetcode 88
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        for p in range(m+n-1,-1,-1):
            if p2 < 0:
                break
            if p1 >= 0 and nums2[p2] < nums1[p1]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                
# Time = O(m+n)
# Space = O(1)
