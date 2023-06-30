from TicTacToe import TicTacToe
from MCTS import MCTS

game = TicTacToe()

print('Game board:\n1 2 3\n4 5 6\n7 8 9')
player = 0
while player != 1 and player != 2:
    player = int(input('Please select player 1 or 2: '))

computer = 3 - player

mcts = MCTS(game, computer)

while not game.ended():
    if game.turn == computer:
        pos = mcts.next_move()
        print(f"Player {game.turn} played next move at {pos}")
        game.play(pos)
        print(game)
    else:
        pos = int(input(f'Player {game.turn} please select a move [1-9]: '))
        try:
            if pos == 0:
                game.undo()
            else:
                game.play(pos)
                mcts.update_game(pos)
            print(game)
        except IndexError:
            print("Invalid move")

if game.winner != 0:
    print(f'Player {game.winner} wins')
else:
    print('Draw')
