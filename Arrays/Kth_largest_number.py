def kth_largest_number(nums,k):
    # In sorted array in ascending order, 1st largest = num[length-1]
    # second largest = num[length-2]
    # kth largest = num[length-k]
    k = len(nums) - k

    def quick_select(left,right): # improvement over quick sort. You select one half of the array over another.
        pivot = nums[right]
        pindex = left
        for i in range(left,right):
            if nums[i] <= pivot:
                nums[i], nums[pindex] = nums[pindex], nums[i]
                pindex += 1
        nums[pindex], nums[right] = nums[right], nums[pindex]

        if k > pindex: return quick_select(pindex+1,right)
        elif k < pindex: return quick_select(left,pindex-1) # depending on the value of K, we select the part of array 
        else: return nums[pindex]                           # to sort again.


    return quick_select(0,len(nums)-1)
print(kth_largest_number([6,2,1,5,4,3],1))
