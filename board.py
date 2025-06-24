try:
    from colorama import Fore, init
    init(autoreset=True)
except ImportError:
    print("Colorama is not installed.")
    print("Please install it by running: pip install colorama")
    exit(1)


class Board:
    width = 7
    height = 6
    turn = "O" #circle always goes first


    def __init__(self):
        self.board = [["-" for square in range(self.width)] for square in range(self.height)]
        self.winning_line =[]


    def copy(self):
        new_board = Board()
        #2d array copy method
        new_board.board = [row[:] for row in self.board]
        new_board.turn = self.turn 
        return new_board

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

    def get_valid_moves(self):
        valid_moves = []

        for col in range(self.width):
            if self.is_move_valid(col):
                valid_moves.append(col)
        return valid_moves
    
    #def is_move_valid(self):
    def is_square_valid(self, row, collumn):
        return (collumn >= 0 and collumn < self.width) and ((row >= 0 and row < self.height))

    def is_move_valid(self, collumn):
        if not self.is_square_valid(0,collumn):
            return False
        
        if self.board[0][collumn] != "-":
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
                
                #check bot-right
                if self.is_square_valid(row+3,col+3):
                    if all(piece == self.board[row+i][col+i] for i in range(4)):
                        self.winning_line = [(row+i, col+i) for i in range(4)]
                        return piece
                    
                #check right
                if self.is_square_valid(row,col+3):
                    if all(piece == self.board[row][col+i] for i in range(4)):
                        self.winning_line = [(row, col+i) for i in range(4)]
                        return piece
                
                #check up-right
                if self.is_square_valid(row-3,col+3):
                    if all(piece == self.board[row-i][col+i] for i in range(4)):
                        self.winning_line = [(row-i, col+i) for i in range(4)]
                        return piece

                #check up
                if self.is_square_valid(row-3,col):
                    if all(piece == self.board[row-i][col] for i in range(4)):
                        self.winning_line = [(row-i, col) for i in range(4)]
                        return piece

                #we only need to check Up up-right right and bottom-right, this will cover all win positions
                
        #if no winner is found
        if draw == True:
            return "draw"
        return
    

    def print_board(self):
        for row_index in range(self.height):
            print_str = ""
            for col_index in range(self.width):
                cell = self.board[row_index][col_index] + " "
                if self.winning_line != [] and (row_index, col_index) in self.winning_line:
                    print_str += Fore.GREEN + cell
                elif cell == 'X ':
                    print_str += Fore.RED + cell
                elif cell == 'O ':
                    print_str += Fore.YELLOW + cell
                else:
                    print_str += Fore.WHITE + cell

                
            print(print_str)
