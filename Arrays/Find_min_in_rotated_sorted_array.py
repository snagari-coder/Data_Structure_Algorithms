# Find minimum in rotated sorted array

def find_min(arr):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] > arr[n - 1]:
        pivot_index = find_pivot(arr, 0, n - 1)
        return min(arr[0], arr[pivot_index])
    else:
        return arr[0]


def find_pivot(arr, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if mid + 1 and arr[mid] > arr[mid + 1]:
        return mid + 1
    else:
        if arr[start] > arr[mid]:
            return find_pivot(arr, 0, mid - 1)
        else:
            return find_pivot(arr, mid + 1, end)


print(find_min([1, 2, 3, 4, 5]))
# Time complexity = O(n)
# Space complexity = O(1)
