'''
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


def rob(nums):
    sum0 = 0
    sum1 = 0
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    if len(nums) % 2 == 0:
        for i in range(0, len(nums) - 1, 2):
            sum0 = sum0 + nums[i]
        for i in range(0, len(nums), 2):
            sum1 = sum1 + nums[i]
        if sum0 > sum1:
            print(sum0)
        else:
            print(sum1)
    else:
        for i in range(0, len(nums), 2):
            sum0 = sum0 + nums[i]
        for i in range(0, len(nums) - 1, 2):
            sum1 = sum1 + nums[i]
        if sum0 > sum1:
            print(sum0)
        else:
            print(sum1)


##rob([1, 2, 3, 1])
##rob([2, 7, 9, 3, 1])


# Time complexity = O(n)
# space complexity = O(1)

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
    dp = [0] * len(nums)  # This array stores the max values upto the current house.

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
