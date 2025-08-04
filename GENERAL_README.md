# About the project 
This is a CLI game based on Tic-tac-toe game, the game that used X's and O's. 

This game is built with following rules:
- The player to take first turn is randomly chosen.
- Game allows 2 players to take turn to place their symbol into a displayed board, one player is assigned with X and the other is assigned with O. 
- The first player who get four of their symbols in a row (either horizontally, vertically, or diagonally) wins.
- If all spaces in the board (displayed with '-') are filled and no player has four in a row, the game is a draw.

## Features
The game has following features:
- Display the board
- Allow player to choose to play with human or machine or AI bot, with following agents has been built:
  - Player - the basic playable character
  - Randobot - picks a random move, does not know how to win
  - Monte Carlo Agent - A much more complex agent that will play the game with more intelligent moves to try to win you. 
- Notify when one of the player wins and highlight the win row in Green.

Detailed information about Monte Carlo Agent is as following:

### Monte Carlo Agent
The monte carlo agent uses a monte carlo tree search to find the best moves. The concept is that the agent plays the game to the very end by selecting moves randomly. 

While it does this, it makes sure that winning moves are further explored, while unexplored moves gain at least
some exploration.

The formula for deciding which node to explore is as follows:

$\frac{w}{n} + c \sqrt{\frac{\ln N}{n}}$

This is the Upper Confidence Bound for Trees (UCBT) formula, commonly used in other Monte Carlo tree search algorithms
To change the difficulty of the AI we just change how many iterations the agent gets when exploring.

This agent follow below steps:
#### Selection
Find a node that is unexplored, using the UCBT formula it finds a node, then travels through that nodes's best child and continues until a unexplored option is found

#### Expansion
A random valid move is chosen to make from this nodes board, then return the node

#### Rollout
With the chosen node, a game is simulated with the node's scenario, and return who the winner was ('X' 'O' or draw)

#### Back propagation
All nodes visits are then updated by +1 and its win if it is the corresponding piece. Ie. a board that played a 'O' move gains a point if 'O' won the rollout
Drawn boards also add 0.5 to the score, so the agent also accounts for that option

Note: Because of how backpropagation works, the best move for X and O are accounted for regardless of which one is the agent's piece. The reason is that other player is expected to make their best move as well. 



Installation steps are referred to INSTALLATION_README.md file

Requirements for this application are referred to REQUIREMENTS_README.md



