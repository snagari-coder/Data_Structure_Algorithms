
# Leetcode 231
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (-n) == n
    
    # Notes:
    # -x = ~x+1
    # If a number is power of two, it has only one 1 bit, rest are all 0's
    # For a power of two, 'and' operation of n and -n will be same as n

############## Original ###############
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        while n > 1:
            if n%2 == 0:
                n = n/2
            else:
                return False
        if n == 1:
            return True
        else:
            return False
        
        # Time = O(log n), as you decrease by 2 in every step
        # space = O(1)
