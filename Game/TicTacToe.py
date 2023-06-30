class TicTacToe:
    PLAYER_1 = 1
    PLAYER_2 = 2

    def __init__(self):
        self.board = [[0 for j in range(3)] for i in range(3)]
        self.turn = TicTacToe.PLAYER_1
        self.moves = set(i for i in range(1, 10))
        self.history = []
        self.winner = 0

    def play(self, pos):
        if self.ended():
            return

        row = (pos - 1) // 3
        col = pos - 1 - row * 3

        if pos in self.moves:
            self.moves.remove(pos)
            self.history.append(pos)
            self.board[row][col] = self.turn

            # check vertical win
            for i in range(3):
                if self.board[i][col] != self.turn:
                    break
                elif i == 2:
                    self.winner = self.turn

            # check horizontal win
            for i in range(3):
                if self.board[row][i] != self.turn:
                    break
                elif i == 2:
                    self.winner = self.turn

            # check forward diagonal win
            if row + col == 2:
                for i in range(3):
                    if self.board[2 - i][i] != self.turn:
                        break
                    elif i == 2:
                        self.winner = self.turn

            # check backward diagonal win
            if row == col:
                for i in range(3):
                    if self.board[i][i] != self.turn:
                        break
                    elif i == 2:
                        self.winner = self.turn

            # change turn to next player
            self.turn = 3 - self.turn
        else:
            raise IndexError(f"Invalid move, position {pos} has been placed.")

    def undo(self):
        if len(self.history):

            pos = self.history[-1]
            row = (pos - 1) // 3
            col = pos - 1 - row * 3
            self.board[row][col] = 0

            self.turn = 3 - self.turn
            self.moves.add(self.history.pop())
            self.winner = 0

    def ended(self):
        return self.winner != 0 or len(self.moves) == 0

    def last_move(self):
        if len(self.history):
            return self.history[-1]
        return 0

    def __str__(self):
        res = ''
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    res += '. '
                elif self.board[i][j] == 1:
                    res += 'O '
                elif self.board[i][j] == 2:
                    res += 'X '
            res += '\n'
        return res




