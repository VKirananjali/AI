def print_board(board):
    for row in board:
        for ele in row:
            print(ele, end=" ")
        print()
        print("---------------")
        
def isSafe(board,row,col):
    for i in range(col):
        if(board[row][i]==1):
            return False
    x=row
    y=col
    while(x>=0 and y>=0):
        if(board[x][y]==1):
            return False
        x=x-1
        y=y-1
        
    x=row
    y=col
    while(x<N and y>=0):
        if(board[x][y]==1):
            return False
        x=x+1
        y=y-1
    return True

def solveNQueen(board,col):
    if(col==N):
        print_board(board)
        return True
    for i in range (N):
        if isSafe(board,i,col):
            board[i][col]=1
            if solveNQueen(board,col+1):
                return True
            board[i][col]=0
    return False

N=8
board=[[0 for x in range(N)]for y in range(N)]
if(not solveNQueen(board,0)):
    print("not solvable")
