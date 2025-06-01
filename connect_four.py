from board import Board  # Import the class from the other file
from human_player import Human_player
from player import Player


import random
import os

#os clearing
def clear():
    if os.name in ('nt', 'dos'):
        os.system("cls")
    elif os.name in ('linux', 'osx', 'posix'):
        os.system("clear")
    else:
        print("\n" * 120)



running_game = True

while running_game:
    print("Starting new game...")
    print()
    game_board = Board()

    player = []
    
    #selecting your opponent
    playing_game = True
    while len(player) != 2:

        print("""Select Opponent:
    1. Human (same machine)
    2. Randobot
    3. Normal AI
    4. Hard AI
e/exit: stop playing
              """)
       
        
        match (input("Select Player " + str(len(player) + 1) + ": ").strip().lower()):
            case "1": 
                player.append(Human_player(game_board))
            case "2": 
                player.append(Player(game_board))
            case "3": 
                print("Not done yet")
            case "4": 
                print("Not done yet")
            case "e": 
                playing_game = False
                break
            case "-":
                continue

    
    starting_turn = [0,1]
    random.shuffle(starting_turn)
    turn_order = dict(zip(['X', 'O'], starting_turn)) 
    turn_index = turn_order[game_board.get_current_turn()]
    #Playing the game
    while playing_game:
        #playing game
        clear()
        game_board.print_board()
        
        #turn = game_board.get_current_turn()

        desired_move = player[turn_index].get_move()

        if desired_move == "e":
            break
        
        if type(desired_move) is int: 
            if game_board.is_move_valid(desired_move):

                game_board.play_move(desired_move)

                turn_index = turn_order[game_board.get_current_turn()]

                player[turn_index].update_board(game_board)
                winner = game_board.check_game_win()



                if winner == "draw":
                    game_board.print_board()
                    print("Tie!")
                    break

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

    

