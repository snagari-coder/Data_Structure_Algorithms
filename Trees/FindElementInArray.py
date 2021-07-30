# Find the location of a number in an array
def binarySearch(arr,start,end,num):
    n = len(arr)
    mid = (start + end)//2
    while start <= end:
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            end = mid - 1
            return binarySearch(arr,start,end,num)
        else: # arr[mid] < num
            start = mid + 1
            return binarySearch(arr, start, end, num)

    return -1

print(binarySearch([2,5,7,11,12,15,20,30,34,36],0,9,38))


#Time complexity = O(logn)
#Space complexity = O(1)
