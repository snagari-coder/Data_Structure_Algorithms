'''
Leetcode 153. Find Minimum in Rotated Sorted Array

'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[len(nums)-1]:
            return nums[0]
        left,right = 0,len(nums)-1
        while right >= left:
            mid = left + (right-left)/2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[0]<nums[mid]:
                left=mid+1
            else:
                right=mid-1
                
#Time = O(log n)
#space = O(1)

########################################################################################
# Find minimum in rotated sorted array

def find_min(arr):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] > arr[n - 1]:
        pivot_index = find_pivot(arr, 0, n - 1)
        return min(arr[0], arr[pivot_index])
    else:
        return arr[0]


def find_pivot(arr, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if mid + 1 and arr[mid] > arr[mid + 1]:
        return mid + 1
    else:
        if arr[start] > arr[mid]:
            return find_pivot(arr, 0, mid - 1)
        else:
            return find_pivot(arr, mid + 1, end)


print(find_min([1, 2, 3, 4, 5]))
# Time complexity = O(n)
# Space complexity = O(1)
