# About the project 
This is a CLI game based on Tic-tac-toe game, the game that used X's and O's. 

This game is built with following rules:
- The first turn is randomly chosen between 2 players. 
- Game allows 2 players to take turn to place their symbol into a displayed board, one player is assigned with X and the other is assigned with O. 
- The player chooses a column (1–7) to place their symbol.  
- Symbols stack from the bottom of the column upward, filling the lowest available space.  
- The first player who get four of their symbols in a row (either horizontally, vertically, or diagonally) wins.
- If all spaces in the board (displayed with '-') are filled and no player has four in a row, the game is a draw.
- Enter "e" to exit the game anytime. If you would like to play again, enter "y", otherwise enter "n".

## Features
The game has following features:
- Display the board
- Allow player to choose to play with human or machine or AI bot, with following agents has been built:
  - Player - the basic playable character
  - Randobot - picks a random move, does not know how to win
  - Monte Carlo Agent - A much more complex agent that will play the game with more intelligent moves to try to win you. 
- Notify when one of the player wins and highlight the win row in Green.

Detailed information about Monte Carlo Agent is as following:

# Monte Carlo Agent
There are three available difficulties of the monte carlo agent, the only change netween them is the amount of times the AI agent gets to think:
- Normal AI: 250
- Hard AI: 750
- Impossible AI: 1500

For the best experience vrsing this agent unhindered, Impossible AI is the best to go with!

## Explanation
The monte carlo agent uses a monte carlo tree search to find the best moves. The concept is that the agent plays the game to the very end by selecting moves randomly. 

While it does this, it makes sure that winning moves are further explored, while unexplored moves gain at least
some exploration.

The formula for deciding which node to explore is as follows:

$\frac{w}{n} + c \sqrt{\frac{\ln N}{n}}$

This is the Upper Confidence Bound for Trees (UCBT) formula, commonly used in other Monte Carlo tree search algorithms.

## MCST nodes

This is what the search tree is made from. Think of each node as a board state. Each of these board states have a amount of valid moves they can make. Eg this could be a nodes current board state

```
- - - - 
- - - -
- - X -
```
We would be able to make a move at collumn: 1 2 3 and 4 so how will we find which move to make next?

We figure this out by creating child nodes to this board, each of these mimicking what would happen if the corresponding move was played

```
Child 1     Child 2     Child 3     Child 4
- - - -     - - - -     - - - -     - - - -  
- - - -     - - - -     - - O -     - - - - 
O - X -     - O X -     - - X -     - - X O      
```

Each of these nodes would be valid children of the first node

With this new node, we give it a few more bits of information:
- Which move was just made to get to this point 
- The turn that was just played ('O' in this case)
- The parent node, so the node that this node came from

Other information the node contains are:
- The amount of wins it has seen
- The amount of visits/ checks the program has done here

As we keep expanding each of these nodes (by giving them more children) we start to see the nodes make a tree like structor. Giving the algorithm its name.

## Logic on the turn

First the agent makes a starting node using the oringinal board that they will be playing to.

> Most notably this node does not have a parent thus making it the 'root' 

## Selection
When selecting we must find a node that is unexplored and has the best chance of winning, or leading to a good outcome.

We do this by using the UCBT formula ($\frac{w}{n} + c \sqrt{\frac{\ln N}{n}}$) on a node, checking which child has the best result on the formula. Wins and visits are used to balence it out since nodes with medium visits but high wins should be explored just as throuroughly.

After a best child has been chosen, we go to that node and repeat until we find a node with a missing child (a move that has yet to be mimicked) This node is selected to be expanded.

## Expansion
With the given best child, we create a child to that board using a move that has yet to have a child based on

```
      Current Node
        - - - -      
        - - O -     
        - - X - 


Old child   Created Child 
- - X -        - - - -     
- - O -        - - O -     
- - X -        - - X X     
```

> Eg. placing a new move on column 3 would not be allowed, since there is already a child with that move used attached to this node

## Rollout
We then simulate a full match of a game starting from the new nodes board.
using random moves for both players. This continues until there is a draw or a win
```
Created Child         Rollout results 
    - - - -              O - O X 
    - - O -     ->       X - O O        -> X wins
    - - X X              X X X X 
```
With the simulated game we return who won: 'X' 'O' or draw

## Back propagation
With the simulated result, we have to tell each node wether one of their children won, lost or drew.

So we end up going back through each node, until we reach the root node (the board we are acutally looking for the best move for). Adding points for a win and adding a visit to the node.


```
     Root
   - - - -      
   - - - -  - Root, add nothing   
   - - X - 
      |
    Child
   - - - -      
   - - O -  + 0 wins (X won) + 1 visit!       
   - - X - 
      |
    Child
   - - - -   
   - - O -  + 1 wins (X won) + 1 visit!    
   - - X X 
```

As we go through each node we check what piece the nodes last move made was ('X' or 'O'). this is because we will end up finding the best move from **each game state**. So if X won the board that X just played to would get a point but if O just played to the board they dont get anything.

We do this because we need to assume that every player will make the best move for them, we shouldnt just assume the enemy player is going to make the best move to let us win!

> On a draw 0.5 points are instead rewarded to both players. To insentivise draws if no wins are availble


```
*Installation steps are referred to INSTALLATION_README.md file*

*Requirements for this application are referred to REQUIREMENTS_README.md*
```