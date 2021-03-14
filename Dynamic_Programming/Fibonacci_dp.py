# Fibonacci series = [0,1,1,2,3,5,8,13,21,34,55]
ans_list = []
ans_list.insert(0, 0)
ans_list.insert(1, 1)
calculations = 0


def fibonacci(n):
    global calculations
    calculations = calculations + 1
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_dp(n):
    global calculations
    calculations = calculations + 1
    if n < 2:
        return ans_list[n]
    else:
        ans_list.insert(n, fibonacci_dp(n - 1) + fibonacci_dp(n - 2))
        return ans_list[n]


print(fibonacci(10),calculations)
print(fibonacci_dp(10),calculations)
