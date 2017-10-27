class TicTacToe():
    def __init__(self):
        self.board = [[" "]* 3 for i in range(3)]
        self.cross = 'X'
        self.circle = 'O'
        self.turn = 0
        self.playerXwins = 0
        self.playerOwins = 0
        self.draws = 0
        self.playerTurn = ""

    #deprecated
    def _placeSign(self, sign, x, y):
        try:
            if sign.upper() != self.cross and sign.upper() != self.circle:
                raise BaseException("Invalid sign placed")
        except BaseException:
            print("Invalid sign")

        self.board[y][x] = sign

    def placeSign(self, x, y):
        x = int(x) - 1
        y = int(y) - 1

        try:
            if x < 0 or x > 2 or y < 0 or y > 2:
                raise BaseException("offset")

            if self.board[y][x] != " ":
                raise BaseException("already placed")
        except BaseException:
            print("invalid coordinates\n put again:")
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
        score = "Player X    {} - {} - {}    Player O"
        columns = "            1   2   3 "
        boardRow = "         {} [{}] [{}] [{}]"

        print(score.format(self.playerXwins, self.draws, self.playerOwins))
        print(columns)
        print(boardRow.format(1, self.board[0][0], self.board[0][1], self.board[0][2]))
        print(boardRow.format(2, self.board[1][0], self.board[1][1], self.board[1][2]))
        print(boardRow.format(3, self.board[2][0], self.board[2][1], self.board[2][2]))

    def clearScreen(self):
        print("\r\r\r\r\n\n\n\n\r\r\r\r")

game = TicTacToe()
while True:
    game.printASCIIgame()
    game.countTurn()
    valid = False
    while valid == False:
        if game.placeSign(input(), input()) == 0:
            valid = True
    if game.turn > 4:
        game.checkGame()
    game.clearScreen()