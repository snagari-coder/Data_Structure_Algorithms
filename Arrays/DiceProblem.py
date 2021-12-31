You have just rolled a dice several times. The N roll results that you remember are described by an array A. 
However, there are F rolls whose results you have forgotten. The arithmetic mean of all the roll results equals M. 
What are the possible results of the missing rolls?
import math

def solution(A, F, M):

# write your code in Python 3.6
all_rolls = len(A) + F
sum_X = (M*all_rolls) - sum(A)       # X is an array we look for, we can calculate the sum of that array
try:
    close_choice = sum_X/F
except ZeroDivisionError:
    return [0]
X = []
if 1 <= close_choice <= 6:
    for n in range(1, F):
        if sum(X) != sum_X:
            X.append(math.floor(close_choice))
    remainder = sum_X - sum(X) 
    if remainder <= 6:
        X.append(remainder)
    else:
        for n in range(0, len(X)):
            if remainder > 6:
                remainder -=1
                X[n] +=1
            else:
                X.append(remainder)
                break
    return X
