def binary_strings_better(n):
    result = []
    binary_helper(n, [], result)
    return result


def binary_helper(n, slate, result):
    if len(slate) == n:
        # or result.append(slate.copy())
        result.append(" ".join(slate))
    else:
        for ele in [0, 1]:
            # or slate.append(ele)
            slate.append(str(ele))
            binary_helper(n, slate, result)
            slate.pop()

print(binary_strings_better(3))

#Time complexity = O(2^n) = O(branch ^ height of tree )
# Space complexity = O(n) == The number of nodes of the tree
#########################################################################


# print all binary strings of length n
def binary_string(n):
    binary_helper('', n)


def binary_helper(prefix, n):
    # print(len(prefix),n)
    if n == 0:
        print(prefix)
    else:
        binary_helper(prefix + '0', n - 1)
        binary_helper(prefix + '1', n - 1)


# print(binary_string(3))

