# Write a program to print all the LEADERS in the array.
# An element is leader if it is greater than all the elements
# to its right side. And the rightmost element is always a leader.
# For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.

def leader(arr):
    length = len(arr)
    result = []
    result.append(arr[length-1])
    for i in range(0, length-1):
        for j in range(i+1, length):
            if arr[i] < arr[j]:
                count = 0
                break
            else:
                count = 1
                continue
        if count == 1:
            result.append(arr[i])
    return result

print(leader([16,17,4,3,5,2]))
#Time complexity = O(n*n)
#Space complexity = O(m), m < n

#####################################################################################

def leaders_better(arr):
    length = len(arr)
    result = []

    i = length - 1
    max_from_right = 0
    while i >= 0:

        if arr[i] > max_from_right:
            max_from_right = arr[i]
            result.append(max_from_right)
        i = i - 1

    return result

print(leaders_better([16,17,4,3,5,2]))
#Time complexity = O(n)
