def reverse_string(input_string):
    strLength = len(input_string);

    reversed_string = []
    for i in range(0, strLength):
        reversed_string.insert(i, input_string[strLength - 1 - i])

    print(str(reversed_string))
    print("".join(reversed_string))


# Time = O(n)
# Space = O(n)
#############################################################################
def swap(string, a, b):
    string = list(string)
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    return "".join(string)


def smarter_way(input_string):
    for i in range(0, len(input_string) // 2):
        input_string = swap(input_string, i, len(input_string) - i - 1)
    return input_string


# Time O(n)
# Space O(1)

# reverse_string('Hi, How are you?')
# print(smarter_way('Hi, How are you?'))


##################################################################################
def simpler_way(input_string):
    input_string = list(input_string)
    reversed_string = input_string[::-1]

    return "".join(reversed_string)


print(simpler_way('Hi, How are you?'))
