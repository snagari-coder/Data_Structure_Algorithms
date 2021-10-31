#Leetcode 416
#Using Dynamic programming
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        n = len(nums)

        target_sum = int((sum(nums) / 2))
        table = [[0 for x in range(target_sum + 1)] for y in range(n + 1)]

        for x in range(n + 1):
            table[x][0] = 1

        for x in range(1, target_sum + 1):
            table[n][x] = 0

        for i in range(n - 1, -1,-1):
            for j in range(1, target_sum + 1):
                lower_j = j - nums[i]
                table[i][j] = table[i + 1][j] or (lower_j >= 0 and table[i + 1][lower_j])

        #print(table)
        if table[0][target_sum]:
            return True
        else:
            return False
          
        #Time complexity = space = O(n*m), as we are using 2D array
#####################################################################################
#Using recursion. 
#There will be lot of overlapping problems, so for large inputs, you will get "time limit exceeded error"
        def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        target_sum = sum(nums)//2
        n = len(nums)
        
        def helper(nums,i,k):
            if k == 0:
                return True
            if i == n and k != 0:
                return False
            return helper(nums,i+1,k) or helper(nums,i+1,k-nums[i])
        
        
        return helper(nums,0,target_sum)
