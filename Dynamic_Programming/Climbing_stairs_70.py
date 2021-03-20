# Leetcode 70: Climbing stairs

# Recursion
def num_of_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return num_of_ways(n - 1) + num_of_ways(n - 2)


# Time complexity = O(n)
# Space complexity = O(1)

def num_of_ways_dp(n):  # Using dynamic programming
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Time complexity = O(n)
# Space complexity = O(n)

def num_of_ways_dp_better(n):  # No need to store all the values, just store the previous two values, to save space
    if n == 0 or n == 1:
        return 1
    num_of_ways_two_before_step = 1
    num_of_ways_one_before_step = 1

    for i in range(2, n + 1):
        num_of_ways_current_step = num_of_ways_two_before_step + num_of_ways_one_before_step
        print(num_of_ways_current_step)
        num_of_ways_two_before_step = num_of_ways_one_before_step
        num_of_ways_one_before_step = num_of_ways_current_step

        print(num_of_ways_current_step)
    return num_of_ways_current_step


# Time complexity = O(n)
# Space complexity = O(1)
print(num_of_ways(4))
print(num_of_ways_dp(4))
print(num_of_ways_dp_better(4))
