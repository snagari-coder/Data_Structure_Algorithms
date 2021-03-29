# You are given a list of n-1 integers and these integers are in the range of 1 to n.
# There are no duplicates in list. One of the integers is missing in the list.
# Write an efficient code to find the missing integer.

def missing_number(arr):
    actual_length = len(arr)
    expected_length = actual_length + 1
    actual_array_sum = 0
    expected_array_sum = expected_length * (expected_length + 1) / 2  # n(n+1)/2
    for i in range(0, actual_length):
        actual_array_sum += arr[i]
    missing_integer = expected_array_sum - actual_array_sum

    return missing_integer


# Time complexity = O(n)
# Space complexity = O(1)
print(missing_number([1, 2, 3, 4, 6, 7, 8, 9, 10]))


# XOR has certain properties
# Assume a1 ^ a2 ^ a3 ^ …^ an = a and a1 ^ a2 ^ a3 ^ …^ an-1 = b
# Then a ^ b = an

def missing_number_xor(arr):
    x1 = arr[0]
    x2 = 1
    n = len(arr)
    for i in range(1, n):
        x1 = x1 ^ arr[i]
    for i in range(2, n + 2):
        x2 = x2 ^ i
    missing_integer = x1 ^ x2
    return missing_integer


# Time complexity = O(n)
# Space complexity = O(1)

print(missing_number_xor([1, 2, 3, 4, 6, 7, 8, 9, 10]))
