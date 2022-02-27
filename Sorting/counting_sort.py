def counting_sort(inp, max_value):
    count = [0] * (max_value + 1)

    for value in inp:
        count[value] += 1
    output = []
    for i in range(len(count)):
        curr_count = count[i]

        for x in range(curr_count):
            output.append(i)

    return output


print(counting_sort([1, 4, 1, 2, 7, 5, 2], 9))


def counting_sort_hash(inp, max_value):
    count = {}
    for val in inp:
        count[val] = 1 + count.get(val, 0)
    print(count)
    output = []
    for i in range(max_value + 1):
        curr_count = count[i] if i in count else 0
        for x in range(curr_count):
            output.append(i)
    return output


print(counting_sort_hash([1, 4, 1, 2, 7, 5, 2], 9))

# Time = O(n^2)
# Space = O(n)
