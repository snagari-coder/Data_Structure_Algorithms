def permutations2(nums):
    result = []
    helper(nums, [], result)
    return result


def helper(nums, slate, result):
    if len(slate) == len(nums):
        result.append(slate.copy())
    else:
        cur_idx = len(slate)
        hashmap = {}  # There will be redundancy because many sub-workers will get same task.
        for i in range(cur_idx, len(nums)):
            if nums[i] not in hashmap: # To avoid repetition of permutations we won't give two sub-workers, same job
                hashmap[nums[i]] = 1   # we can do that by checking if a job has been submitted in hashmap
                nums[i], nums[cur_idx] = nums[cur_idx], nums[i]
                slate.append(nums[cur_idx])
                helper(nums, slate, result)
                slate.pop()
                nums[i], nums[cur_idx] = nums[cur_idx], nums[i]


print(permutations2([1, 2, 1]))
