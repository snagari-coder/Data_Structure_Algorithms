# Given an integer array nums, find a contiguous non-empty
# subarray within the array that has the largest product, and return the product.
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

def max_product_subarray_better(arr):
    if len(nums) == 0:
        return 0

    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far

    for i in range(1, len(nums)):
        curr = nums[i]
        max_so_far = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

        #max_so_far = temp_max

        result = max(max_so_far, result)

    return result

#Time = O(n), space = O(1)
################################################################
def max_product_subarray(arr):
    if len(nums) == 0:
        return 0
    
    result = nums[0]
    for i in range(len(nums)):
        acc = 1
        for j in range(i,len(nums)):
            acc *= nums[j]
            result = max(result,acc)
    return result


# Time complexity = O(n*2)
# Space complexity = O(1)
print(max_product_subarray([-1, -3, -10, 0, 60]))
print(max_product_subarray_better([-1, -3, -10, 0, 60]))
