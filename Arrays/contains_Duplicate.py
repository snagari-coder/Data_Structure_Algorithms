# Given an integer array nums and an integer k, return true if there are
# two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k
# Leetcode 219
def contains_duplicate(arr, k):
    hashmap = {}
    for i in range(len(arr)):
        if arr[i] in hashmap:
            value = abs(i - hashmap[arr[i]])
            hashmap[arr[i]] = i
            if value <= k:
                return True
        else:
            hashmap[arr[i]] = i

    return False


print(contains_duplicate([99, 99], 2))
# Time complexity = O(n)
# Space complexity = O(n)
