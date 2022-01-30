#Leetcode 49

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #We will create a hashtable, whose keys is a list, and value is a list
        #key = char_count_array 
        #value = list of strings which have same char count array
        result = defaultdict(list)
        for s in strs:
            char_count_array = [0]*26
            
            for char in s:
                char_count_array[ord(char) - ord("a")] += 1
            # We will group all the strings, whose char_count_array is the same
            # keys of hashmap can't be a list. So converting into tuple
            result[tuple(char_count_array)].append(s)
        
        return result.values()
      
      # Time = O(m*n) , where m = length of give list of strings, n = avg length of each string
      # Space = less than or equal to O(m)
      
