#Leetcode 696
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups=[1]
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                groups[-1] += 1
            else:
                groups.append(1)
        ans = 0
        for i in range(1,len(groups)):
            ans += min(groups[i-1],groups[i])
        return ans
        
        # Time = O(n), as we are visiting each element
        # space = O(n), for groups
