import unittest
from copy import deepcopy
from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from game import Game

class GameTest(unittest.TestCase):
    
    def test_game(self):
        game = Game()
        game.move('e2','e4')
        self.assertTrue(game.current_player == 'black')
        self.assertTrue(game.turn_counter == 2)
        self.assertTrue(game.board[4][1] is None)
        self.assertTrue(game.board[4][3].col == 4 and game.board[4][3].row == 3)
        self.assertFalse(game.board[4][3].moved == False)
        self.assertTrue(game.move('d7','d6'))
        self.assertTrue(game.move('d2','d4'))
        self.assertTrue(game.move('g8','f6'))
        self.assertTrue(game.move('b1','c3'))
        self.assertTrue(game.move('g7','g6'))
        self.assertTrue(game.move('c1','e3'))
        self.assertTrue(game.move('f8','g7'))
        self.assertTrue(game.move('d1','d2'))
        self.assertTrue(game.move('c7','c6'))
        self.assertTrue(game.board[2][5].col == 2 and game.board[2][5].row == 5)
        self.assertTrue(game.move('f2','f3'))
        self.assertTrue(game.move('b7','b5'))
        self.assertTrue(game.move('g1','e2'))
        self.assertTrue(game.move('b8','d7'))
        self.assertTrue(game.move('e3','h6'))
        self.assertTrue(game.move('g7','h6'))
        self.assertTrue(game.move('d2','h6'))
        self.assertTrue(game.move('c8','b7'))
        self.assertTrue(game.move('a2','a3'))
        self.assertTrue(game.move('e7','e5'))
        self.assertTrue(game.move('e1','c1'))
        self.assertTrue(game.move('d8','e7'))
        self.assertTrue(game.move('c1','b1'))
        self.assertTrue(game.move('a7','a6'))
        self.assertTrue(game.move('e2','c1'))
        self.assertFalse(game.current_player == 'white')
        self.assertTrue(game.move('e8','c8'))
        self.assertTrue(game.move('c1','b3'))
        self.assertTrue(game.move('e5','d4'))
        self.assertTrue(game.move('d1','d4'))
        self.assertTrue(game.move('c6','c5'))
        self.assertTrue(game.move('d4','d1'))
        self.assertTrue(game.move('d7','b6'))
        self.assertTrue(game.move('g2','g3'))
        self.assertTrue(game.move('c8','b8'))
        self.assertTrue(game.move('b3','a5'))
        self.assertTrue(game.move('b7','a8'))
        self.assertTrue(game.move('f1','h3'))
        self.assertTrue(game.move('d6','d5'))
        self.assertTrue(game.move('h6','f4'))#дава се шах на черните
        self.assertFalse(not game.king_in_check(game.current_player,game.board))
        
        self.assertTrue(game.move('b8','a7'))
        
        self.assertTrue(game.move('h1','e1'))
        self.assertTrue(game.move('d5','d4'))
        self.assertTrue(game.move('c3','d5'))
        self.assertTrue(game.move('b6','d5'))
        self.assertTrue(game.move('e4','d5'))
        self.assertTrue(game.move('e7','d6'))
        self.assertTrue(game.move('d1','d4'))
        self.assertTrue(game.move('c5','d4'))
        self.assertTrue(game.move('e1','e7'))#шах на верните
        self.assertTrue(game.current_player == 'black')
        self.assertTrue(game.move('a7','b6'))
        self.assertTrue(game.move('f4','d4'))
        self.assertTrue(game.move('b6','a5'))
        self.assertTrue(game.move('b2','b4'))#шах на черните
        self.assertTrue(game.current_player == 'black')
        self.assertTrue(game.move('a5','a4'))
        self.assertTrue(game.move('d4','c3'))
        self.assertTrue(game.move('d6','d5'))
        self.assertTrue(game.move('e7','a7'))
        
        self.assertTrue(game.move('a8','b7'))
        self.assertTrue(game.move('a7','b7'))
        self.assertTrue(game.move('d5','c4'))
        self.assertTrue(game.move('c3','f6'))
        self.assertTrue(game.move('a4','a3'))
        self.assertTrue(game.move('f6','a6'))#шах на черните
        self.assertTrue(game.move('a3','b4'))
        self.assertTrue(game.move('c2','c3'))
        self.assertTrue(game.move('b4','c3'))
        self.assertTrue(game.move('a6','a1'))
        self.assertTrue(game.move('c3','d2'))
        self.assertTrue(game.current_player == 'white')
        self.assertTrue(game.move('a1','b2'))#шах на черните
        self.assertTrue(game.move('d2','d1'))
        self.assertTrue(game.move('h3','f1'))
        self.assertTrue(game.move('d8','d2'))
        self.assertTrue(game.move('b7','d7'))

        self.assertTrue(game.move('d2','d7'))
        self.assertTrue(game.move('f1','c4'))
        self.assertTrue(game.move('b5','c4'))
        self.assertTrue(game.move('b2','h8'))
        self.assertTrue(game.move('d7','d3'))
        self.assertTrue(game.move('h8','a8'))

        self.assertTrue(game.move('c4','c3'))

        self.assertTrue(game.move('a8','a4'))
        
        self.assertTrue(game.move('d1','e1'))
        self.assertTrue(game.move('f3','f4'))
        self.assertTrue(game.move('f7','f5'))
        self.assertTrue(game.move('b1','c1'))
        self.assertTrue(game.move('d3','d2'))
        self.assertTrue(game.move('a4','a7'))


    def test_stalemate(self):
        game = Game()
        game.board[2][3] = Bishop(2,3,'white')
        game.board[0][5] = None
        game.board[3][0] = None
        game.board[5][6] = Queen(5,6,'white')
        game.board[4][1] = None
        game.board[4][3] = Pawn(4,3,'white')
        game.board[4][4] = Pawn(4,4,'black')
        game.board[4][6] = None
        game.board[0][5] = Pawn(0,5,'black')
        game.board[0][6] = None
        game.board[7][5] = Pawn(7,5,'black')
        game.board[7][6] = None
        game.current_player = 'black'
        game.next_player = 'white'
        #printb(game.board)
        game.backup_board = deepcopy(game.board)
        self.assertTrue(game.stalemate())
        #self.assertTrue(game.king_in_check(game.current_player, game.backup_board))        

    def test_material_stalemata_kings(self):
        game = Game()
        for x in range(0,8):
            for y in range(0,8):
                game.board[x][y] = None

        
        
        game.board[3][0] = King(3,0,'white')
        
        game.board[7][2] = King(7,2,'black')
        game.backup_board = deepcopy(game.board)
        #printb(game.board)
        self.assertTrue(game.material_stalemate())


    def test_material_stalemate_bishops(self):
        game = Game()
        for x in range(0,8):
            for y in range(0,8):
                game.board[x][y] = None

        game.board[0][0] = Bishop(0,0,'white')
        game.board[2][0] = Bishop(2,0,'white')
        game.board[3][0] = King(3,0,'white')
        game.board[4][0] = Bishop(4,0,'black')
        game.board[6][0] = Bishop(6,0,'black')
        game.board[7][2] = King(7,2,'black')
        game.backup_board = deepcopy(game.board)
        #printb(game.board)
        self.assertTrue(game.material_stalemate())

        game.board[4][4] = Knight(4,4,'black')
        game.backup_board = deepcopy(game.board)
        self.assertFalse(game.material_stalemate())

    def test_material_stalemate_knights(self):
        game = Game()
        for x in range(0,8):
            for y in range(0,8):
                game.board[x][y] = None

        
        
        game.board[3][0] = King(3,0,'white')
        
        game.board[7][2] = King(7,2,'black')

        
        game.board[0][0] = Knight(0,0,'white')
        
        game.backup_board = deepcopy(game.board)
        self.assertTrue(game.material_stalemate())

        game.board[4][4] = Knight(4,4,'black')
        game.backup_board = deepcopy(game.board)
        self.assertFalse(game.material_stalemate())

        game.board[7][0] = Knight(7,0,'black')
        game.backup_board = deepcopy(game.board)
        self.assertFalse(game.material_stalemate())



if __name__ == '__main__':
    unittest.main()
