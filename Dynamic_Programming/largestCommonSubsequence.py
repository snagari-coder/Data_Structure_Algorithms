def longest_common_substring(s1, s2):
    # Using dynamic programming
    m = len(s1)  # rows
    n = len(s2)  # columns
    dp_matrix = [[0 for x in range(n + 1)] for y in range(m + 1)]
    # 2d matrix = [[0 for x in range(columns)] for y in range(rows)]
    # Another way
    # 2d matrix = [[0]*(columns) for i in range(rows)]
    # To find the length of longest common subsequence
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp_matrix[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
            else:  # (s1[i-1] != s2[j-1])
                dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i][j - 1])
    # return dp_matrix[m][n]
    index = dp_matrix[m][n]
    print(f'The length of longest common subsequence is {index}')
    subsequence = [""] * (index + 1)

    subsequence[index] = ''  # Null char at the end of string
    i, j = m, n
    while (dp_matrix[i][j]) != 0:
        if s1[i - 1] == s2[j - 1]:
            subsequence[index - 1] = s1[i - 1]  # or s2[j-1]
            i -= 1
            j -= 1
            index -= 1
        elif dp_matrix[i - 1][j] > dp_matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print(" The longest common subsequence is: ", "".join(subsequence))
    return


print(longest_common_substring("stone", "longest"))
# Time complexity = O(mn) m = length of s1, n = length of s2
# Space complexity = O(mn)

