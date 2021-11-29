def merge_sort(A):
    def helper(nums, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        helper(nums, start, mid)
        helper(nums, mid + 1, end)
        aux = []
        i, j = start, mid + 1
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                aux.append(nums[i])
                i += 1
            else:
                aux.append(nums[j])
                j += 1
        while i <= mid:
            aux.append(nums[i])
            i += 1
        while j <= end:
            aux.append(nums[j])
            j += 1

        nums[start:end+1] = aux

    helper(A, 0, len(A) - 1)
    return A


print(merge_sort([3, 5, 2, 4, 1]))
