def sortZeroOneTwos(arr):
    sorted_array = []
    hashmap = {}
    count = 1
    if len(arr) == 0:
        print("Nothing to sort")
        return
    if len(arr) == 1:
        return arr
    for i in range(0, len(arr)):
        if arr[i] in hashmap:
            hashmap[arr[i]] = hashmap[arr[i]] + 1
        else:
            hashmap[arr[i]] = 1
    for key in sorted(hashmap):
        sorted_array.extend(key for i in range(hashmap[key]))
    return sorted_array


print(sortZeroOneTwos([2, 0, 1, 0, 2, 1, 1, 2, 0]))
# Time complexity = O(n*3)
# Space complexity = 2*O(n)

# --------------------------------------------------------------------------------------------

def sort012(arr):
    sorted_array = []
    indexOfOne = 0
    for i in range(len(arr)):
        if arr[i] == 2:
            sorted_array.append(arr[i])
        elif arr[i] == 1:
            sorted_array.insert(indexOfOne, arr[i])
            indexOfOne += 1
        elif arr[i] == 0:
            sorted_array.insert(0, arr[i])
            indexOfOne += 1
        else:
            print("Invalid input")
            return
    return sorted_array


print(sort012([2, 0, 1, 0, 2, 1, 2, 0, 1]))
# Time complexity = O(n)
# Space complexity = O(n)

# -------------------------------------------------------------------------------------
# Dutch Nation Flag algorithm ( 0,1,2 can be colors also )

def sortDNFAlgo(arr):
    low, mid = 0, 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr


print(sortDNFAlgo([2, 0, 1, 0, 2, 1, 2, 0, 1]))
# Time complexity = O(n)
# Space complexity = O(1)
