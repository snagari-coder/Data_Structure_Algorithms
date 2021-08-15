
#Leetcode 63
def uniquePaths2_withObstacles(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    dp = [[0 for i in range(columns)] for i in range(rows)]  # create a new dp matrix.
    if matrix[rows - 1][columns - 1] == 1 or matrix[0][0] == 1:
        return 0
    # Where ever there is obstacle, dp will have zero in its place
    dp[rows - 1][columns - 1] = 1
    for i in range(columns - 2, -1, -1):  # starting from the target, last row is all 1 if there is no obstacle
        if matrix[rows - 1][i] != 1:
            dp[rows - 1][i] = dp[rows - 1][i + 1] + 0
        else:
            dp[rows - 1][i] = 0

    for i in range(rows - 2, -1, -1):  # starting from the target, last column is all 1 if there is no obstacle
        if matrix[i][columns - 1] != 1:
            dp[i][columns - 1] = dp[i + 1][columns - 1] + 0
        else:
            dp[i][columns - 1] = 0

    for i in range(rows - 2, -1, -1):
        for j in range(columns - 2, -1, -1):
            if matrix[i][j] != 1:
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
            else:
                dp[i][j] = 0

    print(matrix)
    print(dp)
    return dp[0][0]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(uniquePaths2_withObstacles(obstacleGrid))
# Time complexity = O(r * c)  = space complexity

############################################################################################################################################################

#Leet code 62
def uniquePaths(r, c):
    dp = [[0 for i in range(c)] for i in range(r)]
    for i in range(c - 1, -1, -1):
        dp[r - 1][i] = 1
    for i in range(r - 1, -1, -1):
        dp[i][c - 1] = 1

    for i in range(r - 2, -1, -1):
        for j in range(c - 2, -1, -1):
            dp[i][j] = dp[i+1][j] + dp[i][j+1]

    print(dp)
    return dp[0][0]

print(uniquePaths(3, 7))
# Time = space = complexity = O(r*c)
