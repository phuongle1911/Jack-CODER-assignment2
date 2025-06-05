import random

class Player():

    def __init__(self, board):
        self.board = board

    def set_peice(self, peice):
        self.peice = peice


    def get_move(self):
        
        return random.choice(self.board.get_valid_moves())
    
    def update_board(self, board):
        self.board = board.copy()


    