# Rob cut problem
# Give the length of a rod, and a list of proces for different lengths
# of rods, return the maximum revenue achievable by cutting a rod into pieces

# Using recursion
def rodCut(L, prices):
    # base case
    if L == 0:
        return 0
    maxRevenue = 0
    # recursive case
    for cut in range(0, L):
        revenue = rodCut(cut, prices) + prices[L - cut]
        maxRevenue = max(revenue, maxRevenue)

    return maxRevenue


# Time complexity = O(L!)
# Space = O(L) = stack size, depth of the tree
print(rodCut(3, [0, 4, 10, 13]))


# Using dynamic programming
def rodCut_dp(L, prices):
    # table[i] stores the max revenue obtained for a rod of length i
    table = [-1] * (L + 1)
    table[0] = 0

    for i in range(1, L + 1):
        maxRevenue = 0 # Max revenue of rod of length i
        for cut in range(0, i):
            revenue = table[cut] + prices[i - cut]
            maxRevenue = max(maxRevenue, revenue)
        table[i] = maxRevenue

    return table[L]


# Time complexity = O(L*L) --> Two for loops
# Space complexity = O(L) --> For the 1D array of length L+1
print(rodCut_dp(3, [0, 4, 10, 13]))
