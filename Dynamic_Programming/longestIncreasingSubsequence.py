def longestIncreasingSubsequence_better(arr):
    # Using dynamic programming
    n = len(arr)
    dp = [1] * n  # Every ele of arr is a longestIncreasingSubsequence of length 1, hence one in each of dp ele
    i, j = 1, 0  # Since for 0th ele we already know LIS is of length 1, we start from index 1
    max_length = 1
    while i < n:
        while j < i:
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], 1 + dp[j])  # Each ele of dp represents max length of increasing subsequence
                # until that point
                # Adding one because we are adding the current ele to the previous
                # max length of increasing subsequence
                if max_length < dp[i]:
                    max_length = dp[i]
                j += 1
                continue
            else:
                j += 1

        i += 1  # Every time i increases by 1, j goes to the starting of the array.
        j = 0
    print(dp)
    return max_length


print(longestIncreasingSubsequence_better([10, 9, 2, 5, 3, 7, 101, 18]))
# Time complexity = O(n)
# Space complexity = 0(n)

def longestIncreasingSubsequence(arr):
    n = len(arr)
    maxSubsequenceLength = 0
    for i in range(n):
        result = []
        while i < n:
            if len(result) == 0:
                result.append(arr[i])
                result_count = 0
                i += 1
            else:
                if arr[i] > result[result_count]:
                    result.append(arr[i])
                    result_count += 1
                    i += 1
                else:
                    i += 1
        if maxSubsequenceLength < len(result):
            maxSubsequenceLength = len(result)

    return maxSubsequenceLength


print(longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18]))
# Time: O(n*2)
# Space = O(m) - m is length of subsequence
