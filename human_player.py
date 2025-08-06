from player import Player # imports the base Player class so we can build a human player class on top of it

class Human_player(Player):

    """
    A class for human players in the game.
    
    Inherits from:
        Player (base class): contains common properties for all players, such as their symbol or board.
   
    The class allows for a real person to input their move through the console.
     
    Attributes: 
        valid_commands (list): A list of strings the player is allowed to input,
        including numbers 1-7 for columns and 'e' or 'exit' to end the game.
     
     Example:
        player1 = Human_player("X", board)  # creates a human player with symbol 'X' and a game board
        move = player1.get_move()  # prompts the player for a move and returns it if valid
      
    """
    # list of valid commands for the player to make a move or exit the game
    valid_commands = ["1","2","3","4","5","6","7","e","exit"]

    def is_valid_input(self, _in):
        """
        Checks if the players input is valid.
        
        Args:
         _in (str): the user input as a string.
         
        Returns:
         bool: true if the input is in the list of valid commands, otherwise false.
         
        Example:
         player1.is_valid_input("3")  # returns True
         player1.is_valid_input("8")  # returns False
        """
        return _in in self.valid_commands

    def get_move(self):
        """
        
        Gets the move from the human player using console input.
        
        Returns:
         int or str: the column index (0-6) where the player wants to drop their piece,
         or 'e' if they want to exit the game.
         
         This Method:
         - Asks the player to input a move
         - Validates the input using 'is_valid_input'
         - If input is 'e' or 'exit, it quits the game
         - If the move is valid column and not full, it returns the column index (0-6)
         - Otherwise, it tells the player the row is full and asks for input again.
         
        Example flow:
         > Enter a move: 3
         Returns: 2 (since we subtract 1 to match 0-indexing)
         """
        # Read input from the player, ensuring it's stripped of whitespace and converted to lowercase
        player_in = input("Enter a move:").strip().lower()

        if not self.is_valid_input(player_in):
            print("Not a valid command!") # if the input is not in the list of valid commands eg "8" or "a"
            return

        if player_in in ["e", "exit"]:
            print("Exiting...")
            return "e"
        # Check if the move is valid (column is not full)    
        if self.board.is_move_valid(int(player_in) - 1):
            return int(player_in) - 1
        else:
            print("Row is full!")
