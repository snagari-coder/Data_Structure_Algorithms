import heapq

li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
heapq.heapify(li1)  # To generate min Heap using heapify algo
print(li1)
print(heapq.heappop(li1))  # Deleting the min or topmost element
print(heapq.heappop(li1))
heapq.heappush(li1, 2)  # Inserting an element, maintains the min heap
print(li1)
nlargest = heapq.nlargest(3, li1)  # The 3 largest values from the heap are returned
print(nlargest[2])
print(heapq.nsmallest(3, li1))  # The 3 smallest values from the heap are returned
