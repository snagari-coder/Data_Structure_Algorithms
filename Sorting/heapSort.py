import heapq
def heapSort(nums):
    heapq.heapify(nums)
    result = []
    while len(nums) != 0:
        result.append(heapq.heappop(nums))
    return result

print(heapSort([2,4,1,3,5]))
