def sortedSquares(nums):
    i = 0 # First ele
    j = len(nums) - 1 # last element
    result = [0] * (len(nums))
    k = len(nums) - 1 #insert from the last ele of the result list
    while i < j:
        if abs(nums[i]) < abs(nums[j]):
            #result.insert(k, nums[j] * nums[j])
            result[k] = nums[j] * nums[j]
            k -= 1
            j -= 1
        else:

            result[k] = nums[i] * nums[i]
            i += 1
            k -= 1
    result[k] = nums[j] * nums[j]
    return result

print(sortedSquares([-4,-1,0,3,10]))
