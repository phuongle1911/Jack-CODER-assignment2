from player import Player
import random
import math


class Monte_carlo_player(Player):

    def __init__(self, board, interations = 1000):
        super().__init__(board)
        self.interations = interations
        


    def get_move(self):
        
        root = MCTS_node(self.board.copy())

        for i in range(self.interations):
            #start at the root of the tree
            node = root

            node = node.get_best_child()

            new_child = node.expand()

            winner = new_child.rollout()

            new_child.backpropagate(winner)

        best_move = max(root.children, key=lambda child: child.visits).move
        return best_move; 


class MCTS_node():

    def __init__(self, board, move=None, parent=None):
        self.board = board

        self.children = []
        self.unexplored_moves = board.get_valid_moves()

        self.visits = 0
        self.wins = 0

        self.move = move
        self.parent=parent

    def get_best_child(self):
        #if we are fully explored
        if len(self.unexplored_moves) != 0:
            return self
          

        #if there are no children to explore
        if not self.children:
            return self
        
        #search each of this nodes children
        best_child = max(self.children,
                         #this lambda function checks a given node for its (UCB1 Formula) insuring that we check a varied amount of nodes
                         #Not just ones that win, but ones that are unexplored (The formula is based on visits and wins)
                        key=lambda node: node.wins / node.visits + 1.41 * math.sqrt(math.log(self.visits) / node.visits))
        
        #we then will check our best childs, best child and so on until an unexplored node is found
        return best_child.get_best_child()
    

    def expand(self):
        if not self.unexplored_moves:
            return self  # No moves to expand, return

        #choose a random valid move to make, we will explore that move
        index = random.randint(0, len(self.unexplored_moves)-1)
        move = self.unexplored_moves[index]
        self.unexplored_moves.pop(index)

        new_board = self.board.copy()
        new_board.play_move(move)

        new_node = MCTS_node(new_board, move, self)
        self.children.append(new_node)
        return new_node
    
    def rollout(self):
        
        #play a random game from the made move, see who wins and return the result
        temp_board = self.board.copy()

        while True:
            #check if there is a winner to the game
            winner = temp_board.check_game_win()
            if winner != None:
                return winner
          
            temp_board.play_move(random.choice(temp_board.get_valid_moves()))

    
    def backpropagate(self, result):
            #result can either be, None, draw or 'X' and 'O'
            self.visits += 1

            #Get the nodes turn 'X' or 'O'
            turn = self.board.get_current_turn()

            if result in ['O', 'X']:

                #if the turn (does not equal result add one)
                #i do this as the current turn of the board, is flipped
                #It could be fixed, but oh well ¯\_(ツ)_/¯

                if turn != result:
                    self.wins += 1
            elif result == "draw":
                self.wins += 0.5

            #if we are not the root
            if not self.parent == None:
                self.parent.backpropagate(result)
            
    