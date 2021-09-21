# Leetcode 17
def letter_combinations_of_phone_pad(nums_string):
    hashmap = {'1': [], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'], 0: []}
    result = []
    helper(nums_string, [], result, 0, hashmap)

    return result


def helper(nums_string, slate, result, idx, hashmap):
    if idx == len(nums_string):
        result.append(''.join(slate))
    elif nums_string[idx] == '1' or nums_string[idx] == '0': # 1 and 0 have no letters attached to it.
        helper(nums_string, slate, result, idx + 1, hashmap) # hence skip that number and proceed to next number
        return
    else:
        for letter in hashmap[nums_string[idx]]:
            slate.append(letter)
            helper(nums_string, slate, result, idx + 1, hashmap)
            slate.pop()


print(letter_combinations_of_phone_pad('123'))
