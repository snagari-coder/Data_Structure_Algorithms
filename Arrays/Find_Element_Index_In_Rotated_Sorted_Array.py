# Find an element in shifted/rotated sorted array.
# Given an array = [9,12,15,17,25,28,32,37,3,5,7,8]
# Find the index of element 17.

def find_element_in_sorted_rotated_array(arr, ele):
    n = len(arr)

    pivot_index = find_pivot(arr, 0, n - 1)
    print(pivot_index)
    if arr[pivot_index] == ele:
        return pivot_index
    if arr[0] < ele < arr[pivot_index - 1]:
        # search in left side
        index = binary_search(arr, 0, pivot_index - 1, ele)
        return index
    if arr[pivot_index + 1] < ele < arr[n - 1]:
        # search in right side
        index = binary_search(arr, pivot_index + 1, n - 1, ele)
        return index

    return -1


def find_pivot(arr, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if mid + 1 and (arr[mid] > arr[mid + 1]):
        pivot_index = mid + 1
        return pivot_index
    else:
        if arr[start] > arr[mid]:
            # Check in the first part of array
            return find_pivot(arr, start, mid - 1)
        else:
            # Check in the second part of array
            return find_pivot(arr, mid + 1, end)


def binary_search(arr, start, end, ele):
    mid = (start + end) // 2
    while start <= end:
        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            return binary_search(arr, start, mid - 1)
        else:
            return binary_search(arr, mid + 1, end)
    return -1


print(find_element_in_sorted_rotated_array([9, 12, 15, 17, 25, 28, 32, 37, 3, 5, 7, 8], 17))
# print(find_pivot([9,12,15,17,25,28,32,37,3,5,7,8], 0, 11))

# Time complexity = O(log n)
# Space complexity = O(1)
