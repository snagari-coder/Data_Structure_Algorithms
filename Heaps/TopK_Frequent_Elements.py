# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Leetcode 347

def topKFrequent(nums, k):
    hashmap = {}
    n = len(nums)
    freq = [[] for i in range(n + 1)]
    result = []
    for i in range(len(nums)):
        if nums[i] in hashmap:
            hashmap[nums[i]] += 1
        else:
            hashmap[nums[i]] = 1

    print(hashmap)
    for key, value in hashmap.items():
        freq[value].append(key)

    print(freq)

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result

print(topKFrequent([1,1,1,2,2,3],2))

# Time complexity = O(n)
# Space complexity = 2*O(n)

###########################################################################################################################
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        output = []
        for i in range(len(nums)): # find freq of each element
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        
        print(hashmap)
        for key, value in hashmap.items(): # create a list of lists, consisting of key, value pair in result array
            result.append([key,value])
        
        print(result)
        def take_second(elem):
            return elem[1]
        
        result_f = sorted(result,key=take_second, reverse=True) # sort result based on value ( = freq of elements )
        for i in range(k):
            output.append(result_f[i][0]) # give the output only the key values
        
        return output
      
# Time complexity = O(n) + O(nlogn)
# Space complexity = O(n), without considering the output array space
