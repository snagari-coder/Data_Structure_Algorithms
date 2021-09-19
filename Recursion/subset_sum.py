# Return all the subsets where the sum is equal to N
# All numbers are positive, no duplicates

def subset_sum(nums, target):
    result = []
    helper(nums, [], 0, target, result)
    return result


def helper(nums, slate, idx, target, result):
    if sum(slate) == target:
        result.append(slate.copy())
        return
    elif sum(slate) > target:
        return
    elif idx == len(nums):
        return
    else:
        # include
        slate.append(nums[idx])
        helper(nums, slate, idx + 1, target, result)
        slate.pop()
        # exclude
        helper(nums, slate, idx + 1, target, result)


print(subset_sum([1, 2, 3], 3))
print(subset_sum([1, 2, 3, 4, 5, 6], 9))

# Time complexity = O(b^n) = O(2^n)
# space complexity = implicite = O(n) = callstack
