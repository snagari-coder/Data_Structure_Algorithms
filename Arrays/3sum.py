'''

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''
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
