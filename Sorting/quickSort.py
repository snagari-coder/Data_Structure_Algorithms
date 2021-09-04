import random
def quickSort(nums):
    def helper(A,start,end):
        if start >= end:
            return
        pivotindex = random.randint(start,end)
        A[start],A[pivotindex]=A[pivotindex],A[start]
        orange = start
        for green in range(start+1,end+1):
            if A[green] < A[start]:
                orange += 1
                A[orange],A[green] = A[green],A[orange]
        A[start],A[orange] = A[orange],A[start]

        helper(nums,start,orange-1)
        helper(nums,orange+1,end)
    helper(nums,0,len(nums)-1)
    return nums

print(quickSort([3,2,1,5,4]))
