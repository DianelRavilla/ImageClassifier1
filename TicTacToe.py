# TIC TAC TOE
# "X" for computer
# "O" for user

from random import randrange

def DisplayBoard(board):
  print("\
+-------+-------+-------+\
    \n|       |       |       |\
    \n|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |\
    \n|       |       |       |\
    \n+-------+-------+-------+\
    \n|       |       |       |\
    \n|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |\
    \n|       |       |       |\
    \n+-------+-------+-------+\
    \n|       |       |       |\
    \n|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |\
    \n|       |       |       |\
    \n+-------+-------+-------+")

def EnterMove(board):
    print("\nUser's turn")
    turn = 0
    while turn == 0:
        move = int(input("\nEnter your move: "))
        for columna in range(3):
            for fila in range(3):
                if move == board[columna][fila]:
                    board[columna][fila] = "O"
                    turn = 1     
    return board
                
def DrawMove(board):
    print("\nComputer's turn\n")
    turn = 0
    while turn == 0:
        move = randrange(10)
        for columna in range(3):
            for fila in range(3):
                if move == board[columna][fila]:
                    board[columna][fila] = "X"     
                    turn = 1
    return board

def MakeListOfFreeFields(board):
    free = []
    for columna in range(3):
        for fila in range(3):
            if not(board[columna][fila] == "X" or board[columna][fila] == "O"):
                free.append(board[columna][fila])
    return free

def VictoryFor(board, sign):
    if board[0][0] == board[0][1] == board[0][2] == sign \
        or board[1][0] == board[1][1] == board[1][2] == sign \
        or board[2][0] == board[2][1] == board[2][2] == sign \
        or board[0][0] == board[1][0] == board[2][0] == sign \
        or board[1][0] == board[1][1] == board[1][2] == sign \
        or board[2][0] == board[2][1] == board[2][2] == sign \
        or board[0][0] == board[1][1] == board[2][2] == sign \
        or board[0][2] == board[1][1] == board[2][0] == sign:        
        if sign == "X":
            print("Computer WINS!")
        elif sign == "O":
            print("You WIN!")
        return True
    else:
        return False                     

# Creation of the empty board
board = [[0 for i in range(3)] for j in range(3)]
num = 0
for i in range(3):
    for j in range(3):
        num += 1
        board[i][j] = num

DisplayBoard(board)

turn = 0
while not(VictoryFor(board, "X") or VictoryFor(board, "O")):
    print(len(MakeListOfFreeFields(board))," spaces left")
    if len(MakeListOfFreeFields(board)) > 0:
        if turn == 0:
            DisplayBoard(DrawMove(board))
            turn = 1
            continue
        if turn == 1:
            DisplayBoard(EnterMove(board))
            turn = 0
            continue
    else:
        print("EMPATE!")
        break 
# ARCHIVO DE PRUEBA

    
