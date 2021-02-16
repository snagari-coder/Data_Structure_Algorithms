def factorial_recursion(num):
    if num <= 1:
        return 1
    else:
        return num * factorial_recursion(num - 1)


def factorial_iterative(num):
    i = 0
    result = 1
    if num <= 1:
        return 1
    else:
        while i < num:
            result = result * (num - i)
            i = i + 1
        return result


print(factorial_recursion(5))
print(factorial_iterative(5))
