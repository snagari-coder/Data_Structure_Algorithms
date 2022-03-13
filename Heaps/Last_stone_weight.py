
# Leetcode 1046
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 != stone2:
                heapq.heappush(stones,stone1-stone2)
                
        return -stones[0] if stones else 0

        # Time = O(n log n), n times, we are heapifying it
        # space = O(n) for the heap
