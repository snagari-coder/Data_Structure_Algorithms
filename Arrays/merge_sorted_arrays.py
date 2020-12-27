#Given two sorted arrays, we need to merge them and create one big sorted array.
#For example, array1 = [1,3,5,7], array2 = [2,4,6,8]
#The result should be array = [1,2,3,4,5,6,7,8]


def merge_sorted_arrays(array1, array2):
    i = 0
    j = 0
    k = 0
    merged_array = []
    # check inputs

    if len(array1) == 0:
        merged_array = array2

    if len(array2) == 0:
        merged_array = array1

    if type(array1) != list or type(array2) != list:
        print('Please give two inputs of type list')

    while i < len(array1) and j < len(array2):

        if array1[i] < array2[j]:
            merged_array.insert(k, array1[i])
            i = i + 1
            k = k + 1
            continue
        if array1[i] == array2[j]:
            merged_array.insert(k, array1[i])
            k = k + 1
            i = i + 1
            merged_array.insert(k, array2[j])
            k = k + 1
            j = j + 1
            continue
        if array1[i] > array2[j]:
            merged_array.insert(k, array2[j])
            j = j + 1
            k = k + 1
            continue
    final_i = i
    final_j = j

    if i != len(array1):
        for a in range(final_i, len(array1)):
            merged_array.insert(k, array1[a])
            k = k + 1
    if j != len(array2):
        for a in range(final_j, len(array2)):
            merged_array.insert(k, array2[a])
            k = k + 1

    return merged_array


# Time complexity = O(n+m)
# Space complexity = O(n+m)

print(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))
