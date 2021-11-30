'''

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if nums[i] > 0: #if num is > 0, there is no way this can lead to a sum of 0, hence break
                break
            if i == 0 or nums[i] != nums[i-1]: # make sure there are no duplicate triplets
                self.twosum(i,nums,result)
        return result
                
    def twosum(self,i,nums,result):
        lo = i+1
        hi = len(nums)-1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                result.append([nums[i],nums[lo],nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1

# Time = O(nlogn + n)
# space from \mathcal{O}(\log{n})O(logn) to \mathcal{O}(n)O(n), depending on the implementation of the sorting algorithm. 
# For the purpose of complexity analysis, we ignore the memory required for the output.
#########################################################################################################
def three_sum(nums):
    nums = sorted(nums)
    n = len(nums)
    result = []
    for i in range(n - 2):
        if i == 0 or i > 0 and nums[i] != nums[i-1]: # This makes sure that there are no duplicate triplets
            start = i + 1
            end = n - 1
            sum = 0 - nums[i]

        while start < end:
            # Finding the two sum
            if nums[start] + nums[end] == sum:
                list1 = [nums[i], nums[start], nums[end]]
                result.append(list1)

                start += 1
                end -= 1
            elif nums[start] + nums[end] < sum:
                start += 1
            else:
                end -= 1
    return result


print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([]))
print(three_sum([0]))
