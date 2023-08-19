print("Welcome to Tic-Tac-Toe by Marcos Sardina and the pig!Abit of the pig...")
import random


def draw_line(line):
    """
    Draws one line of play
    
    line is a list [ p1, p2, p3] where p1, p2, p3 are 0, -1 or 1 (0 for blank)    
    """
    if  line[0] == 0:   # p1
        play_1 = " "
    elif line[0] == 1:
        play_1 = "X"
    else:
        play_1 = "O"

    if line[1] == 1:    # p2
        play_2 = "X"
    elif line[1] == 0:
        play_2 = " "
    else:
        play_2 = "O"
    
    if line[2] == -1:
        play_3 = "O"
    elif line[2] == 1:
        play_3 = "X"
    else:
        play_3 = " "   


    print(f" {play_1}  |  {play_2} | {play_3} ")
    
def get_cell(move):
    # get the line index of the move
    pos = (0, 0 )
    if move in [1,2,3]:
        pos = (0, move -1)
    if move in [4,5,6]:
        pos = (1, move -4)
    if move in [7, 8, 9]:
        pos = (2 , move -7)
    return pos

def draw_board(plays):
    print()
    draw_line(plays[0])
    print("--------------")
    draw_line(plays[1])
    print("--------------")
    draw_line(plays[2])

def winner_move(board, player):
    # returns the cell no 1 to 9 that player can win on board
    # if none, returns 0
    return 0


def computer_play(board):
    """ 
    This is called when player = -1

    Returns a number betwen 1 and 9
    """
    move = winner_move(board, 1) # move is a winner move for player 1 (human)
    if move > 0:
        # move is the cell that player 1 can play to win
        print("Something of this cool!")
    else:
        computer_move = random.randint(1, 9)
        return computer_move


def player_move(n, board): 
    good_move = False
    while not good_move:
        if n == 1:
            move = int(input(f"Hey! Player {n} where do you want to move (1-9)? "))
        else:
            move = computer_play(board) 
        row, col = get_cell(move)
        # check if move in board
        # check that the move has not been played already
        if board[row][col] == 0:
            # now we play... in line_index in line.
            board[row][col] = n
            good_move = True
        else:
            if n == 1:

                print("That spot has been taken!")
                draw_board(board)

        
        

def draw(board):
    for i in range(0, 3):
        if board[0][i] == 0 or board[1][i] == 0 or board[2][i] == 0:
            return False
    return True





def win(board):
    for row in range(0, 3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and not board[row][0] == 0:
            return board[row][0]
    for col in range(0, 3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and not board[0][col] == 0:
            return board[0][col]
        
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and not board[0][0] == 0:
        return board[0][0]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and not board[2][0] == 0:
        return board[2][0]
        


            

# Set the initial board 
game_board = [[0, 0, 0], [0, 0, 0],[0,0,0]]
player = 1
while True:
    #draw the board first
    draw_board(game_board)

    # ask the current playe to move
    player_move(player, game_board)  
    
    player = player * -1
    result = win(game_board)
    if result == 1:
        print("Player 1 wins!")
        draw_board(game_board)
        break
    elif result == -1:
        print("Player 2 wins!")
        draw_board(game_board)
        break     
    elif draw(game_board) == True:
        print("Draw!")
        draw_board(game_board)
        break




print("The game has ended!")