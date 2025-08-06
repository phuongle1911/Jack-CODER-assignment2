from player import Player
import random
import math

#Create the monte carlo agent
class Monte_carlo_player(Player):

    # constructor for the agent, interations are for the amount of thinking (expansions) the agent gets before it must make a move
    # higher numbers lead to a smarter agent, but a slower run time
    def __init__(self, board, interations = 1000):
        super().__init__(board)
        self.interations = interations
        

    #get the agents chosen move
    def get_move(self):
        
        # create the base node of the MCST (tree) from the current gamestate 
        # this is the actual board we are searching for a move from
        # so we copy the board given to this agent
        root = MCTS_node(self.board.copy())

        # if there isnt any moves to make, return -1
        if root.board.get_valid_moves() == []:
            return -1

        # repeat the logic to the amount of given iterations 
        for i in range(self.interations):
            # start at the root of the tree (the very top)
            node = root
            
            # find the best child of the root. The best child is the one that has the highest Upper confidence bound (UCB1 Formula).
            # This is a child that has a good amounts of wins or low amounts of visits, as we need to insure each option is thouroughly explored
            # When the best child is found, we reapeat this with that nodes children until we find an unexplored node.
            node = node.get_best_child()

            #Expand the best unexplored child node by creating a new child for this node. This child has the board state of a random move from the last board
            #     - - - - -         - - - - -
            #     - - - - -         - - - - -
            #     - - - - -         - - - - -         
            # EG. - x - - - becomes - x o - - in this child. The original node will eventually have each of the possible moves from this board explored
            new_child = node.expand()

            # With this new child, we rollout (simulate) a full game starting from this position
            # The game we simulate has no logic and is just two agents playing random moves
            # we then evaluate a winner or draw
            winner = new_child.rollout()

            # With the winner, we must tell this nodes parents wether this was a winning move or not. 
            # Because of this we 'backpropagate' back up the tree. Starting the node and returning to each of their parents until we make it to the root (a node with no parent)
            # As we go through these parents nodes we add a visit to them to let the next UBC formula more informed.
            # Each of these parents are given a win if they played the move that won EG a board that played a 'O' move would get +1 wins if 'O' won the rollout. 
            # 0.5 points is also awarded to a node if there was a draw, since it should still be incetivised just not as highly as a win.
            # This is done because when finding the best child we need to take into account both players playing the best move. 
            # It wouldnt make sense to only take paths that won for our root board since we should expect the enemy to play their best moves too
            new_child.backpropagate(winner)

        #Decide our best move based on the most explored child node of the root
        best_move = max(root.children, key=lambda child: child.visits).move
        return best_move; 


#Nodes for the tree to build with
class MCTS_node():

    # Node constructor, it takes a base board to play from
    # A parent is added if the node is a child of another
    # move is also added to specify what move was played to get to this position
    def __init__(self, board, move=None, parent=None):
        self.board = board

        self.children = []
        self.unexplored_moves = board.get_valid_moves()

        self.visits = 0
        self.wins = 0

        self.move = move
        self.parent=parent

    # recursive function to find the best unexplored child
    def get_best_child(self):

        # if we havent fully expand here end the recursion and return the current node, this is the best child
        if len(self.unexplored_moves) != 0:
            return self
          

        # If we dont have any children, then we need to be expanded so we are the best child
        # end the recursion and return itself
        if not self.children:
            return self
        
        #search each of this nodes children
        best_child = max(self.children,
                        # Upper Confidence Bound 1 (UCB1) Formula:
                        # This formula is used to find a child that has the most potential if expanded
                        # It does this by weighing up the amount of wins that child has against its visits 
                        # higher visits are expencted to have more wins since they are explored more.
                        # We use this formula since we cant only look for wins and must encourage exploration between different options 
                        # - The 1.41 is a constant that controls how strongly to favor exploration
                        key=lambda node: node.wins / node.visits + 1.41 * math.sqrt(math.log(self.visits) / node.visits))
        
        #we then will check our best childs, best child and so on until an unexplored node is found
        return best_child.get_best_child()
    

    # Adds a new node that uses a new move to a parent node
    def expand(self):

        # If there are no nodes to expand from this point, return
        if not self.unexplored_moves:
            return self  # No moves to expand, return

        # choose a random valid move to make, we will explore that move
        index = random.randint(0, len(self.unexplored_moves)-1)
        move = self.unexplored_moves[index]
        self.unexplored_moves.pop(index)

        # Copy the current nodes board state and play that random move, this will be the starting board for the new node
        new_board = self.board.copy()
        new_board.play_move(move)

        # Create the new node with: the copied board, most recent move made, and the current node as the parent
        new_node = MCTS_node(new_board, move, self)
        self.children.append(new_node) # add the new node as a child to the current node
        return new_node
    
    # Play a full game until a winner is found from a nodes starting board atate
    def rollout(self):
        
        #play a random game from the made move, see who wins and return the result
        temp_board = self.board.copy()

        #Game loop
        while True:
            #check if there is a winner to the game
            winner = temp_board.check_game_win()

            # If there is a winner (or draw) return it
            if winner != None:
                return winner
          
            # Play a random move then repeat the loop
            temp_board.play_move(random.choice(temp_board.get_valid_moves()))

    
    # Add the winning score to each of the nodes parents and increase their visits
    # result can either be, None, draw or 'X' and 'O'
    def backpropagate(self, result):
            
            # Increase the current nodes visits
            self.visits += 1

            #Get the nodes current turn 'X' or 'O'
            turn = self.board.get_current_turn()

            if result in ['O', 'X']: #If the result is a win

                # The turn does not equal the result add a win.
                # This is done because 'turn' would be the next turn to play, 
                # not the current nodes 'turn' it just played 
                # EG if 'O' just played a turn it is now 'X's turn, but this node is refering to 'O' so if 'O' is the result add a win
                if turn != result:
                    self.wins += 1
            elif result == "draw":
                # If there was a draw, add 0.5 regardless of turn
                self.wins += 0.5

            # If we are not the root continue the recursion
            # The root is the only node with no parent
            if not self.parent == None:
                self.parent.backpropagate(result)
            
    