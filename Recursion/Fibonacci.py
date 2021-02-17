# Given a number index N return the Fibonacci value of the sequence
# Sequence == 0,1,1,2,3,5,8,13,21,34,55,89

def fib_recursive(n):
    if n < 2:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    array = [0, 1]
    for i in range(2, n + 1):
        array.append(array[i - 1] + array[i - 2])
    return array[n]


print(fib_recursive(8))
print(fib_iterative(11))
