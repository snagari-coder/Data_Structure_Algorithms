# Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.
# Ex: Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Output: Sum found between indexes 2 and 4
def targetContiguousSubArray(arr, target):
    n = len(arr)
    start, end = 0, 0
    i = 1
    sum = arr[0]

    while n > i > start:
        if sum == target:
            end = i - 1
            break
        if sum < target:
            sum += arr[i]
            i += 1
        if sum > target:
            sum -= arr[start]
            start += 1
    if end == 0:
        print("There is no such subarray")
    else:
        print("Target sum of " + str(target) + " occurs between: " + str(start) + " and " + str(end) + " indices")


# Time complexity = O(n)
# Space complexity = O(1)
targetContiguousSubArray([1, 4, 20, 3, 10, 5], 33)
targetContiguousSubArray([1, 4, 20, 3, -3, 13], 33)
targetContiguousSubArray([1, 4, 0, 0, 0], 33)
targetContiguousSubArray([35, 35, 35, 35, 35], 33)
targetContiguousSubArray([1, 4, 0, 0, 3, 10, 5], 7)
targetContiguousSubArray([1, 4], 0)


# ------------------------------------------------------------------

# Including negative numbers:

def targetContiguousSubArray_negNumbers(arr, target):
    n = len(arr)
    curr_sum = 0
    hashmap = {}
    for i in range(0, n):
        curr_sum += arr[i]

        if curr_sum == target:
            print("The target sum of " + str(target) + " is between 0 and " + str(i))
            return
        if curr_sum - target in hashmap:
            print("Sum found between: ", hashmap[curr_sum - target] + 1, "to", i)
            return
        hashmap[curr_sum] = i

    # If we reached here, then there is no subarray
    print("No sub-array with give sum exists")

#targetContiguousSubArray_negNumbers([0,2,-2,-20,10], -10)
#targetContiguousSubArray_negNumbers([3,4,7,2,-3,1,4,2], 7)
targetContiguousSubArray_negNumbers([3,0,1,2,-3,1,4,2], 7)
