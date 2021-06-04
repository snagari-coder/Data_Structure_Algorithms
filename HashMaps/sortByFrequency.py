'''
Print the elements of an array in the decreasing frequency. If 2 numbers have same frequency
then print the one which came first
Examples:

Input: arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}

Input: arr[] = {2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999}
'''
from collections import defaultdict


# Sort by Frequency
def sortByFreq(arr, n):
    # arr -> Array to be sorted
    # n   -> Length of Array

    # d is a hashmap(referred as dictionary in python)
    hashmap = defaultdict(lambda: 0)

    for i in range(n):
        hashmap[arr[i]] += 1
    print(hashmap)

    # Sorting the array 'arr' where key
    # is the function based on which
    # the array is sorted
    # While sorting we want to give
    # first priority to Frequency
    # Then to value of item

    arr.sort(key=lambda x: (-hashmap[x], x))
    return arr


arr = [2, 5, 2, 6, 9, 5, 8, 8, 8]
n = len(arr)
solution = sortByFreq(arr, n)
print(*solution) # * removes the brackets and commas
