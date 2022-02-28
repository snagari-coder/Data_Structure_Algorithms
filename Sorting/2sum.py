
'''
Leetcode 1. Two Sum
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap={}
        for i in range(len(nums)):
            if target-nums[i] in hashmap:
                result = (i,hashmap[target-nums[i]])
            else:
                hashmap[nums[i]] = i
        return result
  # Time = space = O(n)

#Using set:
def two_sum(input,target):
    values = set()
    result = False
    for value in input:
        difference = target - value
        if difference in values:
            result = True
        values.add(value)
    return result
print(two_sum([5,9,1,3],6))

##############################################################
'''
Leetcode 167. Two Sum II - Input Array Is Sorted
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j=0,len(numbers)-1
        while i < j:
            if numbers[i]+numbers[j] == target:
                return (i+1,j+1)
            elif numbers[i]+numbers[j] > target:
                j -= 1
            else: 
                i += 1
                
 # Time complexity = O(n), space = O(1)

#########################################################################
'''
Leetcode 1099. Two Sum Less Than K
'''
class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i,j = 0, len(nums)-1
        answer = -1
        while i < j:
            sum = nums[i] + nums[j]
            if sum < k:
                answer = max(answer,sum)
                i += 1
            else:
                j-= 1
        return answer

    #Time complexity = O(nlogn) + O(n)
    #Space = O(1)
