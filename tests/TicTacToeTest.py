import unittest, sys
sys.path.append('..')
from games.TicTacToe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def testPlayerXwins(self):
        self.game.board = [['X','O','O'],['X','',''],['X', '', '']]
        self.game.playerTurn = self.game.cross
        self.assertEqual(self.game.checkGame(), "PlayerX wins!")

    def testPlayerOwins(self):
        self.game.board = [['O','X','X'],['O','',''],['O', '', '']]
        self.game.playerTurn = self.game.circle
        self.assertEqual(self.game.checkGame(), "PlayerO wins!")

if __name__ == '__main__':
    unittest.main()