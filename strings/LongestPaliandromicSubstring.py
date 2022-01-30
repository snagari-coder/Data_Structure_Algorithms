#Leetcode 5
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_length = 0
        #algo: Two ways:
        # 1. check first and last char, and move inwards
        # 2. select a middle, and check chars on both sides of middle, and move outwards
        # Here I am using the second algo
        for i in range(len(s)):
            
                #For even length string
                l,r=i,i+1
                while l >=0 and r < len(s) and s[l] == s[r]:
                    if (r-l+1) > result_length:
                        result = s[l:r+1]
                        result_length = (r-l+1)
                    l -= 1 #going outwards
                    r += 1                    

                #For odd length string
                l,r = i,i
                while l >=0 and r < len(s) and s[l] == s[r]:
                    if (r-l+1) > result_length:
                        result = s[l:r+1]
                        result_length = (r-l+1)
                    l -= 1 #going outwards
                    r += 1
        return result
      
      #Time = O(n^2)
