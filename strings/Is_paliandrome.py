# Leetcode 125
class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1 # one pointer starting from 0 and other from end

        while i < j:
            while i < j and not s[i].isalnum(): # if there is non alpha and non number, skip that
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
     
    # Time = O(n)
