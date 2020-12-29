# Given an array, return the first recurring character
# Example1 : array = [2,1,4,2,6,5,1,4]
# It should return 2
# Example 2 : array = [2,6,4,6,1,3,8,1,2]
# It should return 6


def first_recurring_character(array1):
    count = 0
    hash_map = {}
    for i in range(0, len(array1)):
        if array1[i] in hash_map:
            count = count + 1
            hash_map.update({array1[i]: count})
            return array1[i]
        else:
            count = 1
            hash_map.update({array1[i]: count})

    return "undefined"


# Time complexity O(n)
# Space complexity O(n)

print(first_recurring_character([2, 5, 5, 2, 3, 5, 1, 2, 4]))


def frc_no_extra_space(array1):
    i = 0
    result = None
    length = len(array1)
    while i < length:
        j = i + 1
        while j < length:
            if array1[i] == array1[j]:
                length = j
                result = array1[j]
                continue
            else:
                j += 1

        i += 1
    return result


# Time complexity = O(n*n)
# Space complexity = O(1)

print(frc_no_extra_space([2, 5, 5, 2, 3, 5, 1, 2, 4]))
