# Leetcode 131
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def is_palindrom(s):
            return s == s[::-1]
        
        def helper(s,idx,slate):
            #back_tracking case:
            # if the last char of the str is not a palindrome then back track
            if len(slate) > 0 and not is_palindrom(s[-1]):
                return 
            #base case:
            if idx == len(s):
                result.append(slate.copy())
                return
                
            #recursive case:
            for pick in range(idx,len(s)):
                if is_palindrom(s[idx:pick+1]):
                    slate.append(s[idx:pick+1])
                    helper(s,pick+1,slate)
                    slate.pop()
        
        helper(s,0,[])
        return result
      
      # Time = O(b ^ h ) = O(n ^ n ) exponential
      # Space = O(n), no new ds is being created or used.
