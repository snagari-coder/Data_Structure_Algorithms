# Given an input stream of n characters consisting only of small case alphabets the task is to find the first
# non repeating character each time a character is inserted to the stream. If no non repeating element is found print -1.
#Example
# Flow in stream : a, a, b, c
# a goes to stream : 1st non repeating element a (a)
# a goes to stream : no non repeating element -1 (a, a)
# b goes to stream : 1st non repeating element is b (a, a, b)
# c goes to stream : 1st non repeating element is b (a, a, b, c)

from collections import OrderedDict

def first_non_repeating_char(input):
    input_stream = input
    hashmap = OrderedDict()
    firstNonRecurringChar = input_stream[0]
    for char in input_stream:
        print("Reading "+ char + " from input stream")
        if char not in hashmap:
            hashmap[char] = 1
        else:
            hashmap[char] = hashmap[char] + 1
        #print(hashmap)

        if hashmap[firstNonRecurringChar] != 1:
            for key,value in hashmap.items():
                #print("key, value : ", key, value)
                if value == 1:
                    firstNonRecurringChar = key
                    print("firstNonRecurringChar so far is: : ", firstNonRecurringChar)
                    break
                elif value != 1:
                    print("There is no non-repeating char in the given sequence")
                    return -1
        else:
            print("firstNonRecurringChar so far is: ", firstNonRecurringChar)
#first_non_repeating_char("geekforgeekandgeeksandquizfor")
first_non_repeating_char("ababab")
# Time complexity = O(1) Looking up from hashmap
# Space complexity = O(n)

==========================================================================================================================================================================
===== SIMPLER VERSION ====================================================================================================================================================

from collections import OrderedDict


def first_non_repeating_char(str):
    n = len(str)
    hashmap = OrderedDict()

    for i in range(n):
        print(f'Reading the char {str[i]}')
        if str[i] in hashmap:
            hashmap[str[i]] += 1
        else:
            hashmap[str[i]] = 1

        key = value_one(hashmap)
        print(f'First non repeating char is {key}')

    return


def value_one(hashmap):
    for key, value in hashmap.items():
        if value != 1:
            continue
        else:
            return key

    return -1
first_non_repeating_char('aabc')

first_non_repeating_char('aabcbc')

# Time complexity = O(n) + O(1) going through the string and lookup from hashmap
# Space complexity = O(m), m < n, number of unique chars
