import unittest
from pieces import Pawn,  Knight,  Bishop,  Rook,  Queen,  King


def print_board(board):
        print('  A  B  C  D  E  F  G  H')
        counter = 8
        for row in range(8, 0, -1):
            print("{} ".format(counter),  end='')
            for col in 'ABCDEFGH':
                address = col + str(row)
                if board[address] is None:
                    print('   ',  end='')
                else:
                    print("{}".format(board[address].sign),  end='')
            print("{}".format(counter))
            counter = counter - 1
        print('  A  B  C  D  E  F  G  H')


class PawnTest(unittest.TestCase):
    def test_is_valid_position_white(self):
        self.pawn = Pawn('B2',  'white')
        self.assertTrue(self.pawn.is_valid_position('A3'))
        self.assertTrue(self.pawn.is_valid_position('B3'))
        self.assertTrue(self.pawn.is_valid_position('B4'))
        self.assertTrue(self.pawn.is_valid_position('C3'))
        self.assertFalse(self.pawn.is_valid_position('C5'))
        self.assertFalse(self.pawn.is_valid_position('Q3'))
        self.assertFalse(self.pawn.is_valid_position('C9'))
        self.pawn.moved = True
        self.assertFalse(self.pawn.is_valid_position('B4'))

    def test_is_valid_position_black(self):
        self.pawn = Pawn('F7', 'black')
        self.assertTrue(self.pawn.is_valid_position('G6'))
        self.assertTrue(self.pawn.is_valid_position('F6'))
        self.assertTrue(self.pawn.is_valid_position('F5'))
        self.assertTrue(self.pawn.is_valid_position('E6'))
        self.assertFalse(self.pawn.is_valid_position('E5'))
        self.assertFalse(self.pawn.is_valid_position('Q3'))
        self.assertFalse(self.pawn.is_valid_position('C9'))
        self.pawn.moved = True
        self.assertFalse(self.pawn.is_valid_position('F5'))

    def test_is_valid_move(self):
        self.board = {'A8': Rook('A8', 'black'),  'B8': Knight('B8', 'black'), 'C8': Bishop('C8', 'black'), 'D8': King('D8', 'black'),
                      'E8': Queen('E8', 'black'), 'F8': Bishop('F8', 'black'), 'G8': Knight('G8', 'black'), 'H8': Rook('H8', 'black'),
                      'A7': Pawn('A7', 'black'), 'B7': Pawn('B7', 'black'), 'C7': Pawn('C7', 'black'), 'D7': Pawn('D7', 'black'),
                      'E7': Pawn('E7', 'black'), 'F7': Pawn('F7', 'black'), 'G7': Pawn('G7', 'black'), 'H7': Pawn('H7', 'black'),
                      'A6': Rook('A6', 'black'), 'B6': None, 'C6': Rook('C6',  'white'), 'D6': None, 'E6': None, 'F6': None, 'G6': None, 'H6': None,
                      'A5': None, 'B5': None, 'C5': None, 'D5': None, 'E5': None, 'F5': None, 'G5': None, 'H5': None,
                      'A4': None, 'B4': None, 'C4': None, 'D4': None, 'E4': None, 'F4': None, 'G4': None, 'H4': None,
                      'A3': None, 'B3': Bishop('B3', 'white'), 'C3': None, 'D3': Knight('D3', 'black'), 'E3': None, 'F3': None, 'G3': None, 'H3': None,
                      'A2': Pawn('A2', 'white'), 'B2': Pawn('B2', 'white'), 'C2': Pawn('C2', 'white'), 'D2': Pawn('D2', 'white'),
                      'E2': Pawn('E2', 'white'), 'F2': Pawn('F2', 'white'), 'G2': Pawn('G2', 'white'), 'H2': Pawn('H2', 'white'),
                      'A1': Rook('A1', 'white'), 'B1': Knight('B1', 'white'), 'C1': Bishop('C1', 'white'), 'D1': King('D1', 'white'),
                      'E1': Queen('E1', 'white'), 'F1': Bishop('F1', 'white'), 'G1': Knight('G1', 'white'), 'H1': Rook('H1', 'white')
                      }
        self.assertTrue(self.board['E2'].is_valid_move('D3', self.board))
        self.assertFalse(self.board['E2'].is_valid_move('F3', self.board))
        self.assertTrue(self.board['D7'].is_valid_move('C6', self.board))
        self.assertFalse(self.board['D7'].is_valid_move('E6', self.board))
        self.assertFalse(self.board['A2'].is_valid_move('B3', self.board))
        self.assertFalse(self.board['B7'].is_valid_move('A6', self.board))


