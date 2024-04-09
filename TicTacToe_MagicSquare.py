import random

board=[" " for x in range (9)]
print("X is the 1st player.")
print("O is the 2nd player.")
player=input("enter a symbol 'X' or 'O':")
cmp="O" if player=="X" else "X"
slots_avl=[0,1,2,3,4,5,6,7,8]
magicSquare=[2,7,6,9,5,1,4,3,8]
p_turns=0
c_turns=0

def print_board():
    print(board[0],"|",board[1],"|",board[2])
    print("---------")
    print(board[3],"|",board[4],"|",board[5])
    print("---------")
    print(board[6],"|",board[7],"|",board[8])
    print("---------")

def print_winner(v):
    if v==player:
        print("Congrats you have won!!")
    else:
        print("Bot won, Try again...")

def players_turn():
    global p_turns
    place=int(input("enter a index to place the symbol:"))
    if(place not in slots_avl):
        print("Invalid input. Please choose an empty slot.")
        return players_turn()
    board[place]=player
    slots_avl.remove(place)
    p_turns=p_turns+1
    print_board()
    if(not winner() and not is_full()):
      print("Computers turn:")
      cmp_turn()

def cmp_choice():
    place=random.choice(slots_avl)
    board[place]=cmp
    slots_avl.remove(place)
    
def cmp_move():
    global c_turns
    for i in range(9):
        if(board[i]==cmp):
            for j in range(9):
                if(board[i]==board[j]):
                    num=15-magicSquare[i]-magicSquare[j]
                    if(num in [1,2,3,4,5,6,7,8,9]):
                        place=magicSquare.index(num)
                        if(place in slots_avl):
                            board[place]=cmp
                            slots_avl.remove(place)
                            c_turns+=1
                            return
    for i in range(9):
        if(board[i]==player):
            for j in range(9):
                if(board[i]==board[j]):
                    num=15-magicSquare[i]-magicSquare[j]
                    if(num in [1,2,3,4,5,6,7,8,9]):
                        place=magicSquare.index(num)
                        if(place in slots_avl):
                            board[place]=cmp
                            slots_avl.remove(place)
                            c_turns+=1
                            return
    cmp_choice()
    return

def cmp_turn():
    global c_turns
    if(p_turns<2 and c_turns<2):
        cmp_choice()
        c_turns+=1
    else:
        cmp_move()
    print_board()
        
    if(not winner() and not is_full()):
      players_turn()

def is_full():
    if all(cell != " " for cell in board):
        print("It's a Draw.")
        return True
    return False

def winner():
    for i in [0,3,6]:
      if(board[i]==board[i+1]==board[i+2]!=" "):
        print_winner(board[i])
        return True
    for i in range(3): 
      if(board[i]==board[i+3]==board[i+6]!=" "):
        print_winner(board[i])
        return True
    if(board[0]==board[4]==board[8]!=" "):
        print_winner(board[0])
        return True
    if(board[2]==board[4]==board[6]!=" "):
        print_winner(board[2])
        return True

def TicTacToe():
    if(player=="X"):
        players_turn()
    else:
        cmp_turn()


TicTacToe()
