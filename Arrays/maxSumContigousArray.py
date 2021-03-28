# Write an efficient program to find the sum of contiguous subarray
# within a one-dimensional array of numbers which has the largest sum.
from sys import maxsize
def maxSumContiguousSubArray(arr):
    max_current = 0
    max_so_far = 0
    for i in range(0, len(arr)):
        max_current = arr[i] + max_current
        if max_current < 0:
            max_current = 0
        else:
            max_so_far = max(max_current, max_so_far)

    return max_so_far
#Time complexity = O(n)
#Space complexity = O(1)

print(maxSumContiguousSubArray([-2, -3, 4, -1, -2, 1, 5, -3]))

# Works when all the numbers in array are negative
def better_way(arr):
    max_current = arr[0]
    max_so_far = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_so_far = max(max_current, max_so_far)
    return max_so_far
#Time complexity = O(n)
#Space complexity = O(1)

# Also outputs the indices between which max sum is created
def maxSumContiguousSubArray_withIndices(arr):
    max_current = 0
    max_so_far = 0
    count, start, end = 0, 0, 0
    for i in range(0, len(arr)):
        max_current = arr[i] + max_current

        if max_current < 0:
            max_current = 0
        else:

            if max_so_far < max_current:
                max_so_far = max_current
                if count == 0:

                    start = i
                    count += 1
                else:
                    end = i

    print("Start index: "+str(start)+" End Index: "+str(end))
    return max_so_far
#Time complexity = O(n)
#Space complexity = O(1)

#print(-maxsize-1)
print(better_way([-2, -3, 4, -1, -2, 1, 5, -3]))
print(maxSumContiguousSubArray_withIndices([-2, -3, 4, -1, -2, 1, 5, -3]))
