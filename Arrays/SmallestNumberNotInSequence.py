#Find the smallest positive integer that does not occur in a given sequence
def solution(A):
    # write your code in Python 3.6
    A = list(set(A))
    A.sort()
    print(A)
    res = all(ele > 0 for ele in A)
    if res is False:
        return 1
    else:

        for i in range(len(A)):
            if i+1 != A[i]:
                return i+1

        return A[len(A)-1]+1



print(solution([1,2,3]))
