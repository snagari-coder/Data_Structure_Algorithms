# Is one array a rotation of another ?
# Example: [1,2,3,4,5,6,7] is a rotation of [4,5,6,7,1,2,3]
# Note: There are no duplicates in each of these arrays
# Implement your function below.
def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    if list2[0] in list1:
        list1_p = list1.index(list2[0]) # pointer of list1
    else:
        return False

    i = 0

    while list1_p + i < len(list1):
        if list1[list1_p + i] == list2[i]:
            i += 1
        else:
            return False

    while i < len(list2):
        for j in range(list1_p):
            if list1[j] == list2[i]:
                i += 1
            else:
                return False

    return True


print(is_rotation([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 1, 2, 3]))

# Time complexity = O(n)
'''
# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
list2g = [7, 1, 2, 3, 4, 5, 6]
# is_rotation(list1, list2g) should return True.

'''
