import random

class Player():

    def __init__(self, board):
        self.board = board

    def get_move(self):
        return random.randint(1, 7)
    
    def update_board(self, board):
        self.board = board


class Human_player(Player):

    valid_commands = ["1","2","3","4","5","6","7","e","exit"]

    #get commands
    def is_valid_input(self, _in):
        return _in in self.valid_commands

    def get_move(self):
        player_in = input("Enter a move:").strip().lower()


        if not self.is_valid_input(player_in):
            print("Invalid input")

        if player_in in ["e", "exit"]:
            print("Exiting...")
            return
        
        if self.board.is_move_valid(int(player_in) - 1):
            return int(player_in) - 1
    