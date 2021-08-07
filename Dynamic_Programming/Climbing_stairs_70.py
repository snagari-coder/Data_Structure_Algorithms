# Leetcode 70: Climbing stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

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
=========================================================================================================================================

# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 3 or 5 steps. In how many distinct ways can you climb to the top?
# Here arr is [1,3,5] which is either 1 or 3 or 5

def climbing_stairs_variation(n, arr):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        total = 0
        for j in arr:
            if i - j >= 0:
                total += dp[i - j]
        dp[i] = total
    return dp[n]


# Time complexity = O(n)
# Space complexity = O(n)
# print(climbing_stairs_variation(4, [1, 2])) # Here you can climb either 1 or 2 steps
print(climbing_stairs_variation(4, [1, 3, 5]))  # Here you can climb either 1 or 3 or 5 steps at a time
