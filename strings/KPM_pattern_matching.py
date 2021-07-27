# KMP (Knuth-Morris-Pratt) string matching algorithm
## REVISE ##
def kmp_compare(string, pattern):
    string_length = len(string)
    pattern_length = len(pattern)
    lps = [0] * pattern_length # longest prefix suffix string
    compute_lps_array(pattern, lps, pattern_length)
    i = 0
    j = 0

    while i < string_length and j < pattern_length:
        if string[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == pattern_length:
            print("Found the pattern in given string at: ", i - j)
            j = lps[j-1]


def compute_lps_array(pattern, lps, pattern_length):
    lps[0] = 0  # First element of lps is always zero.
    Len = 0
    i = 1

    while i < pattern_length:
        if pattern[i] == pattern[Len]:
            Len += 1
            lps[i] = Len
            i += 1
        else:
            if Len != 0:
                Len = lps[Len - 1]
            else:
                lps[i] = 0
                i += 1

# Time complexity = O(n+m), n = length of string, m = length of pattern
#kmp_compare('ababcabcabababd', 'ababd')
kmp_compare('aabaacaadaabaaba', 'aaba')
