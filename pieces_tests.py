import unittest
from pieces import Pawn,  Knight,  Bishop,  Rook,  Queen,  King

class PawnTest(unittest.TestCase):

    def test_is_valid_move(self):
        board =[
            [Rook(0,0,'white'),Pawn(0,1,'white'),None,None,None,None,Pawn(0,6,'black'),Rook(0,7,'black')],
            [Knight(1,0,'white'),Pawn(1,1,'white'),None,None,None,None,Pawn(1,6,'black'),Knight(1,7,'black')],
            [Bishop(2,0,'white'),Pawn(2,1,'white'),Pawn(2,2,'white'),None,None,None,Pawn(2,6,'black'),Bishop(2,7,'black')],
            [Queen(3,0,'white'),Pawn(3,1,'white'),None,None,None,None,Pawn(3,6,'black'),Queen(3,7,'black')],
            [King(4,0,'white'),Pawn(4,1,'white'),None,None,None,None,Pawn(4,6,'black'),King(4,7,'black')],
            [Bishop(5,0,'white'),Pawn(5,1,'white'),None,None,None,None,Pawn(5,6,'black'),Bishop(5,7,'black')],
            [Knight(6,0,'white'),Pawn(6,1,'white'),None,None,None,Bishop(6,5,'white'),Pawn(6,6,'black'),Knight(6,7,'black')],
            [Rook(7,0,'white'),Pawn(7,1,'white'),None,None,None,None,Pawn(7,6,'black'),Rook(7,7,'black')]
        ]
        
        self.assertTrue(board[5][1].is_valid_move(5,2,board))
        self.assertTrue(board[5][1].is_valid_move(5,3,board))
        self.assertFalse(board[7][1].is_valid_move(9,2,board))
        self.assertFalse(board[2][1].is_valid_move(1,1,board))
        self.assertFalse(board[4][1].is_valid_move(5,2,board))
        self.assertFalse(board[5][1].is_valid_move(4,3,board))
        self.assertTrue(board[0][6].is_valid_move(0,4,board))
        self.assertFalse(board[4][6].is_valid_move(3,5,board))
        self.assertTrue(board[2][6].is_valid_move(2,5,board))
        board[7][6].moved  = True
        self.assertFalse(board[7][6].is_valid_move(7,4,board))
        self.assertFalse(board[2][1].is_valid_move(2,3,board))
        self.assertFalse(board[1][1].is_valid_move(2,3,board))
        self.assertTrue(board[5][6].is_valid_move(6,5,board))
        self.assertTrue(board[7][6].is_valid_move(6,5,board))


class KnightTest(unittest.TestCase):

    def test_is_valid_move(self):

        board =[
            [Rook(0,0,'white'),Pawn(0,1,'white'),Bishop(0,2,'black'),None,None,None,Pawn(0,6,'black'),Rook(0,7,'black')],
            [Knight(1,0,'white'),Pawn(1,1,'white'),None,None,None,None,Pawn(1,6,'black'),Knight(1,7,'black')],
            [Bishop(2,0,'white'),Pawn(2,1,'white'),None,None,None,None,Pawn(2,6,'black'),Bishop(2,7,'black')],
            [Queen(3,0,'white'),Pawn(3,1,'white'),None,None,None,None,Pawn(3,6,'black'),Queen(3,7,'black')],
            [King(4,0,'white'),Pawn(4,1,'white'),None,None,None,None,Pawn(4,6,'black'),King(4,7,'black')],
            [Bishop(5,0,'white'),Pawn(5,1,'white'),None,None,None,None,Pawn(5,6,'black'),Bishop(5,7,'black')],
            [Knight(6,0,'white'),Pawn(6,1,'white'),None,None,None,None,Pawn(6,6,'black'),Knight(6,7,'black')],
            [Rook(7,0,'white'),Pawn(7,1,'white'),None,None,None,None,Pawn(7,6,'black'),Rook(7,7,'black')]
        ]
        self.assertTrue(board[6][0].is_valid_move(5,2,board))
        self.assertFalse(board[6][0].is_valid_move(4,1,board))
        self.assertFalse(board[1][7].is_valid_move(5,2,board))
        self.assertTrue(board[1][7].is_valid_move(2,5,board))
        self.assertFalse(board[6][0].is_valid_move(0,2,board))
        self.assertFalse(board[6][7].is_valid_move(4,6,board))
        self.assertTrue(board[1][0].is_valid_move(0,2,board))
        self.assertFalse(board[6][0].is_valid_move(7,7,board))

