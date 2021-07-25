def LongestCommonSubstring(s1, s2):

    #Using Dynamic programming
    row = len(s1) + 1
    column = len(s2) + 1
    matrix = [[0 for x in range(row)] for y in range(column)]
    # Matrix will hold the lengths of matching substrings
    # The 0th row and column of matrix is zero because when one of s1, s2 is of length 0, LCS length = 0
    print(matrix)
    substring = ''
    longest_length = 0
    for i in range(row):
        for j in range(column):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
                if matrix[i][j] > longest_length:
                    longest_length = matrix[i][j]
            else:
                matrix[i][j] = 0
    print(matrix)

    # To find the longest common substring
    for i in range(row):
        for j in range(column):
            if matrix[i][j] == longest_length:
                x, y = i, j
                while matrix [x][y] != 0:
                    substring += s1[x-1]
                    x -= 1
                    y -= 1
                print(" ".join(list(reversed(list((substring))))))
    return longest_length





print(LongestCommonSubstring('abcdxyz','xyzabcd'))
#Time complexity = O(mxn), m,n size of matrix
#Space complexity = O(mxn), m,n size of matrix
