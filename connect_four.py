from board import Board  # Import the class from the other file


player_in = ""

valid_commands = ["1","2","3","4","5","6","7","e","exit"]

print("Starting game...")

game_board = Board()


#get commands
def is_valid_input(_in):
    return _in in valid_commands


#get inputs
while True:

    #playing game
    game_board.print_board()
    


    player_in = input("Enter your move:").strip().lower()

    if not is_valid_input(player_in):
        print("Invalid input")
        continue

    if player_in in ["e", "exit"]:
        print("Exiting...")
        break
    
    if game_board.is_move_valid(int(player_in) - 1):
        game_board.play_move(int(player_in) - 1)
        winner = game_board.check_game_win()

        if winner != None:
            game_board.print_board()
            print(winner + " Wins!")
            break
    

    
    

    

print("Game over")