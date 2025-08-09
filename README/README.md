# About the project 
This is a CLI game based on Connect Four game, but using symbols from Tic-tac-toe game.

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

# How to play

> Please follow the installation steps in INSTALLATION_README.md before running

Launch the game from connect_four.py

```
python connect_four.py
```

you will then choice between which agent you would like to create a game with:
```
    1. Human (same machine)
    2. Randobot
    3. Normal AI
    4. Hard AI
    5. Impossible AI  
```

You get to choose which two player agents will be vrsing each other. This means any combination is possible, it does just have to be human v machine. You can make the AI's vrs each other 

> the order of players does not determine who goes first. This is randomized

## Playing a move

```
- - - - - - - 
- - - - - - - 
- - - - - - - 
- - - - - - - 
- - - - - - - 
- - - - - - - 
O's turn:

Enter a move:
```

Enter a number where you want to play a move to, 1 if the furthest left and 7 is thr furthest right. If the move you made was invalid, you play again until a valid move is made.

> 'e' or 'Exit' can be used at any time to exit the program



## AI Ethics
### Transparity

**We acknowledge and credit these contributions:**
- Monte Carlo Tree Search is based on work done by Rémi Coulom in 2006, where he explained the use of MCTS in game-theroy (and where he coined the name). 
- UBCT (Upper confidence bounds applied to trees) is also based on work by L. Kocsis and Cs. Szepesvári and further adaptated by S. Gelly in their work on the program MoGo (2008) that would play 9x9 Go

### Fairness and Accessability
This project is open-source, requires no paid softwares, and can be run in terminal. With thorough documentation on how the Monte Carlo Agent works. We do this to encourage people to learn some game theory and how some of these AI agents work.


# Privacy Statement
This project doesn’t collect, store, or share any personal information. Gameplay happens locally, and no network requests are made. No user profiling or tracking is done, so you can rest assured that your privacy is not intefered.

# Extra Information

*Installation steps are referred to "INSTALLATION_README.md" file*

*Requirements for this application are referred to "REQUIREMENTS_README.md"*

*If you would like to know more about Monte Carlo Agent and how it is implemented in this project, refer to "MONTE_CARLO_EXPLAINATION.md"*
