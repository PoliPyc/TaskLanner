class TicTacToe():
    def __init__(self):
        self.board = [[" "]* 3 for i in range(3)]
        self.cross = 'X'
        self.circle = 'O'
        self.turn = 0
        self.playerXwins = 0
        self.playerOwins = 0
        self.playerTurn = ""

    def _placeSign(self, sign, x, y):
        try:
            if sign.upper() != self.cross and sign.upper() != self.circle:
                raise BaseException("Inavlid sign placed")
        except BaseException:
            print("Invalid sign")

        self.board[y][x] = sign

    def placeSign(self, x, y):
        x = int(x) - 1
        y = int(y) - 1
        if self.board[y][x] != " ":
            return 1

        self.board[y][x] = self.playerTurn
        return 0

    def countTurn(self):
        self.turn =+ 1
        if not self.playerTurn or self.playerTurn == self.circle:
            self.playerTurn = self.cross
        else:
            self.playerTurn = self.circle

    def checkGame(self):
        if (self.board[0][0] == self.board[1][0] == self.board[2][0] or
            self.board[0][1] == self.board[1][1] == self.board[2][1] or
            self.board[0][2] == self.board[1][2] == self.board[2][2] or
            self.board[0][0] == self.board[0][1] == self.board[0][2] or
            self.board[1][0] == self.board[1][1] == self.board[1][2] or
            self.board[2][0] == self.board[2][1] == self.board[2][2] or
            self.board[0][0] == self.board[1][1] == self.board[2][2] or
            self.board[0][2] == self.board[1][1] == self.board[2][0]):
                self.endGame()

    def endGame(self):
        if self.playerTurn == self.cross:
            self.playerXwins += 1
        else:
            self.playerOwins += 1
        self.turn = 0
        self.board = [[" "] * 3 for i in range(3)]

    def printASCIIgame(self):
        score = "Player X    {} - {}    Player O"
        boardRow = "         [{}] [{}] [{}]"

        print(score.format(self.playerXwins, self.playerOwins))
        print(boardRow.format(self.board[0][0], self.board[0][1], self.board[0][2]))
        print(boardRow.format(self.board[1][0], self.board[1][1], self.board[1][2]))
        print(boardRow.format(self.board[2][0], self.board[2][1], self.board[2][2]))

game = TicTacToe()
while True:
    game.printASCIIgame()
    while game.countTurn():
        pass
    game.placeSign(input(), input())