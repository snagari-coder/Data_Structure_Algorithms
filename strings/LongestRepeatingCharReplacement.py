# Leetcode 424

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap={}
        l = 0
        max_length = 0
        max_freq = 0 # collects the freq of characters in the string
        for r in range(len(s)):
            #hashmap[s[r]] = 1+ hashmap.get(s[r],0)
            if s[r] in hashmap:
                hashmap[s[r]] += 1
            else:
                hashmap[s[r]] = 1
           
            max_freq = max(max_freq,hashmap[s[r]]) # max of max_freq and the freq of char
                                                   # just entered
            
            if (r-l+1) - max_freq > k: # a substring is valid when 
                                       # substring length - max_char_freq <= k
                                       # if not, decrease the freq of that char from 
                                       # hashmap and increment the left pointer by 1
                hashmap[s[l]] -= 1
                l+=1
            else:
                max_length = max(max_length,r-l+1)
        return max_length
        
##################################################################################################

        
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap={}
        l = 0
        max_length = 0
        for r in range(len(s)):
            #hashmap[s[r]] = 1+ hashmap.get(s[r],0)
            if s[r] in hashmap:
                hashmap[s[r]] += 1
            else:
                hashmap[s[r]] = 1
           
            if (r-l+1) - max(hashmap.values()) > k: # Gets the max of values of the hashmap
                
                hashmap[s[l]] -= 1
                l+=1
            else:
                max_length = max(max_length,r-l+1)
        return max_length
        
