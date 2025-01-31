# import random module
import random

# Function to display the board
def print_board(board):
    for row in board:
        print("|".join(row)) # prints the rows with separators
        print("-"*9) # prints seperator after each row

# Checking for winner or draw
def check_winner(board):
    winning_combinations = [[0,1,2],[3,4,5],[6,7,8], # rows combinations possible for win 
                            [0,3,6],[1,4,7],[2,5,8], # columns combinations possible for win
                            [0,4,8],[2,4,6]] # diagonals combinations possible for win 
    
    for combo in winning_combinations:
        values = [board[i//3][i%3] for i in combo] # Exact values (X/O)
        if values == ['X','X','X']: # if all values are "x" then player win 
            return "You win"
        elif values == ['O','O',"O"]: # if all values are "O" the computer wins
            return "Computer Wins"
        
    if all(cell != " " for row in board for cell in row): # If all the cells are filled (" " are not found) and their is no winner then its a draw
        return "Its a draw"
        
    return None # Game is still going on
    
# Taking the players move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move between (0-8): ")) # Asks the player to enter a number between 0-8 as input
            if move<0 or move>8 or board[move//3][move%3] != ' ': # Checks if move is valid and the position is not already occupied
                print("Invalid move, try again")
            else:
                board[move//3][move%3] = "X" # Players move for example if player enter 5 then 5//3=1 and 5%3==2 therefore "X' is printed at (1,2)
                break
        except ValueError:  # If player enter invalid choice
            print("Enter a valid number between 0 and 8")

# Making the computers move
def computer_move(board):
    empty_cells = [i for i in range(9) if board[i//3][i%3]==" "] # Finds all the empty spaces in the grid
    if empty_cells:
        move = random.choice(empty_cells) # Picks randomly empty spots for the computer from the empty spots 
        board[move//3][move%3] = "O" # Computer places O

# Running the game
def play_game():
    board = [[' ' for i in range (3)] for i in range(3)] # Creates a 3x3 board
    print_board(board) # Display the empty board

    for turn in range (9): # Max of 9 moves
        if turn%2==0:   # Player's turn (Even turns 0,2,4,6,8)
            player_move(board)
        else:           # Computer's turn (Odd turns 1,3,5,7)
            computer_move(board)

        print_board(board) # Prints the updated board after every move
        result = check_winner(board) # Check if somone win or its a draw and prints results accordingly
        if result:
            print(result)
            return

        print("Its a draw") # if all the 9 moves are made and no one wins then its a draw

# Running the game
play_game()

        print("Its a draw") # if all the 9 moves are made and no one wins then its a draw

# Running the game
play_game()
