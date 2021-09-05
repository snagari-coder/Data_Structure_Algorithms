#Leetcode 1365
def smallerNumbersThanCurrent(nums):
    result = [0] * len(nums)
    sorted_nums = sorted(nums)
    for i in range(len(nums)):
        result[i] = sorted_nums.index(nums[i]) # The indices of ele in nums in sorted_nums gives the count of smaller ele
    return result



print(smallerNumbersThanCurrent([8,1,2,2,3]))
print(smallerNumbersThanCurrent([1,2,2,3,8]))
print(smallerNumbersThanCurrent([7,7,7,7,7,7]))
