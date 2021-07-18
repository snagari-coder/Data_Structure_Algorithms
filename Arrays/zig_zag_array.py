# convert an array into zig-zag array
# Given an array of DISTINCT elements, 
# rearrange the elements of array in zig-zag fashion in O(n) time. 
# The converted array should be in form a < b > c < d > e < f. 

def zig_zag_array(arr):
    n = len(arr)
    i = 0
    flag = 0
    while i < n and i != n-1:
        if flag == 0:
            if arr[i] < arr[i+1]:
                i += 1
                flag = 1
            else:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                i += 1
                flag = 1
        if flag == 1 and i != n-1: # No need of i != n-1, it is being checked in while loop
            if arr[i] > arr[i+1]:
                i += 1
                flag = 0
            else:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                i += 1
                flag = 0

    return arr

#print(zig_zag_array([3,4,6,2,1,8,9]))
#print(zig_zag_array([4,3,7,8,6,2,1]))
print(zig_zag_array([1,4,3,2]))
#Time complexity = O(n)
#Space complexity = O(1)