class BishopTest(unittest.TestCase):

    def test_is_valid_move(self):
        board =[
            [Rook(0,0,'white'),Pawn(0,1,'white'),Pawn(0,2,'white'),None,None,None,Pawn(0,6,'black'),Rook(0,7,'black')],
            [Knight(1,0,'white'),Pawn(1,1,'white'),None,None,None,None,Pawn(1,6,'black'),Knight(1,7,'black')],
            [Bishop(2,0,'white'),Pawn(2,1,'white'),None,None,None,None,Pawn(2,6,'black'),Bishop(2,7,'black')],
            [Queen(3,0,'white'),None,None,None,None,None,Pawn(3,6,'black'),Queen(3,7,'black')],
            [King(4,0,'white'),Pawn(4,1,'white'),None,None,None,None,Pawn(4,6,'black'),King(4,7,'black')],
            [Bishop(5,0,'white'),Pawn(5,1,'white'),None,Pawn(5,3,'white'),None,None,Pawn(5,6,'black'),Bishop(5,7,'black')],
            [Knight(6,0,'white'),Pawn(6,1,'white'),None,None,None,None,None,Knight(6,7,'black')],
            [Rook(7,0,'white'),Pawn(7,1,'white'),None,None,None,Knight(7,5,'white'),Pawn(7,6,'black'),Rook(7,7,'black')]
        ]
        self.assertTrue(board[2][0].is_valid_move(3,1,board))
        self.assertTrue(board[2][0].is_valid_move(4,2,board))
        self.assertFalse(board[2][0].is_valid_move(7,5,board))
        self.assertFalse(board[2][0].is_valid_move(1,1,board))
        self.assertFalse(board[2][0].is_valid_move(5,3,board))
        self.assertFalse(board[1][7].is_valid_move(4,4,board))
        self.assertTrue(board[5][7].is_valid_move(7,5,board))
        self.assertFalse(board[5][7].is_valid_move(0,2,board))
        self.assertFalse(board[5][7].is_valid_move(6,7,board))






class RookTest(unittest.TestCase):

    def test_is_valid_move(self):
        board =[
            [Rook(0,0,'white'),Pawn(0,1,'white'),None,None,None,None,None,Rook(0,7,'black')],
            [Knight(1,0,'white'),Pawn(1,1,'white'),None,None,None,None,Pawn(1,6,'black'),Knight(1,7,'black')],
            [Bishop(2,0,'white'),Pawn(2,1,'white'),None,None,None,None,Pawn(2,6,'black'),Bishop(2,7,'black')],
            [Queen(3,0,'white'),Pawn(3,1,'white'),None,None,None,None,Pawn(3,6,'black'),Queen(3,7,'black')],
            [King(4,0,'white'),Pawn(4,1,'white'),None,None,None,None,Pawn(4,6,'black'),King(4,7,'black')],
            [Bishop(5,0,'white'),Pawn(5,1,'white'),None,None,None,None,Pawn(5,6,'black'),Bishop(5,7,'black')],
            [Knight(6,0,'white'),Pawn(6,1,'white'),None,None,None,None,Pawn(6,6,'black'),Knight(6,7,'black')],
            [Rook(7,0,'white'),None,None,None,None,None,Pawn(7,6,'black'),Rook(7,7,'black')]
        ]
        self.assertTrue(board[7][0].is_valid_move(7,6,board))
        self.assertFalse(board[7][0].is_valid_move(7,7,board))
        self.assertFalse(board[0][0].is_valid_move(0,7,board))
        self.assertFalse(board[7][7].is_valid_move(1,7,board))
        self.assertFalse(board[7][0].is_valid_move(5,1,board))
        self.assertTrue(board[0][7].is_valid_move(0,6,board))

