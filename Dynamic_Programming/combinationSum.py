'''
Leetcode 39
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
'''


def combinationSum(candidates, target):
    result = []

    # we use dfs, recursion, back tracking and decision tree
    # one branch we use the candidate, other branch we don't use that candidate, use other candidates if any left
    def dfs(i, current, total):  # current is a list of possible combinations.
        if total == target:
            result.append(current.copy())  # we need to copy here, since we will reuse the same variable
            return
        if i >= len(candidates) or total > target:
            return
        current.append(candidates[i])
        dfs(i, current, total + candidates[i])  # we are including a candidate, hence total is increasing by that value
        current.pop()  # for the other branch, we are not including that candidate, hence removing it from current
        dfs(i + 1, current, total) # opposite branch, where we don't include the candidates[i]

    dfs(0, [], 0)

    return result

print(combinationSum([2,3,6,7],7))
##############################################################################################################################################################
'''
Given an array of distinct integers nums and a target integer target,
return the number of possible combinations that add up to target.
The answer is guaranteed to fit in a 32-bit integer.
Leetcode 377

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
'''


def combinationSum4(nums, target):
    nums = sorted(nums)  # we need to sort, so that we can populate the dp array easily
    n = len(nums)
    if n == 0:
        return -1
    dp = [0] * (target + 1)
    dp[0] = 1
    # dp[1] = number of ways you can get a sum of 1
    # dp[4] = number of ways you can get a sum of 4 with the given elements in nums
    for i in range(1, target + 1):
        for num in nums:
            if num <= i:  # ex: we can make a sum of 4, only with numbers less than or equal to 4
                dp[i] += dp[i - num]
            else:  # if the num in nums is greater than target, break
                break

    return dp[target]


# print(combinationSum4([1, 2, 3], 4))
# print(combinationSum4([2, 3, 6, 7], 7))
