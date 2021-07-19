# Given two list of strings, find a list of common strings between the input lists.
# Ex: list1 = ["dog", "cat", "tiget", "elephant"],list2 = ["horse", "dog", "cow", "cat"], result = ['dog', 'cat']
def find_common_animals(list1, list2):
    hashmap = {}
    common_animals = []
    for animal in list1:
        hashmap[animal] = 1

    for animal in list2:
        if animal in hashmap:
            hashmap[animal] = hashmap[animal] + 1

    for key,value in hashmap.items():
        if value == 2:
            common_animals.append(key)

    return common_animals
#Time complexity = O(n)
#Space complexity = O(n)
print(find_common_animals(["dog", "cat", "tiget", "elephant"],["horse", "dog", "cow", "cat"]))
##########################################################################################################################


def find_common_string(list1, list2):
    hashmap = {}
    result = []
    for i in range(len(list1)):
        if list1[i] in hashmap:
            hashmap[list1[i]] += 1
        else:
            hashmap[list1[i]] = 1
    print(hashmap)
    for i in range(len(list2)):
        if list2[i] in hashmap:
            result.append(list2[i])
            hashmap.pop(list2[i])
    print(hashmap)
    return result
print(find_common_string(["dog", "cat", "tiget", "elephant"],["horse", "dog", "cow", "cat"]))




###########################################################################################################################

def find_common_animals_with_sets(list1, list2):
    common_animals = set(list1) & set(list2)
    print(list(common_animals))
#Time complexity = O(min(len(list1),len(list2)))
#Space complexity = less than or equal to min(len(list1),len(list2))
find_common_animals_with_sets(["dog", "cat", "tiget", "elephant"],["horse", "dog", "cow", "cat"])
