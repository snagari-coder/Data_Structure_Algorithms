def check_common_element(list1, list2):
    length1 = len(list1)
    length2 = len(list2)
    hash_map = {}
    result = 0
    if length1 > length2:
        for i in range(0, length1):
            hash_map.update({list1[i]: 1})

        print(hash_map)
        for j in range(0, length2):
            if list2[j] in hash_map:
                result = 1

        if result == 0:
            print("does not contain")
        else:
            print("contains")
    else:
        for i in range(0, length2):
            hash_map.update({list2[i]: 1})

        for j in range(0, length1):
            if list1[j] in hash_map:
                result = 1
        if result == 0:
            print("does not contain")
        else:
            print("contains")


check_common_element(['a', null, 'c', 'x'], ['a', null, 'r'])
