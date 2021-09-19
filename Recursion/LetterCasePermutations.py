# Leetcode 784
# Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. You can return the output in any order.

def letterCasePermuatations(input_string):
    result = []
    helper(input_string, [], result)
    return result


def helper(input_string, slate, result):
    if len(slate) == len(input_string):
        result.append(''.join(slate))
    else:
        current_char = input_string[len(slate)]
        if current_char.isalpha():

            slate.append(current_char.upper())
            helper(input_string, slate, result)
            slate.pop()

            slate.append(current_char.lower())
            helper(input_string, slate, result)
            slate.pop()

        else:
            slate.append(current_char)
            helper(input_string, slate, result)
            slate.pop()


print(letterCasePermuatations('a1b2'))

# Time complexity = O(n * 2 ^ n ) ==> There are 2^n leaf nodes, and copying the slate to result is n operation
# Space complexity =  O(n*2^n) ==> 2^n outputs, each of length n. Implicit space complexity = O(n) - Callstack -- height of tree