class KnightTest(unittest.TestCase):
    def test_is_valid_position(self):
        self.knight = Knight('D4',  'white')
        self.assertTrue(self.knight.is_valid_position('E2'))
        self.assertTrue(self.knight.is_valid_position('C2'))
        self.assertTrue(self.knight.is_valid_position('B3'))
        self.assertTrue(self.knight.is_valid_position('B5'))
        self.assertTrue(self.knight.is_valid_position('C6'))
        self.assertTrue(self.knight.is_valid_position('E6'))
        self.assertTrue(self.knight.is_valid_position('F5'))
        self.assertTrue(self.knight.is_valid_position('F3'))
        self.assertFalse(self.knight.is_valid_position('Q2'))
        self.assertFalse(self.knight.is_valid_position('D9'))
        self.assertFalse(self.knight.is_valid_position('stuff'))

    def test_is_valid_move(self):
        self.board = {'A8': Rook('A8', 'black'),  'B8': Knight('B8', 'black'), 'C8': Bishop('C8', 'black'), 'D8': King('D8', 'black'),
                      'E8': Queen('E8', 'black'), 'F8': Bishop('F8', 'black'), 'G8': Knight('G8', 'black'), 'H8': Rook('H8', 'black'),
                      'A7': Pawn('A7', 'black'), 'B7': Pawn('B7', 'black'), 'C7': Pawn('C7', 'black'), 'D7': Pawn('D7', 'black'),
                      'E7': Pawn('E7', 'black'), 'F7': Pawn('F7', 'black'), 'G7': Pawn('G7', 'black'), 'H7': Pawn('H7', 'black'),
                      'A6': None, 'B6': None, 'C6': None, 'D6': None, 'E6': None, 'F6': None, 'G6': None, 'H6': None,
                      'A5': None, 'B5': None, 'C5': None, 'D5': None, 'E5': None, 'F5': None, 'G5': None, 'H5': None,
                      'A4': None, 'B4': None, 'C4': None, 'D4': None, 'E4': None, 'F4': None, 'G4': None, 'H4': None,
                      'A3': None, 'B3': None, 'C3': None, 'D3': None, 'E3': None, 'F3': None, 'G3': None, 'H3': None,
                      'A2': Pawn('A2', 'white'), 'B2': Pawn('B2', 'white'), 'C2': Pawn('C2', 'white'), 'D2': Pawn('D2', 'white'),
                      'E2': Pawn('E2', 'white'), 'F2': Pawn('F2', 'white'), 'G2': Pawn('G2', 'white'), 'H2': Pawn('H2', 'white'),
                      'A1': Rook('A1', 'white'), 'B1': Knight('B1', 'white'), 'C1': Bishop('C1', 'white'), 'D1': King('D1', 'white'),
                      'E1': Queen('E1', 'white'), 'F1': Bishop('F1', 'white'), 'G1': Knight('G1', 'white'), 'H1': Rook('H1', 'white')
                      }
        #print_board(self.board)

        self.assertTrue(self.board['B1'].is_valid_move('A3', self.board))
        self.assertTrue(self.board['B1'].is_valid_move('C3', self.board))
        self.assertTrue(self.board['G8'].is_valid_move('H6', self.board))
        self.assertTrue(self.board['G8'].is_valid_move('F6', self.board))
        self.assertFalse(self.board['G8'].is_valid_move('E7', self.board))


