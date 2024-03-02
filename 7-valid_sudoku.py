board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

row = {}
column = {}
grid = {}

for r in range(9):
    row[r] = set()
    for c in range(9):
        if c not in column:
            column[c] = set()
        if (r//3,c//3) not in grid:
            grid[(r//3,c//3)] = set()
        
        if board[r][c] == '.':
            continue
        if( board[r][c] in row[r]) or board[r][c] in column[c] or board[r][c] in grid[r//3, c//3]:
            print(False)
        # if board[r][c] in column[c]:
        #     print(False)
        # if board[r][c] in grid[r//3, c//3]:
        #     print(False)
        else:
            row[r].add(board[r][c])
            column[c].add(board[r][c])
            grid[(r//3,c//3)].add(board[r][c])

print(row)
print(column)
print(grid)

