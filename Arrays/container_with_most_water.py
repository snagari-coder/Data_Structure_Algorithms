#Leetcode 11
def container_with_most_water(arr):
    n = len(arr)
    i, j = 0, n - 1
    max_volume = 0
    while i < j:
        volume = min(arr[i], arr[j]) * (j - i)
        if volume > max_volume:
            max_volume = volume
        if arr[i] < arr[j]:
            i += 1
        else:
            j -= 1

    return max_volume


# print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(container_with_most_water([1, 1]))
# Time complexity = O(n)
# Space complexity = O(1)
