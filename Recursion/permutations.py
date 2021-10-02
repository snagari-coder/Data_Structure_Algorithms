#########################################################################
# Given a string of n distinct characters, print all permutations of size n, no repetition allowed
# Leetcode 46
def permutations_wo_repetitions(nums):
    result = []
    helper(nums, [], result)
    return result


def helper(nums, slate, result):
    if len(slate) == len(nums):
        result.append(slate.copy())
    else:
        cur_idx = len(slate)
        for i in range(cur_idx, len(nums)):
            nums[i], nums[cur_idx] = nums[cur_idx], nums[i]
            slate.append(nums[cur_idx])
            helper(nums, slate, result)
            slate.pop()
            nums[i], nums[cur_idx] = nums[cur_idx], nums[i]


print(permutations_wo_repetitions([1, 2, 3]))
# Time complexity = n*n! ( there are n! leaves and doing copy, which is n work )
# space complexity = explicit -- n*n! ( n! items/permutations each with n elements )
#                   = implicit -- O(n) for callstack
###########################################################################################################################

def permutations_with_repetitions(nums):
    result = []
    helper(nums, [], result)
    return result


def helper(nums, slate, result):
    if len(slate) == len(nums):
        result.append(slate.copy())
    else:

        for i in range(len(nums)):

            slate.append(nums[i])
            helper(nums, slate, result)
            slate.pop()
print(len(permutations_with_repetitions([1, 2, 3])))


###########################################################################################################################
# Printing decimal (0-9) string of length n
# permutations_with_repetitions
def permutations(n):
    permutations_helper('', n)


def permutations_helper(prefix, n):
    if n == 0:
        print(prefix)
    else:
        for i in range(0, n):
            permutations_helper(prefix + str(i), n - 1)


permutations(3)
