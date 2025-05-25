class Board:
    width = 7
    height = 6
    turn = "X"

    def __init__(self):
        self.board = [["-" for square in range(self.width)] for square in range(self.height)]

    def set_board(self, board_ar):
        self.board = board_ar

    def get_current_turn(self):
        return self.turn

    def get_board_state(self):
        return self.board

    def swap_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    #def is_move_valid(self):
    def is_square_valid(self, row, collumn):
        return (collumn >= 0 and collumn < self.width) and ((row >= 0 and row < self.height))

    def is_move_valid(self, collumn):
        if not self.is_square_valid(0,collumn):
            print("Error: move is not valid")
            return False
        
        if self.board[0][collumn] != "-":
            print("Row is full")
            return False
        
        return True      


    def play_move(self, collumn):
        for row in reversed(range(self.height)):
            if self.board[row][collumn] == "-":
                self.board[row][collumn] = self.turn

                self.swap_turn()
                return
                
    def check_game_win(self):
        
        draw = True

        for row in range(self.height):
            for col in range(self.width):
                piece = self.board[row][col]
                if piece == "-":
                    draw = False
                    continue        
                
                #check right
                if self.is_square_valid(row,col+3):
                    if all(piece == self.board[row][col+i] for i in range(4)):
                        return piece
                
                #check up-right
                if self.is_square_valid(row-3,col+3):
                    if all(piece == self.board[row-i][col+i] for i in range(4)):
                        return piece

                #check up
                if self.is_square_valid(row-3,col):
                    if all(piece == self.board[row-i][col] for i in range(4)):
                        return piece

                #we only need to check Up up-right abd right, this will cover all win positions
                
        #if no winner is found
        if draw == True:
            return "draw"
        return
    

    def print_board(self):
        for row in self.board:
            print(" ", end = "")
            for col in row:
                print(col,end=" ")
            print()
