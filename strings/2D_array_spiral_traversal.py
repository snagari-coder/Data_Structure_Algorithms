'''
Given a 2D array, print it in spiral form, clockwise
'''


def print_2d_spiral(arr, m, n):
    r, c = 0, 0
    last_row = m - 1
    last_col = n - 1
    while r < last_row and c < last_col:
        for i in range(c, last_col + 1):
            print(arr[r][i], end=" ")
        r += 1
        for i in range(r, last_row + 1):
            print(arr[i][last_col], end=" ")
        last_col -= 1
        for i in range(last_col, c - 1, -1):
            print(arr[last_row][i], end=" ")
        last_row -= 1
        for i in range(last_row, r-1, -1):
            print(arr[i][c], end=" ")
        c += 1


twod_array = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]]

print_2d_spiral(twod_array, 4, 5)

#Time complexity = O(m*n)
#Space complexity = O(1)
 #output =  1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12 
