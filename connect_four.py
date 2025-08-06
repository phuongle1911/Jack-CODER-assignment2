import random
import os

from board import Board  # Import the class from the other file
from human_player import Human_player
from player import Player
from monte_carlo_player import Monte_carlo_player



#os clearing
def clear():
    #clear the terminal based on os used
    os.system("cls" if os.name in ('nt', 'dos') else "clear")


def refresh_gamestate(board):
    clear()
    board.print_board()

def choose_players(board):
    player = []
    #lambda for delaying object creation
    choices = {
        "1": lambda: Human_player(board),
        "2": lambda: Player(board),
        "3": lambda: Monte_carlo_player(board,250),
        "4": lambda: Monte_carlo_player(board,750),
        "5": lambda: Monte_carlo_player(board,1500)
    }
    
    while len(player) < 2:

        print(f"""Select Player {len(player) + 1}:
    1. Human (same machine)
    2. Randobot
    3. Normal AI
    4. Hard AI
    5. Impossible AI         
e/exit: stop playing
""")
        choice = input(f"Select Player {len(player) + 1}: ").strip().lower()
        if choice == "e" or choice == "exit":
            return False
        if choice in choices:
            player.append(choices[choice]())
            clear()
        else:
            print("Invalid choice.")
    return player

def play_game():
    """
    Starts and runs a single game of Connect Four.
    
    this function:
    - Creates a new game board
    - lets the user select two players (human or AI)
    - randomises which player goes first
    - Alternates turns between players
    - Continues the game loop until theres a win, draw or player exit
    - At the end asks the user if they want to play again
    
    Returns:
     bool: True if the user wants to play again. False if not
     
    Example usage:
     while play_game():
         continue  #keeps restating the game if the user wants to play again 'y'
     
     """
    print("\nStarting new game... \n")
    game_board = Board() # Create a new game board

    player = choose_players(game_board) # Ask the user to choose players

    if player == False:
        return False  #Player chose to exit the game
    
    # Randomise who goes first
    starting_turn = [0,1]
    random.shuffle(starting_turn)

    # Assign turn indexes to symbols (e.g X goes second O goes first)
    turn_order = dict(zip(['X', 'O'], starting_turn)) 

    # Determines which players turn it is based on game_board current state
    turn_index = turn_order[game_board.get_current_turn()]
    
    # Clear screen and print the current board 
    refresh_gamestate(game_board)

    # game loop: this will continue until a win, draw or player quits
    while True:
        print(f"{game_board.get_current_turn()}'s turn: \n") # show whose turn it is

        desired_move = player[turn_index].get_move() # Ask current player for their move

        if desired_move == "e": #Player typed 'e' or 'exit' to quit
            break # Exit the game loop
            
        if type(desired_move) is int: # If the move is a number (valid column index)
            if game_board.is_move_valid(desired_move): # Check if the move is valid

                game_board.play_move(desired_move) # drop the piece in the board
                turn_index = turn_order[game_board.get_current_turn()] # Switch to the next player
                player[turn_index].update_board(game_board) # Let the next player see the updated board state
                winner = game_board.check_game_win() # Check if there's a winner or draw

                refresh_gamestate(game_board) # Clear the screen and print the updated board


                if winner == "draw": # No more valid moves left, it's a draw
                    print("Tie!")
                    break

                if winner != None:
                    print(winner + " Wins!")
                    break
    #Ask user if the want to play again 
    return input("Play again? (y/n): ").strip().lower().startswith("y")

    
while play_game():
    continue

