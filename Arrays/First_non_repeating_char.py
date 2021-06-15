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
