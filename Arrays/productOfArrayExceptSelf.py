'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''

def productExceptSelf_better(nums):
    result = [1]*len(nums)
    for i in range(1,len(nums)): #assuming there is 1 preceeding the nums array
        result[i] = result[i-1]*nums[i-1] #creating prefix array
    temp = 1 #assuming there is 1 succeding the nums array
    for i in range(len(nums)-1,-1,-1):
        result[i] = temp * result[i]
        temp = temp * nums[i]

    return result
#Time = 2 * O(n), Space = O(1)

###################################################################################
def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [1]*len(nums)
        suffix = [1] * len(nums)
        result = [1] * len(nums)
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]

        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]
        

        return result

    # Time = space = 3 * O(n) = O(n)


print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelf_better([1, 2, 3, 4]))
print(productExceptSelf_better([-1,1,0,-3,3]))
