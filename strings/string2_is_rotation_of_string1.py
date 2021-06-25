# Given two strings, the task is to find if a string ('a') can be obtained by rotating another
# string ('b') by two places.
# Examples:
# Input : a = "amazon"         b = "azonam"  // rotated anti-clockwise
# Output : True
# Input : a = "amazon"        b = "onamaz"  // rotated clockwise
# Output : True

# KMP (Knuth-Morris-Pratt) string matching algorithm

def is_rotated_or_not(string1, string2):
    if len(string1) != len(string2):
        print("The string2 is not the rotation of string1")
        return False
    else:
        combined_string = string1 + string1
        pattern_to_find = string2
        result = kmp_compare(combined_string, pattern_to_find)
        if result == '1':
            print(f'{string1} is a rotation of {string2}')
            return
        else:
            print(f'{string1} is not a rotation of {string2}')
            return "No"


def kmp_compare(string, pattern):
    string_length = len(string)
    pattern_length = len(pattern)
    lps = [0] * pattern_length  # longest prefix suffix string
    compute_lps_array(pattern, lps, pattern_length)
    i = 0
    j = 0

    while i < string_length and j < pattern_length:
        if string[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        if j == pattern_length:
            # print("Found the pattern in given string at: ", i - j)
            print(f'{pattern} is obtained by left rotating: ' + str(i - j) + ' times')
            print(f'{pattern} is obtained by right rotating: ' + str(pattern_length - (i - j)) + ' times')
            j = lps[j - 1]
            return '1'

    return '0'


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
# kmp_compare("amazonamazon", "azonam")
is_rotated_or_not("amazon", "azonam")
