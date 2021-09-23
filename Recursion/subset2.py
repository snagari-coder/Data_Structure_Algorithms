#leetcode 90
def subsets2(nums):
    nums = sorted(nums)  # all duplicate values are bundled together. This allows us to count easily how many
    # copies of each value there are
    print(nums)
    result = []
    helper(nums, [], 0, result)
    return result


def helper(nums, slate, idx, result):
    if idx == len(nums):  # base case no more elements are left to examine, reached leaf node
        result.append(slate.copy())
    else:
        count = 1  # of course we have one copy of the element
        j = idx + 1  # but how many are there
        while j < len(nums) and nums[idx] == nums[j]:
            count += 1
            j += 1
        # now we have the number of copies of each element in the given array
        # exclude
        helper(nums, slate, idx + count, result)  # exclude all those copies

        # include
        for copies in range(1, count + 1):  # we include 1 copy, 2 copies, upto count copied
            for op in range(copies):  # append those many copies of nums[idx] to the slate
                slate.append(nums[idx])
            helper(nums, slate, idx + count, result)  # delegate the rest of the work ( not including nums[idx]) to
            # subordinate
            for op in range(copies):
                slate.pop()  # pop out those many copied of nums[idx] for back tracking


print(subsets2([2, 1, 2]))
