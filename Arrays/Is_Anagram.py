# Check if two strings are anagram or not.
# Anagram is if two strings have same letters, but are rearranged.
# Ex: C A T and A C T are Anagram.

def IsAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    hashmap = {}
    for ele in s1:
        if ele not in hashmap:
            hashmap[ele] = 1
        else:
            hashmap[ele] += 1
    print(hashmap)

    for ele in s2:
        if ele not in hashmap:
            return False
        else:
            hashmap.popitem()

    if len(hashmap) != 0:
        return False
    else:
        return True

print(IsAnagram('CAD', 'DAC'))


======================================================================================================================================
def is_anagram(string1,string2):
    list1 = list(string1) # You don't really have to convert to list. You can do the same thing with string.
    list2 = list(string2)

    hashmap = {}

    if len(list1) != len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i] in hashmap:
                hashmap[list1[i]] = hashmap[list1[i]] + 1
            else:
                hashmap[list1[i]] =  1
        print(hashmap)

        for i in range(len(list2)):
            if list2[i] not in hashmap:
                return False
            else:
                hashmap[list2[i]] = hashmap[list2[i]] - 1
        print(hashmap)
        for key,value in hashmap.items():
            if value != 0:
                return False
            else:
                return True
#print(is_anagram("silent", "listen"))
print(is_anagram("letter", "teller"))
# Time complexity = O(n)
# Space complexity = O(n)
