import sys, copy
from multiplayer import *

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
        self.gameEnded = 0

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
        self.turn += 1

    def changePlayer(self):
        if not self.playerTurn or self.playerTurn == self.circle:
            self.playerTurn = self.cross
        else:
            self.playerTurn = self.circle

    def checkGame(self):
        if (self.board[0][0] != " " and self.board[0][0] == self.board[1][0] == self.board[2][0] or
            self.board[0][1] != " " and self.board[0][1] == self.board[1][1] == self.board[2][1] or
            self.board[0][2] != " " and self.board[0][2] == self.board[1][2] == self.board[2][2] or
            self.board[0][0] != " " and self.board[0][0] == self.board[0][1] == self.board[0][2] or
            self.board[1][0] != " " and self.board[1][0] == self.board[1][1] == self.board[1][2] or
            self.board[2][0] != " " and self.board[2][0] == self.board[2][1] == self.board[2][2] or
            self.board[0][0] != " " and self.board[0][0] == self.board[1][1] == self.board[2][2] or
            self.board[0][2] != " " and self.board[0][2] == self.board[1][1] == self.board[2][0]):
                self.endGame(self.playerTurn)

        if self.turn >= 9:
            self.endGame("draw")

    def endGame(self, winner):
        if winner == self.cross:
            self.playerXwins += 1
        elif winner == self.circle:
            self.playerOwins += 1
        else:
            self.draws += 1

        self.clearScreen()
        self.printASCIIgame()

        self.board = [[" "] * 3 for i in range(3)]
        self.turn = 0
        self.playerTurn = ""
        self.gameEnded = 1

        if winner == "draw":
            print("It's draw!")
        else:
            print("Player{} wins!".format(winner))

    def printASCIIgame(self):
        score = '\033[34m'+"Player X    {}" + '\033[0m' + " - {} - " + '\033[31m' + "{}    Player O" + '\033[0m'
        columns = "            1   2   3 "
        boardRow = "         {} [{}] [{}] [{}]"
        turns = "            Turn {}"

        marks = [[" "]* 3 for i in range(3)]
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == self.cross:
                    marks[x][y] = '\033[34m'+self.cross+'\033[0m'
                elif self.board[x][y] == self.circle:
                    marks[x][y] = '\033[31m'+self.circle+'\033[0m'


        print(score.format(self.playerXwins, self.draws, self.playerOwins))
        print(columns)
        print(boardRow.format(1, marks[0][0], marks[0][1], marks[0][2]))
        print(boardRow.format(2, marks[1][0], marks[1][1], marks[1][2]))
        print(boardRow.format(3, marks[2][0], marks[2][1], marks[2][2]))
        print(turns.format(self.turn))

    def clearScreen(self):
        print("\033c")

    def localGame(self):
        self.gameEnded = 0
        while not self.gameEnded:
            self.clearScreen()
            self.countTurn()
            self.changePlayer()
            self.printASCIIgame()
            valid = False
            while valid == False:
                if self.placeSign(input(), input()) == 0:
                    valid = True
            if self.turn > 4:
                self.checkGame()

        self.retryMenu()


    def netGame(self):
        self.multiplayer = Multiplayer()
        self.netMenu()

        self.gameEnded = 0
        while not self.gameEnded:
            self.multiplayer.receiveData()
            self.countTurn()
            self.changePlayer()
            self.printASCIIgame()

            if(self.playerTurn == "X"): #for now that's the player that created game
                valid = False
                while valid == False:
                    if self.multiplayer.sendData((input(), input())) == 0:
                        valid = True

            if self.turn > 4:
                self.checkGame()

        self.retryMenu()

    def createGame(self):
        self.multiplayer.createServer()
        self.multiplayer.setConnection()

    def joinGame(self):
        self.multiplayer.setNetGame()
        self.multiplayer.joinServer()

    def menu(self):
        menu = {
            '1': self.localGame,
            '2': self.netGame
        }

        print("""
Select mode:
1 - local game
2 - net game (not implemented yet)
        """)

        print("game mode: ", end="")
        x = input()

        menu[x]()

    def retryMenu(self):
        menu = {
            't': self.localGame,
            'y': self.localGame,
            'n': sys.exit
        }

        print("Try again? [y/n]: ", end="")
        x = input()

        menu[x]()

    def netMenu(self):
        menu = {
            '1': self.createGame,
            '2': self.joinGame
        }

        print("""
Create or join game?
1 - create game
2 - join game
        """)

        print("choose: ", end="")
        x = input()

        menu[x]()

game = TicTacToe()
game.menu()