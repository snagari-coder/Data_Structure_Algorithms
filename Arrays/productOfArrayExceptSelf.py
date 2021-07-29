'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''

def productExceptSelf_better(nums):
    previous, product = 1, 1
    output = []
    n = len(nums)
    for i in range(n):
        previous *= nums[i]
        output.append(previous)

    for i in range(n - 1, -1, -1):
        if i == n - 1:
            print(output[i - 1])
            output[i] = output[i - 1]
            product *= nums[i]
        elif i == 0:
            output[i] = product
        else:
            insert_element = output[i - 1] * product
            output[i] = insert_element
            product *= nums[i]

    return output


def productExceptSelf(nums):
    ## If division is allowed ##
    product = 1
    result = []
    for i in range(len(nums)):
        product *= nums[i]

    for i in range(len(nums)):
        if nums[i] != 0:
            result.append(product // nums[i])

    return result


print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelf_better([1, 2, 3, 4]))
print(productExceptSelf_better([-1,1,0,-3,3]))
