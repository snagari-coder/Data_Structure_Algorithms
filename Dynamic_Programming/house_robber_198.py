'''
Leetcode 198
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security systems connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''

def rob_dynamic_programming(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[1]
    dp = [0] * len(nums)  # This array stores the max values upto the current house.

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[len(dp) - 1]


# Time complexity = O(n)
# Space complexity = O(n)
print(rob_dynamic_programming([1, 2, 3, 1]))
print(rob_dynamic_programming([2, 7, 9, 3, 1]))


def rob_dynamic_programming_constSpace(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[1]
    
    maxLootForSecondPreviousHouses = nums[0]
    maxLootForImmediatePreviousHouses = max(nums[0], nums[1])
    maxLoot = maxLootForImmediatePreviousHouses
    for i in range(2, len(nums)):
        maxLoot = max(nums[i] + maxLootForSecondPreviousHouses, maxLootForImmediatePreviousHouses)
        maxLootForSecondPreviousHouses = maxLootForImmediatePreviousHouses
        maxLootForImmediatePreviousHouses = maxLoot

    return maxLoot


# Time complexity = O(n)
# Space complexity = O(1)
print(rob_dynamic_programming_constSpace([1, 2, 3, 1]))
print(rob_dynamic_programming_constSpace([2, 7, 9, 3, 1]))

#####################################################################################################################

# Leetcode 213
'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, 
and it will automatically contact the police if two adjacent houses were broken into on the same night.
'''

def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])
        
        def solve(new_nums):
            maxLootSecondPreviousHouse = new_nums[0]
            maxLootImmediatePreviousHouse = max(new_nums[0], new_nums[1])
            max_loot = maxLootImmediatePreviousHouse
            for i in range(2,len(new_nums)):
                max_loot = max(new_nums[i] + maxLootSecondPreviousHouse, maxLootImmediatePreviousHouse )
                maxLootSecondPreviousHouse = maxLootImmediatePreviousHouse
                maxLootImmediatePreviousHouse = max_loot
            return max_loot
        
        actual_max_loot = max(solve(nums[0:n-1]), solve(nums[1:n])) # Given 12345, you can rob from 1-4 or 2-5 because 1,5 are adjacent. 
        
        return actual_max_loot
