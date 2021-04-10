# Write a function that returns the common elements ( as an array ) between two sorted arrays of integers ( ascending order ).
def common_elements(list1, list2):
    result = []

    i, j = 0, 0
    if len(list1) == 0 or len(list2) == 0:
        return None

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
            continue
        if list1[i] > list2[j]:
            j += 1
            continue
        if list1[i] < list2[j]:
            i += 1
            continue
    return result

print(common_elements([1,3,4,6,7,9],[1,2,4,5,9,10]))
#list_b1 = [1, 2, 9, 10, 11, 12]
#list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]

#list_c1 = [0, 1, 2, 3, 4, 5]
#list_c2 = [6, 7, 8, 9, 10, 11]
#Time complexity = max(len(arr1),len(arr2))
