# Print 2D array diagonally from lower-left to upper-right
def twod_diagonal_print(arr, m, n):
    r = m #row
    c = n #column
    for k in range(0,r):
        i = k
        j = 0
        print(" ")
        while i >= 0: # Each diagonal ends with the 0th row
            print(arr[i][j], end=" ")
            i = i - 1
            j = j + 1

    for k in range(1,c):
        i = r - 1
        j = k
        print(" ")
        while j <= c - 1: #Each diagonal ends with the last ( c - 1 )th column
            print(arr[i][j], end=" ")
            i = i - 1
            j = j + 1

array = [[00,1,2,3,4],
         [10,11,12,13,14],
         [20,21,22,23,24],
         [30,31,32,33,34]]
twod_diagonal_print(array, 4, 5)

#Time complexity = O(m*n)
