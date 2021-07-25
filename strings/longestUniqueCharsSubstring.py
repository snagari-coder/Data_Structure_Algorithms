# Given a string, find length of the longest substring and subsequence with
# all distinct characters.
# For example, for input "abca",
# the output is 3 as "abc" is the longest substring and subsequence with all distinct characters.
# For example, for input "pwwkew"
# Substring = wke, subsequence = pwke

def longestSubstringWithAllDistinceChars(str):
    # Sliding window method
    start, end = 0, 0
    max_length = 0
    seen_hashmap = {}
    for end in range(len(str)):
        if str[end] in seen_hashmap:
            # If the char has already been seen, move the start position
            # to position after the last occurrence.
            start = max(start, seen_hashmap[str[end]] + 1)

        # Updating the last seen value of the character
        seen_hashmap[str[end]] = end
        max_length = max(max_length, end - start + 1)
    print("The max length of substring with unique chars is: ", max_length)
    print("The substring is: ", str[start:end + 1])
    return
longestSubstringWithAllDistinceChars("pwwkew")


# Time complexity = O(n)
# Space complexity = O(n)

def longestSubsequenceWithAllDistinctChars(str):
    hashmap = {}
    Subsequence = []
    for i in range(len(str)):
        if str[i] in hashmap:
            hashmap[str[i]] += 1
        else:
            hashmap[str[i]] = 1
            Subsequence.append(str[i])
    print("The max length of subsequence with unique chars is: ", len(Subsequence))
    print("The substring is: ", "".join(Subsequence))
    return


longestSubsequenceWithAllDistinctChars("pwwkew")
# Time complexity = O(n)
# Space complexity = O(n)
