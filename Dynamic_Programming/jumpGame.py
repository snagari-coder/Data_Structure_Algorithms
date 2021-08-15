# Leetcode 45, jump game II
# Find the min number of jumps required to each the end of the array
# Dynamic programming
def min_jumps_games(nums):
    n = len(nums)
    min_array_jumps = [float('inf')] * n # Each element here presents the min jumps needed to reach
                                         # ith element from 0th element
    i = 1 # The min jumps needed to reach 0th element is 0, so starting from 1
    min_array_jumps[0] = 0

    while i < n:
        j = 0 # For every increment in i, j will start over from 0
        while j < i:
            if i <= (j + nums[j]): # if i falls in the range of j's jump
                min_array_jumps[i] = min(min_array_jumps[i], min_array_jumps[j] + 1)
            j += 1
        i += 1

    print(min_array_jumps)
    return min_array_jumps[n-1]
#print(min_jumps_games([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))
print(min_jumps_games([2,3,1,1,4]))
# Time complexity = O(n) = Space complexity

#######################################################################################################################################################################


#Leetcode 55
def jumpgame(nums):
    n = len(nums)
    reachable_index = 0 # We store the maximum projectile index after each visit to an index

    for i in range(n):
        if reachable_index < i:
            return False
        reachable_index = max(reachable_index, nums[i]+i)
        if reachable_index == n-1:
            break
    return True

# Time complexity = O(n)
# Space = O(1)
