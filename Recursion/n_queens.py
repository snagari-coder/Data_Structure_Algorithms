# Leetcode 51
# given the size of the board, return all the possible positions of n queens without conflict.
def n_queens(n):
    result = []
    helper(n, [], result)
    return result


def helper(n, slate, result):
    if not is_valid(slate):
        return
    elif len(slate) == n:
        result.append(slate.copy())
        return
    else:
        for idx in range(n):
            slate.append(idx)
            helper(n, slate, result)
            slate.pop()


def is_valid(slate):
    if len(slate) <= 1:
        return True
    # index of slate is the row of board
    # value at the index is the column of the board
    # new_row and new_column are after the insertion of the latest queen on the board
    new_row = len(slate) - 1
    new_column = slate[new_row]

    for old_row in range(len(slate) - 1):
        old_col = slate[old_row]
        if old_col == new_column:
            return False # queens can't be on the same column

        if abs(old_col-new_column) == abs(old_row-new_row): # checking the diagonal
            return False

    return True

print(n_queens(4))
