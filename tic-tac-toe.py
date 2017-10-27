class TicTacToe():
    def __init__(self):
        self.board = [[" "]* 3 for i in range(3)]
        self.cross = 'X'
        self.circle = 'O'
        self.turn = 0
        self.playerXwins = 0
        self.playerOwins = 0
        self.playerTurn = ""

    def placeSign(self, sign, x, y):
        try:
            if sign != self.cross and sign != self.circle:
                raise BaseException("Inavlid sign placed")
        except BaseException:
            print("Invalid sign")

        self.board[y][x] = sign

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
        score = "Player X    "+self.playerXwins+" - "+self.playerOwins+"    Player O"
        boardFirstRow = "["+self.board[0][0]+"] ["+self.board[0][1]+"] ["+self.board[0][2]+"]"
        boardSecondRow = "["+self.board[1][0]+"] ["+self.board[1][1]+"] ["+self.board[1][2]+"]"
        boardThirdRow = "["+self.board[2][0]+"] ["+self.board[2][1]+"] ["+self.board[2][2]+"]"

        print(score+"\n\n\n"+boardFirstRow+"\n"+boardSecondRow+"\n"+boardThirdRow)

game = TicTacToe()
game.printASCIIgame()