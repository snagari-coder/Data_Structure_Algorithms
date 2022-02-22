# Leetcode 5
# Better
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_length = 0
        #algo: Two ways:
        # 1. check first and last char, and move inwards
        # 2. select a middle, and check chars on both sides of middle, and move outwards
        # Here I am using the second algo
        for i in range(len(s)):
            
                #For even length string
                l,r=i,i+1
                while l >=0 and r < len(s) and s[l] == s[r]:
                    if (r-l+1) > result_length:
                        result = s[l:r+1]
                        result_length = (r-l+1)
                    l -= 1 #going outwards
                    r += 1                    

                #For odd length string
                l,r = i,i
                while l >=0 and r < len(s) and s[l] == s[r]:
                    if (r-l+1) > result_length:
                        result = s[l:r+1]
                        result_length = (r-l+1)
                    l -= 1 #going outwards
                    r += 1
        return result


#####################################################################################################################################################
# Given a string S, find the longest palindromic substring in S

def longest_paliandromic_substring(string):
    length = len(string)
    start,low,high = 0,0,0
    max_length = 1
    for i in range(1,length):
        # For even length substring
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

        # For odd length substring
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

    print("Max length paliandromic substring is: ")
    print(string[start:start+max_length])
    print("Maxlength of this paliandrom is: ", max_length)

longest_paliandromic_substring('babad')
