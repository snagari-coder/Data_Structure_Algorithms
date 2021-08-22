# Median of streaming in numbers:
# We divide the input sorted array = left part ( Max Heap ) and right part ( Min Heap )
# The Max of max heap = last element of left part
# The min of min heap = first element of right part
# We assume that the difference between len of max heap and min heap is 1
# The length of max heap can only be one more that the min heap

import heapq


class MedianFinder:
    def __init__(self):
        self.minHeap = []  # initializing the minHeap
        heapq.heapify(self.minHeap)
        self.maxHeap = []
        heapq.heapify(self.maxHeap)

    def add_Number(self, num):
        if not self.maxHeap and not self.minHeap:  # The first element goes to maxHeap ( left part )
            heapq.heappush(self.maxHeap, -num)
            return
        if not self.minHeap:
            if num > -self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                temp = -self.maxHeap[0]
                self.maxHeap.pop()
                heapq.heappush(self.minHeap, temp)
                heapq.heappush(self.maxHeap, -num)
            return
        if len(self.maxHeap) == len(self.minHeap):
            if num < self.minHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                temp = self.minHeap[0]
                self.minHeap.pop()
                heapq.heappush(self.maxHeap, -temp)
                heapq.heappush(self.minHeap, num)
        elif len(self.maxHeap) > len(self.minHeap):
            if num < self.minHeap[0]:

                heapq.heappush(self.minHeap, -self.maxHeap.pop())
                heapq.heappush(self.maxHeap, -num)

            else:
                heapq.heappush(self.minHeap, num)

    def find_Median(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + (-self.maxHeap[0])) / 2
        elif len(self.maxHeap) > len(self.minHeap):  # max heap has more elements, head of maxHead is returned
            return -self.maxHeap[0]


S = MedianFinder()
S.add_Number(5)
print(S.find_Median())
S.add_Number(3)
result = S.find_Median()
print(result)
S.add_Number(4)
result = S.find_Median()
print(result)
S.add_Number(2)
print(S.find_Median())
S.add_Number(6)
result = S.find_Median()
print(result)

# Time complexity = O(nlogn) ---> log n is for inserting into heaps. For inserting n integers, it is nlogn.
# We can also use insertion sort every time a new number is streamed in, and find median. Time complexity in this case is O(n*2)
