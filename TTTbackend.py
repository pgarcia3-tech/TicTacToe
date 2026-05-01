
## BASIC BACKEND!
# IDEAS:
    # computer "thinks" before moving 
    # 

import random

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

# list of lists like a 2D array

# initializing the game_state variables!
game_over = False
winner = None 
player = "X" # user is X
computer = "O"
CELL_SIZE = 150

player_score = 0 
computer_score = 0
ties = 0

#function to reset the game 

def reset_game():
    global board, game_over, winner

    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
    
    game_over = False
    winner = None

#for every win, loss, tie, update score
def update_score(result):
    global player_score, computer_score, ties
    if result == player:
        player_score += 1
    elif result == computer:
        computer_score +=1
    elif result == "Tie":
        ties += 1

#check for a winner 
def check_winner():
    for row in board: #check row for row 
        if row[0] == row[1] == row[2] != "":
            return row [0] #return either X or O

    for col in range(3): # check column for column
        if board[0][col] == board [1][col] == board[2][col] != "":
            return board[0][col] #value in column 

    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]

    if board[0][2] == board [1][1] == board[2][0] != "":
        return board[0][2]

    for row in board: #is the row full?
        if "" in row:
            return None

    return "Tie" #check for tie

#computer makes first move
def computer_move():
    empty_spaces = []
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                empty_spaces.append((row, col))

    if empty_spaces:
        row, col = random.choice(empty_spaces)
        board[row][col] = computer
        print("Computer moved: ", row, col)



#convert mouse click
def handle_click(pos):
    global winner, game_over
    x, y = pos

    board_x = 25 # left edge of the board
    board_y = 75 # top of the board

    #is the click inside the board?
    if board_x <= x <= board_x + 450 and board_y <= y <= board_y + 450:

        col = (x - board_x) // CELL_SIZE
        row = (y - board_y) // CELL_SIZE #dont really understand this, the logic

        print("Clicked:", row, col)

        #if empty, place an X

        if board[row][col] == "" and not game_over:
            board[row][col] = player

            result = check_winner()
            if result is not None:
                winner = result
                game_over = True
                update_score(result)
                print("Game Over: ", winner)
                print("Player Score: ", player_score)
                print ("Computer Score: ", computer_score)
                print ("Ties Score: ", ties)
                return 

            computer_move()

            result = check_winner()
            if result is not None:
                winner = result
                game_over = True
                update_score(result)
                print("Game Over: ", winner)
                print("Player Score: ", player_score)
                print ("Computer Score: ", computer_score)
                print ("Ties Score: ", ties)
                return

