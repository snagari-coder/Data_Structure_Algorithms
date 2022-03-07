#Leetcode 703
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:  #keep poping from min heap, until the size of heap is k
            heapq.heappop(self.heap) 
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]  #top most element of min heap of size k, will be the kth largest element
        
        
# contructor Time = O(n log n) --> for converting array to heap and adding
# add function Time = O(m.log k) --> m add func calls and maintaining heap of size k
# Space = O(n) for heap


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
