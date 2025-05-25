from board import Board  # Import the class from the other file



running_game = True

while running_game:
    print("Starting new game...")
    game_board = Board()

    #selecting your opponent
    playing_game = True
    while True:

        print("""Select Opponent:
    1. Human (same machine)
    2. Easy AI
    3. Normal AI
    4. Hard AI
e/exit: stop playing""")
        
        
        match (input("Enter Opponent: ").strip().lower()):
            case "1": 
                break
            case "2": 
                break
            case "3": 
                break
            case "4": 
                break
            case "e": 
                playing_game = False
                break
            case "-":
                continue
    
        
    
    #Playing the game
    while playing_game:
        #playing game
        game_board.print_board()
        
        turn = game_board.get_current_turn()

        player_in = input(turn+"'s turn\nEnter a move:").strip().lower()

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
    

    #Game is over
    if playing_game:
        print("Game over")
        #print score here if needed

        #Ask to play another game


    else:
        running_game = False

    