class BishopTest(unittest.TestCase):

    def test_is_valid_position(self):
        self.bishop = Bishop('B2', 'white')
        self.assertTrue(self.bishop.is_valid_position('C3'))
        self.assertTrue(self.bishop.is_valid_position('D4'))
        self.assertTrue(self.bishop.is_valid_position('E5'))
        self.assertTrue(self.bishop.is_valid_position('F6'))
        self.assertTrue(self.bishop.is_valid_position('G7'))
        self.assertTrue(self.bishop.is_valid_position('C1'))
        self.assertTrue(self.bishop.is_valid_position('A1'))
        self.assertTrue(self.bishop.is_valid_position('A3'))
        self.assertFalse(self.bishop.is_valid_position('Q2'))
        self.assertFalse(self.bishop.is_valid_position('D9'))
        self.assertFalse(self.bishop.is_valid_position('D3'))
        self.assertFalse(self.bishop.is_valid_position('stuff'))

    def test_is_valid_move(self):
        self.board = {'A8': None, 'B8': None, 'C8': None, 'D8': None, 'E8': None, 'F8': None, 'G8': None, 'H8': None,
                      'A7': None, 'B7': Knight('B7', 'white'), 'C7': None, 'D7': None, 'E7': None, 'F7': None, 'G7': None, 'H7': Rook('H7', 'white'),
                      'A6': None, 'B6': None, 'C6': None, 'D6': None, 'E6': None, 'F6': None, 'G6': Bishop('G6', 'black'), 'H6': None,
                      'A5': None, 'B5': None, 'C5': None, 'D5': None, 'E5': None, 'F5': None, 'G5': None, 'H5': None,
                      'A4': None, 'B4': None, 'C4': None, 'D4': None, 'E4': Bishop('E4', 'black'), 'F4': None, 'G4': None, 'H4': None,
                      'A3': None, 'B3': None, 'C3': None, 'D3': None, 'E3': None, 'F3': None, 'G3': None, 'H3': None,
                      'A2': None, 'B2': None, 'C2': Knight('C2', 'white'), 'D2': None, 'E2': None, 'F2': None, 'G2': Bishop('G2', 'black'), 'H2': None,
                      'A1': None, 'B1': Rook('B1', 'white'), 'C1': None, 'D1': None, 'E1': Knight('E1', 'white'), 'F1': None, 'G1': None, 'H1': None
                      }

        #print_board(self.board)

        self.assertTrue(self.board['E4'].is_valid_move('B7', self.board))
        self.assertFalse(self.board['E4'].is_valid_move('G6', self.board))
        self.assertTrue(self.board['E4'].is_valid_move('C2', self.board))
        self.assertTrue(self.board['E4'].is_valid_move('C6', self.board))
        self.assertFalse(self.board['E4'].is_valid_move('H7', self.board))
        self.assertFalse(self.board['E4'].is_valid_move('G2', self.board))
        self.assertFalse(self.board['E4'].is_valid_move('E1', self.board))
        self.assertFalse(self.board['E4'].is_valid_move('B1', self.board))
        self.assertFalse(self.board['E4'].is_valid_move('H1', self.board))


class RookTest(unittest.TestCase):

    def test_is_valid_position(self):
        self.rook = Rook('D4',  'white')
        self.assertTrue(self.rook.is_valid_position('D2'))
        self.assertTrue(self.rook.is_valid_position('C4'))
        self.assertTrue(self.rook.is_valid_position('A4'))
        self.assertTrue(self.rook.is_valid_position('D1'))
        self.assertTrue(self.rook.is_valid_position('G4'))
        self.assertTrue(self.rook.is_valid_position('D8'))
        self.assertFalse(self.rook.is_valid_position('F3'))
        self.assertFalse(self.rook.is_valid_position('Q2'))
        self.assertFalse(self.rook.is_valid_position('D9'))
        self.assertFalse(self.rook.is_valid_position('stuff'))

    def test_is_valid_move(self):
        self.board = {'A8': None, 'B8': None, 'C8': None, 'D8': None, 'E8': None, 'F8': None, 'G8': None, 'H8': None,
                      'A7': None, 'B7': None, 'C7': None, 'D7': None, 'E7': None, 'F7': None, 'G7': None, 'H7': None,
                      'A6': None, 'B6': None, 'C6': None, 'D6': None, 'E6': None, 'F6': Queen('F6', 'white'), 'G6': None, 'H6': None,
                      'A5': None, 'B5': None, 'C5': None, 'D5': None, 'E5': None, 'F5': None, 'G5': None, 'H5': None,
                      'A4': Pawn('A4', 'black'), 'B4': None, 'C4': Bishop('C4', 'black'), 'D4': Rook('D4', 'white'), 'E4': None, 'F4': Bishop('F4', 'white'), 'G4': None, 'H4': King('H4', 'black'),
                      'A3': None, 'B3': None, 'C3': None, 'D3': None, 'E3': None, 'F3': None, 'G3': None, 'H3': None,
                      'A2': None, 'B2': None, 'C2': None, 'D2': Bishop('D2', 'white'), 'E2': None, 'F2': None, 'G2': None, 'H2': None,
                      'A1': None, 'B1': None, 'C1': None, 'D1': Rook('D1', 'black'), 'E1': None, 'F1': None, 'G1': Bishop('G1', 'black'), 'H1': None
                      }
        self.assertTrue(self.board['D4'].is_valid_move('C4', self.board))
        self.assertTrue(self.board['D4'].is_valid_move('D7', self.board))
        self.assertFalse(self.board['D4'].is_valid_move('D1', self.board))
        self.assertFalse(self.board['D4'].is_valid_move('A4', self.board))
        self.assertFalse(self.board['D4'].is_valid_move('G1', self.board))
        self.assertFalse(self.board['D4'].is_valid_move('F4', self.board))


