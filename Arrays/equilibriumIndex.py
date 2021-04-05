# Write a function int equilibrium(int[] arr, int n); that given a sequence arr[] of size n,
# returns an equilibrium index (if any) or -1 if no equilibrium indexes exist.

def equilibriumIndex(arr):
    n = len(arr)
    sum = 0
    left_sum = 0
    for i in range(n):
        sum += arr[i]
    i = 1
    while i < n:
        left_sum += arr[i - 1]
        right_sum = sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        else:
            i = i + 1
    return -1


print("Equilibrium index is: ", equilibriumIndex([-7, 1, 2, -4, 3, -5]))
print("Equilibrium index is: ", equilibriumIndex([-7, 1, 5, 2, -4, 3, 0]))
