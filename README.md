# Tic-Tac-Toe-AI-MCTS
Tic Tac Toe with AI using Monte Carlo Tree Search.

## Note
In the game of Tic Tac Toe, it is widely known that assuming both players are skilled, the starting player will never lose and will at least achieve a tie if they play optimally. Interestingly, scientific analysis, including the use of Monte Carlo Tree Search (MCTS), has revealed that the optimal initial move for the starting player is not the middle position but rather one of the corners. However, it should be noted that this knowledge pertains to probabilities and strategic considerations, as skilled players at the master level will consistently reach a tie outcome.

## Play
```
Game.py
```

## Result
```
Game board:
1 2 3
4 5 6
7 8 9
Please select player 1 or 2: 2
Player 1 (AI) played next move at 5
. . . 
. O . 
. . . 

Player 2 please select a move [1-9]: 5
Invalid move
Player 2 please select a move [1-9]: 6
. . . 
. O X 
. . . 

Player 1 (AI) played next move at 9
. . . 
. O X 
. . O 

Player 2 please select a move [1-9]: 1
X . . 
. O X 
. . O 

Player 1 (AI) played next move at 7
X . . 
. O X 
O . O 

Player 2 please select a move [1-9]: 3
X . X 
. O X 
O . O 

Player 1 (AI) played next move at 8
X . X 
. O X 
O O O 

Player 1 wins
```
AI assumes the role of player 1, unless you choose to designate humans as the starting players by selecting 1.

## References
Algorithm (https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)