class QueenTest(unittest.TestCase):
    def test_is_valid_position(self):
        self.queen = Queen('D4',  'white')
        self.assertTrue(self.queen.is_valid_position('H8'))
        self.assertTrue(self.queen.is_valid_position('G7'))
        self.assertTrue(self.queen.is_valid_position('B6'))
        self.assertTrue(self.queen.is_valid_position('D6'))
        self.assertTrue(self.queen.is_valid_position('E4'))
        self.assertTrue(self.queen.is_valid_position('F4'))
        self.assertTrue(self.queen.is_valid_position('G4'))
        self.assertTrue(self.queen.is_valid_position('B2'))
        self.assertTrue(self.queen.is_valid_position('F2'))
        self.assertFalse(self.queen.is_valid_position('Q2'))
        self.assertFalse(self.queen.is_valid_position('D9'))
        self.assertFalse(self.queen.is_valid_position('G5'))
        self.assertFalse(self.queen.is_valid_position('C8'))
        self.assertFalse(self.queen.is_valid_position('stuff'))

    def test_is_valid_move(self):
        self.board = {'A8': None, 'B8': None, 'C8': None, 'D8': None, 'E8': None, 'F8': None, 'G8': None, 'H8': Bishop('H8', 'white'),
                      'A7': None, 'B7': None, 'C7': None, 'D7': None, 'E7': None, 'F7': None, 'G7': Pawn('G7', 'white'), 'H7': None,
                      'A6': None, 'B6': Bishop('B6', 'black'), 'C6': None, 'D6': Rook('D6', 'white'), 'E6': None, 'F6': None, 'G6': None, 'H6': None,
                      'A5': None, 'B5': None, 'C5': None, 'D5': None, 'E5': None, 'F5': None, 'G5': None, 'H5': None,
                      'A4': None, 'B4': None, 'C4': None, 'D4': Queen('D4', 'black'), 'E4': Rook('E4', 'white'), 'F4': None, 'G4': Pawn('G4', 'white'), 'H4': None,
                      'A3': None, 'B3': None, 'C3': None, 'D3': None, 'E3': None, 'F3': None, 'G3': None, 'H3': None,
                      'A2': None, 'B2': Queen('B2', 'white'), 'C2': None, 'D2': None, 'E2': None, 'F2': Rook('F2', 'white'), 'G2': None, 'H2': None,
                      'A1': None, 'B1': None, 'C1': None, 'D1': Knight('D1', 'white'), 'E1': None, 'F1': None, 'G1': None, 'H1': None
                      }

        self.assertFalse(self.board['D4'].is_valid_move('H8', self.board))
        self.assertTrue(self.board['D4'].is_valid_move('G7', self.board))
        self.assertFalse(self.board['D4'].is_valid_move('B6', self.board))
        self.assertTrue(self.board['D4'].is_valid_move('D6', self.board))
        self.assertTrue(self.board['D4'].is_valid_move('E4', self.board))
        self.assertFalse(self.board['D4'].is_valid_move('F4', self.board))
        self.assertFalse(self.board['D4'].is_valid_move('G4', self.board))
        self.assertTrue(self.board['D4'].is_valid_move('B2', self.board))
        self.assertTrue(self.board['D4'].is_valid_move('F2', self.board))
        self.assertTrue(self.board['D4'].is_valid_move('D1', self.board))
        self.assertFalse(self.board['D4'].is_valid_move('F1', self.board))
        self.assertFalse(self.board['D4'].is_valid_move('G1', self.board))
        self.assertFalse(self.board['D4'].is_valid_move('A7', self.board))
        self.assertTrue(self.board['D4'].is_valid_move('C4', self.board))


class KingTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
