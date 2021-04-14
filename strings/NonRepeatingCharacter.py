#Implement a function that takes a string and returns the first character that does not appear twice or more.
#If there is no non-repeating character, return None

# Implement your function below.
def non_repeating(given_string):
    n = len(given_string)
    hashmap = {}
    for i in range(n):
        if given_string[i] in hashmap:
            hashmap[given_string[i]] =  hashmap[given_string[i]] + 1
        else:
             hashmap[given_string[i]] = 1
    key_list = list(hashmap.keys())
    value_list = list(hashmap.values())
    if 1 in value_list:
        position = value_list.index(1)
        non_repeating = key_list[position]
        return non_repeating
    else:
        return None
    

# NOTE: The following input values will be used for testing your solution.
non_repeating("abcab") # should return 'c'
non_repeating("abab") # should return None
non_repeating("aabbbc") # should return 'c'
non_repeating("aabbdbc") # should return 'd'
