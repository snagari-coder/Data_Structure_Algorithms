#Given two sorted arrays, we need to merge them and create one big sorted array.
#For example, array1 = [1,3,5,7], array2 = [2,4,6,8]
#The result should be array = [1,2,3,4,5,6,7,8]



   def mergeSortedArray(nums1, nums2):
        i, j = 0, 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                result.append(nums2[j])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:  # nums1[i] > nums2[j]
                result.append(nums2[j])
                j += 1

        if i != len(nums1) - 1:
            for xi in range(i,len(nums1)):
                result.append(nums1[x])

        if j != len(nums2) - 1:
            for y in range(j,len(nums2)):
                result.append(nums2[y])

        return result


# Time complexity = O(n+m)
# Space complexity = O(n+m)

print(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))
