#Leetcode 912
# Lomuto's partitioning
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.quick_sort(nums,0,len(nums)-1)
        return nums
        
    def quick_sort(self,nums,start,end):
        if start >= end:
            return
        pivot = random.randint(start,end)
        nums[pivot],nums[start] = nums[start],nums[pivot]
        i = start
        for j in range(start+1,end+1):
            if nums[j] < nums[start]:
                i += 1
                nums[i],nums[j]=nums[j],nums[i]
        nums[i],nums[start]=nums[start],nums[i]
        
        self.quick_sort(nums,start,i-1)
        self.quick_sort(nums,i+1,end)
#######################################################################################################################

import random
def quickSort(nums):
    def helper(A,start,end):
        if start >= end:
            return
        pivotindex = random.randint(start,end)
        A[start],A[pivotindex]=A[pivotindex],A[start]
        orange = start
        for green in range(start+1,end+1):
            if A[green] < A[start]:
                orange += 1
                A[orange],A[green] = A[green],A[orange]
        A[start],A[orange] = A[orange],A[start]

        helper(nums,start,orange-1)
        helper(nums,orange+1,end)
    helper(nums,0,len(nums)-1)
    return nums

print(quickSort([3,2,1,5,4]))
