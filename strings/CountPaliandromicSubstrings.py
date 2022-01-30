# Leetcode 647
class Solution:
    def countSubstrings(self, s: str) -> int:
        #result_list = [] #if you maintain a list of strings then out of memory problems occur.
        count_pali = 0
        for i in range(len(s)):
            #odd length string
            l,r=i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #result_list.append(s[l:r+1])
                count_pali += 1
                l -= 1
                r += 1
            
            #even lenth string
            l,r=i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #result_list.append(s[l:r+1])
                count_pali += 1
                l -= 1
                r += 1
            
        #print(result_list)
        #return len(result_list)
        return count_pali
      
# Time = O(n^2), we are visiting each char of string, atleast twice

######################################################   CONCISE VERSION  ################################################

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count_pali = 0
        for i in range(len(s)):
            
            count_pali += self.countPaliandromicSubstring(s,i,i) #for odd length string
            count_pali += self.countPaliandromicSubstring(s,i,i+1)#for even length string
        return count_pali    
            
    def countPaliandromicSubstring(self,s,l,r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
