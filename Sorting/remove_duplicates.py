def remove_duplicates_unsorted(inp):
    # output = []
    hash = {}
    for val in inp:
        hash[val] = 1 + hash.get(val, 0)
    print(hash)
    return list(hash.keys())


print(remove_duplicates_unsorted([1, 4, 1, 2, 7, 5, 2]))

# Using counting_sort algorithm
def remove_duplicates_sorted(input, max_value):
    count = {}
    for value in input:
        count[value] = 1 + count.get(value, 0)
    print(count)
    output = []

    for value in range(max_value + 1):
        curr_count = count[value] if value in count else 0
        if curr_count > 0:
            output.append(value)
    return output


print(remove_duplicates_sorted([1, 4, 1, 2, 7, 5, 2], 9))
