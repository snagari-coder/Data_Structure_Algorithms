# Given a string s and a dictionary of strings wordDict, return true if s can be
# segmented into a space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# Leetcode 139
def wordBreak(str, wordDict):
    dp = [False] * (len(str) + 1)  # +1 because we want to store the base condition

    dp[len(str)] = True  # Base condition
    for i in range(len(str) - 1, -1, -1):
        for w in wordDict:  # Comparing each word in the dict with part of the given string
            # if length of part of string is greater than or equal to length of wordDict word
            if (i + len(w)) <= len(str) and str[i:i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]: # if one word from wordDict is found in string, then dont have to compare
                      # with the remaining words of wordDict.
                break

    return dp[0]  # If we reach the begining of the string and
    # True was copied for each detection of matching dict word, then we found all the substrings of string
    # that are present in the wordDict.


#print(wordBreak('neetacode', ['leet', 'neet', 'code']))
dict = ["self", "th", "is", "famous", "Word",
        "break", "b", "r", "e", "a", "k", "br",
        "bre", "brea", "ak", "problem"]
print(wordBreak('Wordbreakabproblem', dict))
