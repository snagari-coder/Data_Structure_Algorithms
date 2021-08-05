# Given an integer array nums, find a contiguous non-empty
# subarray within the array that has the largest product, and return the product.
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

def max_product_subarray_better(arr):
    max_product = max(arr)
    current_min, current_max = 1, 1
    for n in arr:
        if n == 0:
            current_min, current_max = 1, 1
            continue
        tmp_max = current_max * n
        tmp_min = current_min * n
        current_max = max(tmp_min, tmp_max, n)
        current_min = min(tmp_min, tmp_max, n)
        max_product = max(max_product, current_max)

    return max_product


def max_product_subarray(arr):
    max_product, product = 0, 1
    n = len(arr)
    i = 0
    for i in range(n):
        product = arr[i]
        for j in range(i + 1, n):
            product *= arr[j]
            max_product = max(product, max_product)
        max_product = max(product, max_product)  # Checking the (n-1)th index by itself
    return max_product


# Time complexity = O(n*2)
# Space complexity = O(1)
print(max_product_subarray([-1, -3, -10, 0, 60]))
print(max_product_subarray_better([-1, -3, -10, 0, 60]))
