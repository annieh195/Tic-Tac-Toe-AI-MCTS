import numpy as np
import random
from TicTacToe import TicTacToe


class Node:
    def __init__(self, player, N):
        self.child = dict()

        self.player = player
        self.w = 0
        self.n = 0
        self.N = N
        self.c = np.sqrt(2)

    def utc(self):
        if self.n == 0:
            return float('inf')
        return self.w / self.n + self.c * np.sqrt(np.log(self.N) / self.n)

    def update(self, winner):
        if self.player == winner:
            self.w += 1
        self.n += 1
        self.N += 1

    def __str__(self):
        return f'player={self.player} w={self.w} n={self.n} N={self.N}'


class MCTS:
    def __init__(self, game, player, simulations=5000, min_visit=20):
        self.game = game
        self.player = player
        self.simulations = simulations
        self.min_visit = min_visit
        self.root = Node(3 - player, 0)
        if self.player == 2:
            self.root.player = 2
            self.expand(self.root)
            self.root.player = 1

    def next_move(self):
        for i in range(self.simulations):
            self.simulate(self.root)

        best = max(self.root.child, key=lambda m: self.root.child.get(m).utc())
        self.root = self.root.child[best]
        return best

    def update_game(self, move):
        self.root = self.root.child[move]

    def simulate(self, root):
        if self.game.ended():
            root.update(self.game.winner)
            return self.game.winner

        if root.n < self.min_visit:
            winner = self.rollout()
            root.update(winner)
            return winner

        if not len(root.child):
            self.expand(root)

        best = max(root.child, key=lambda m: root.child.get(m).utc())
        self.game.play(best)
        winner = self.simulate(root.child[best])
        root.update(winner)
        self.game.undo()
        return winner

    def expand(self, root):
        for move in self.game.moves:
            root.child[move] = Node(3 - root.player, root.n)

    def rollout(self):
        count = 0
        while not self.game.ended():
            self.game.play(random.choice(tuple(self.game.moves)))
            count += 1
        winner = self.game.winner
        for i in range(count):
            self.game.undo()
        return winner






