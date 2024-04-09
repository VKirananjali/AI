def is_valid(matrix, row, col, num):
    for i in range(3):
        if matrix[row][i] == num or matrix[i][col] == num:
            return False
    return True

def print_board(matrix):
    for row in matrix:
        for x in row:
            print(x,end=" ")
        print()
        print("------")

def solve_matrix(matrix, row, col):
    if(isFull(matrix)):
        print_board(matrix)
        matrix[2][2]=0
        print("\n")
        return 
    next_row = (row + 1) % 3
    next_col = col + 1 if next_row == 0 else col
    
    for num in range(1, 4):
        if is_valid(matrix, row, col, num):
            matrix[row][col] = num
            if solve_matrix(matrix, next_row, next_col):
                return True
            matrix[row][col] = 0  
    
    return False

def isFull(board):
    return all(all(cell != 0 for cell in row)for row in board)

matrix = [[0] * 3 for _ in range(3)]
solve_matrix(matrix, 0, 0)