class QueenTest(unittest.TestCase):

    def test_is_valid_move(self):
        board = [
        [None,None,None,None,None,None,None,None],
        [None,Bishop(1,1,'white'),None,None,Rook(1,4,'black'),None,None,None],
        [None,None,Pawn(2,2,'white'),None,None,None,Knight(2,6,'white'),None],
        [Knight(3,0,'white'), None,None,Queen(3,3,'black'),Pawn(3,4,'black'), None,None,Bishop(3,7,'white')],
        [None,None,None,Queen(4,3,'white'),None,None,None, None],
        [None,None,None,None,None,None,None,None],
        [Rook(6,0,'black'), Bishop(6,1,'black'), Pawn(6,2,'black'),None,None,None,None,None],
        [None,None,None,None,None,None,None,None,]
        ]
        self.assertTrue(board[3][3].is_valid_move(3,0,board))
        self.assertFalse(board[3][3].is_valid_move(3,4,board))
        self.assertFalse(board[3][3].is_valid_move(3,7,board))
        self.assertTrue(board[3][3].is_valid_move(4,3,board))
        self.assertTrue(board[3][3].is_valid_move(4,4,board))
        self.assertTrue(board[3][3].is_valid_move(6,6,board))
        self.assertTrue(board[3][3].is_valid_move(2,2,board))
        self.assertFalse(board[3][3].is_valid_move(1,1,board))
        self.assertTrue(board[4][3].is_valid_move(6,1,board))
        self.assertFalse(board[4][3].is_valid_move(0,3,board))

class KingTest(unittest.TestCase):

    def test_is_valid_move(self):
        
        board =[
            [Rook(0,0,'white'),Pawn(0,1,'white'),None,None,None,None,Pawn(0,6,'black'),Rook(0,7,'black')],
            [None,Pawn(1,1,'white'),None,None,None,None,Pawn(1,6,'black'),Knight(1,7,'black')],
            [None,Pawn(2,1,'white'),None,None,None,None,Pawn(2,6,'black'),Bishop(2,7,'black')],
            [None,Pawn(3,1,'white'),None,None,None,None,Pawn(3,6,'black'),Queen(3,7,'black')],
            [King(4,0,'white'),None,None,None,None,None,Pawn(4,6,'black'),King(4,7,'black')],
            [Bishop(5,0,'white'),Pawn(5,1,'white'),None,None,None,None,Pawn(5,6,'black'),None],
            [Knight(6,0,'white'),Pawn(6,1,'white'),None,None,None,None,Pawn(6,6,'black'),None],
            [Rook(7,0,'white'),Pawn(7,1,'white'),None,None,None,None,Pawn(7,6,'black'),Rook(7,7,'black')]
        ]
        
        self.assertTrue(board[4][0].is_valid_move(2,0,board))
        self.assertTrue(board[4][0].is_valid_move(3,0,board))
        self.assertTrue(board[4][0].is_valid_move(4,1,board))
        self.assertFalse(board[4][0].is_valid_move(5,2,board))
        self.assertFalse(board[4][0].is_valid_move(6,0,board))
        self.assertTrue(board[4][7].is_valid_move(6,7,board))
        self.assertFalse(board[4][7].is_valid_move(6,5,board))
        board[3][7] = Queen(3,7,'white')
        self.assertTrue(board[4][7].is_valid_move(3,7,board))
        board[3][7] = Queen(3,7,'black')
        board[0][0].moved = True
        self.assertFalse(board[4][0].is_valid_move(2,0,board))
        board[0][0].moved = False
        board[4][0].moved = True
        self.assertFalse(board[4][0].is_valid_move(2,0,board))
        board[4][0].moved = False
        board[7][7].moved = True
        self.assertFalse(board[4][7].is_valid_move(6,7,board))
        board[7][7].moved = False
        board[4][7].moved = True
        self.assertFalse(board[4][7].is_valid_move(6,7,board))
        board[1][0] = Knight(1,0,'white')
        self.assertFalse(board[4][0].is_valid_move(2,0,board))
        #printb(board)

        board =[
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [King(4,0,'white'),None,King(4,2,'black'),None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
        ]
        self.assertTrue(board[4][0].is_valid_move(4,1,board))
        self.assertTrue(board[4][0].is_valid_move(3,1,board))
        self.assertTrue(board[4][0].is_valid_move(5,1,board))







if __name__ == '__main__':
    unittest.main()
