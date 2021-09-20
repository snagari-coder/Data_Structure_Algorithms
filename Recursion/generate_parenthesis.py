# Leetcode 22

def generate_parenthesis(n):
    result = []
    helper(n, 0, 0, [], result)
    return result


def helper(n, num_open, num_closed, slate, result):
    if num_closed > num_open:
        return
    elif num_closed > n:
        return
    elif num_open > n:
        return
    elif num_closed == num_open == n:
        result.append(''.join(slate))
    else:
        slate.append('(')
        helper(n, num_open + 1, num_closed, slate, result)
        slate.pop()

        slate.append(')')
        helper(n, num_open, num_closed + 1, slate, result)
        slate.pop()

print(generate_parenthesis(3))
