# The code belows to check if colorama package has been installed
try:
    from colorama import Fore, init # colorama is installed and used to color texts in the terminal. In this case, it is used for color players' symbols 'X' and 'O'
                                    # init function is imported to initialise Colorama: init(autoreset=True)
                                    # Fore is an object within the colorama module that provides access to various text color constants.
    init(autoreset=True) # colorama is initilised, Autoreset ensures colors reset after each print
except ImportError: # capture ImportError (occured when colorama has not been installed)
    print("Colorama is not installed.") # print error message
    print("Please install it by running: pip install colorama")
    exit(1)

# Create a board for playing
class Board:
    width = 7 # 7 columns
    height = 6 # 6 rows
    turn = "O" #circle always goes first

    # class constructor
    def __init__(self):
        self.board = [["-" for square in range(self.width)] for square in range(self.height)] # Initilising 'board' attribute, which is a list of "-" repeated by looping through width and height of the board
                                                                                            # '-' represent for empty space
        self.winning_line =[] # Initilising winning_line attribute, being an empty list

    # function to capture and display the latest updated board, and capture
    def copy(self):
        new_board = Board() # create an instance of Board class
        #2d array copy method
        new_board.board = [row[:] for row in self.board]
        new_board.turn = self.turn 
        return new_board
    
    # set the board
    def set_board(self, board_ar):
        self.board = board_ar

    # function to capture current player having turn
    def get_current_turn(self):
        return self.turn

    # get the current board state
    def get_board_state(self):
        return self.board

    # change turn to the other player
    def swap_turn(self):
        if self.turn == "X":  # change to "O" turn if the current turn is "X"
            self.turn = "O"
        else:
            self.turn = "X" # if current turn is not "X", it must be "O", therefore turn changed to "X"

    # function to capture all column indexes of empty cell at bottom of the board and return in a list
    def get_valid_moves(self):
        valid_moves = [] # move to be reset to be empty list

        # capture the all empty cell at the bottom of the board and append their column index to valid_moves list
        for col in range(self.width):
            if self.is_move_valid(col):
                valid_moves.append(col)
        return valid_moves
    
    # check if row and collumn is valid, meaning within the board
    # If one of row and column is outside of the board or lower than 0, the function returns False
    # for example:
    # is_square_valid(4,8) return False, as column value (8) > board width (7)
    # is_square_valid(2,6) return True, as row value (2) < board height (6), column value (6) < board width (7)
    def is_square_valid(self, row, collumn):
        return (collumn >= 0 and collumn < self.width) and ((row >= 0 and row < self.height))

    # check if entered move (represent column index) is valid. 
    # valid move is a number within board width and the cell at bottom of the board in that column number is empty 
    def is_move_valid(self, collumn):
        if not self.is_square_valid(0,collumn): # if the move not within range of (0,board width), is_square_valid function return False, and is_move_valid return False
            return False
         # check if the cell in bottom of the board in entered column index is empty. If not, function return False. 
        if self.board[0][collumn] != "-":
            return False
        
        return True      

    # function to place symbol on the board based on move input
    def play_move(self, collumn):
        for row in reversed(range(self.height)): # loop through row index on the board
            if self.board[row][collumn] == "-": # check if the requested place on board is empty
                self.board[row][collumn] = self.turn # place current player's symbol in that place if empty

                self.swap_turn() # then swap to the other player's turn when done
                return # finish the function, dont need to return anything

    # function to check if any player wins            
    def check_game_win(self):
        
        draw = True

        # Check if the game is draw (all spaces in the board are full)
        for row in range(self.height):
            for col in range(self.width):
                piece = self.board[row][col]
                if piece == "-": # draw becomes False if there is any empty space in the board, then continue with the loop
                    draw = False 
                    continue        
                
                # check 3 pieces diagonally on the down-right of each piece in the board
                # if all 3 spaces is equal to the piece, that is winning line, return the winning piece (X or O)
                if self.is_square_valid(row+3,col+3): # ensure only the pieces inside the board are checked
                    if all(piece == self.board[row+i][col+i] for i in range(4)): # only return True when all arguments are True
                        self.winning_line = [(row+i, col+i) for i in range(4)] # capture the row and column index of all winning pieces in winning_line list
                        return piece # return which symbol is winner
                    
                #check 3 pieces horizontally on the right of each piece in the board
                # if all 3 spaces is equal to the piece, that is winning line, return the winning piece (X or O)
                if self.is_square_valid(row,col+3):  # ensure only the pieces inside the board are checked
                    if all(piece == self.board[row][col+i] for i in range(4)):  # ensure only the pieces inside the board are checked
                        self.winning_line = [(row, col+i) for i in range(4)] # capture the row and column index of all winning pieces in winning_line list
                        return piece # return which symbol is winner
                
                # check 3 pieces diagonally on the up-right of each piece in the board
                if self.is_square_valid(row-3,col+3):
                    if all(piece == self.board[row-i][col+i] for i in range(4)):
                        self.winning_line = [(row-i, col+i) for i in range(4)]
                        return piece

                #check 3 pieces vertically above of each piece in the board
                if self.is_square_valid(row-3,col):
                    if all(piece == self.board[row-i][col] for i in range(4)):
                        self.winning_line = [(row-i, col) for i in range(4)]
                        return piece

                #we only need to check Up up-right right and bottom-right, this will cover all win positions
                
        #if no winner is found, return draw
        if draw == True:
            return "draw"
        return
    
    # print latest updated board with all latest players' moves in color format
    def print_board(self):
        # loop through all spaces on board
        for row_index in range(self.height):
            print_str = ""
            for col_index in range(self.width):
                cell = self.board[row_index][col_index] + " " # a cell on the board

                # Color the winning lines in Green
                if self.winning_line != [] and (row_index, col_index) in self.winning_line:
                    print_str += Fore.GREEN + cell

                # Color 'X' symbol on the board in Red
                elif cell == 'X ':
                    print_str += Fore.RED + cell

                # Color 'O' symbol on the board in Yellow
                elif cell == 'O ':
                    print_str += Fore.YELLOW + cell

                # Color empty space '-' in White
                else:
                    print_str += Fore.WHITE + cell

                
            print(print_str) # Print the board
