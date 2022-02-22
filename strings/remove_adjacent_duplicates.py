# Leetcode 1047
# Better
class Solution:
    def removeDuplicates(self, s: str) -> str:
        output = [] #Stack will hold all non-duplicate chars
        for ch in s:
            if output and ch == output[-1]:
                output.pop()
            else:
                output.append(ch)
        return "".join(output)

# Time = O(n)
# Space = O(n-d), where d = sum of length of all duplicate chars, stack space
######################################################################################################
# Given a string, remove adjacent duplicate characters from string. The output string should not
# have any adjacent duplicates. See following examples
# Input:  azxxzy
# Output: ay
# First "azxxzy" is reduced to "azzy". The string "azzy" contains duplicates, so it is further reduced to "ay".
# Input: caaabbbaacdddd
# Output: Empty String
# Input: acaaabbbacdddd
# Output: acac

def remove_adjacent_duplicates(string):
    if len(string) == 0 or len(string) == 1:
        return string
    length = len(string)
    i = 0
    result = []
    while (i < length):
        if i == 0:
            result.append(string[i])
            i += 1


        if len(result) !=  0 and result[len(result)-1] == string[i]:
            while i < length and (result[len(result)-1] == string[i]):
                i += 1
            result.pop()
            #i += 1
        elif len(result) ==  0:
            result.append(string[i])
            i += 1
        else:
            result.append(string[i])
            i += 1

    return result

print(remove_adjacent_duplicates('acaaabbbacdddd'))
