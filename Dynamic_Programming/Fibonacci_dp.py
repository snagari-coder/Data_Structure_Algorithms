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


def fibonacci_dp_norecursion(n):
    answer_list = []
    answer_list.insert(0, 0)
    answer_list.insert(1, 1)
    for i in range(2, n + 1):
        global calculations
        calculations = calculations + 1
        answer_list.insert(i, answer_list[i - 1] + answer_list[i - 2])
    return answer_list[n]


print(fibonacci(10), calculations)
print(fibonacci_dp(10), calculations)
print(fibonacci_dp_norecursion(10), calculations)
