def pascalsTriangle(numRows):
    rows = numRows
    table = [[1 for j in range(x+1)] for x in range(rows)] # each row has different columns
    for row in range(2,len(table)):
        for col in range(1,len(table[row])-1):
            table[row][col] = table[row-1][col-1] + table[row-1][col]
    for row in range(len(table)):
        print(table[row])

pascalsTriangle(5)
