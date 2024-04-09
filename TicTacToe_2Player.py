def print_board(board):
    for row in board:
        print("|".join(row))
        print("_"*6)

def ch_winner(board):
    for row in board:
        if(len(set(row))==1 and row[0]!=" "):
            return row[0]
    for col in range(3):
        if(board[0][col]==board[1][col]==board[2][col]!=" "):
            return board[0][col]
    if(board[0][0]==board[1][1]==board[2][2]!=" "):
        return bord[0][0]
    if(board[0][2]==board[1][1]==board[2][0]!=" "):
        return board[1][1]
    return None

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def play_TicTacToe():
    player = "X"
    board=[[" " for _ in range(3)]for _ in range(3)]
    while(True):
        print()
        print_board(board)
        print(f"player {player} turn")
        row = int(input("enter a row in (0,1,2):"))
        col = int(input("enter a col in (0,1,2):"))
        print()
        if(board[row][col]==" "):
            board[row][col]= player
            winner = ch_winner(board)
            if(winner):
                print_board(board)
                print(f"{player} won the game")
                break
            elif(is_board_full(board)):
                print("It's a draw")
                break
            player = "O" if player == "X" else "X"
        else:
            print("Cell is already occupied. try again:")

if __name__=="__main__":
    play_TicTacToe()
            
            
                  
