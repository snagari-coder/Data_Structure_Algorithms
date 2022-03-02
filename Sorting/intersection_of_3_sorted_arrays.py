# Leetcode 1213
class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        p1 = p2 = p3 = 0
        ans = []
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                ans.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            elif arr1[p1] < arr2[p2]:
                p1 += 1
            elif arr2[p2] < arr3[p3]:
                p2 += 1
            else: # if arr1[p1] >= arr2[p2] and arr2[p2] >= arr3[p3]
                p3 += 1
        return ans
#Time = O(n), where n is the total length of all of the input arrays
#space = O(x), where x is the length of smallest array in worst case
