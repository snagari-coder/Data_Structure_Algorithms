# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.
# Leetcode 78

def printSubsets(nums):
    result = []
    helper(nums, [], 0, result)
    return result


def helper(nums, slate, idx, result):
    if idx == len(nums):
        result.append(slate.copy())
    else:
        # include
        slate.append(nums[idx])
        helper(nums, slate, idx + 1, result)
        slate.pop()
        # exclude
        helper(nums, slate, idx + 1, result)



print(printSubsets([1, 2, 3]))
# Time complexity = O(2^n)
# Space complexity = O(n) == implicit, callstack length == length of tree
#                   O(2^n) == explicit, 2^n subsets are generated
