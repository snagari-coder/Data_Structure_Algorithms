# Leetcode 77
# Given two integers n and k, return all possible combinations of k numbers out of 1 to n
def combinations(n, k):
    result = []
    helper(n, k, [], 1, result)
    return result


def helper(n, k, slate, cur_idx, result):
    if len(slate) == k:
        result.append(slate.copy())
        return
    elif len(slate) > k:
        return
    elif cur_idx == n + 1:
        return
    else:
        # include
        slate.append(cur_idx)
        helper(n, k, slate, cur_idx + 1, result)
        slate.pop()
        # exclude
        helper(n, k, slate, cur_idx + 1, result)


print(combinations(4, 2))
