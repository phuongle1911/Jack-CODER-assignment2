import random

class Player():

    def __init__(self, board):
        self.board = board

    def get_move(self):
        
        move = random.randint(0,6)

        return move
    
    def update_board(self, board):
        self.board = board


    