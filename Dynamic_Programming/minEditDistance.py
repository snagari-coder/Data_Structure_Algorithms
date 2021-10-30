# Minimum edit distance

# Given two strings s1 and s2, what is the minimum number of edits
# you have to make to s1 in order to create s2.
# These types of edits are allowed:
# insert 1 char
# delete 1 char
# replace 1 char

def minimumEditDistance(s1, s2):
    # USING RECURSION
    i = len(s1)
    j = len(s2)

    def helper(str1, str2, i, j):
        if i == 0:
            return j
        elif j == 0:
            return i
        elif str1[i - 1] == str2[j - 1]:  # if last char of s1ms2 match, cancel it and work with remaining strings
            return helper(str1, str2, i - 1, j - 1)
        else:
            # if inserting the last char of s2 in s1, they get canceled and decrement the last char of s2,
            # + 1 for insertion if deleting the last char of s1, then decrement the last char of s1, + 1 for deletion
            # if replacing the last char of s1 to be that of s2, they get canceled and decrement s1,s2 length by 1,
            # + 1 for replacement
            return 1 + min(helper(str1, str2, i - 1, j), helper(str1, str2, i, j - 1), helper(str1, str2, i - 1, j - 1))

    return helper(s1, s2, i, j)


print(minimumEditDistance('abc', 'cab'))


def minimumEditDistance_DP(s1, s2):
    table = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    #table[i][j] = minimum number of edits from s1[:i] to s2[:j]
    for i in range(len(s1)):
        table[i][0] = i # filling in 0th column when len(s2) = 0
    for j in range(len(s2)):
        table[0][j] = j # filling in 0th row when len(s1) = 0

    for i in range(1,len(s1) + 1): # because we already filled the 0th row
        for j in range(1,len(s2) + 1): # because we already filled the 0th column
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i][j - 1], table[i - 1][j], table[i - 1][j - 1])
    print(table)
    return table[len(s1)][len(s2)]

# Time complexity = O(m*n) = space complexity, where m = len(s1), n = len(s2)
print(minimumEditDistance_DP('abc', 'cab'))
