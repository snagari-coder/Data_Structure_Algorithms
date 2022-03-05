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
