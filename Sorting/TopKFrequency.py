# Leetcode 347

from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        if k == len(nums):
            return nums
        hashmap = Counter(nums) # Counter will create a hashmap based on frequency of numbers
        return heapq.nlargest(k,hashmap.keys(),hashmap.get) #output the k largest numbers based on their freq
    
    # Time = O(nlogk), if k < n to build the heap
    # Space = O(n+k),  for hashmap and heap of k elements

################################ USING QUICK SELECT ###############################################################
    
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
 
        hashmap = {}
        for ele in nums:
            hashmap[ele] = 1 + hashmap.get(ele,0)
        keys = list(hashmap.keys())
        return self.quick_select(keys,0,len(keys)-1,k,hashmap)
        
    def quick_select(self,input,start,end,k,hashmap):
        if k == len(input):
            return input
        if start == end:
            return input[end:]
        pivot_index = self.partition(input,start,end,hashmap)
        # print(pivot_index, input)
        k_index = len(input)-k
        if k_index > pivot_index:
            return self.quick_select(input,pivot_index+1,end,k,hashmap)
        elif k_index < pivot_index:
            return self.quick_select(input,start,pivot_index-1,k,hashmap)
        else:
            return input[pivot_index:]
            
            
    def partition(self,input,start,end,hashmap):
        current = start
        insert_index = start - 1
        pivot_index  = end
 
        while current < pivot_index:
            if hashmap[input[current]] < hashmap[input[pivot_index]]:
                insert_index += 1
                input[current],input[insert_index] = input[insert_index],input[current]
            current += 1
        insert_index += 1
        input[pivot_index],input[insert_index] = input[insert_index],input[pivot_index]
        return insert_index
                    
        
    # Time = O(n) for quickselect, O(n^2) for worst case
    # Space = O(n) for hashmap and array of unique elements
