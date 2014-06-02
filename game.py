from pieces import Pawn, Knight, Bishop, Rook, Queen, King


class Game:

    def __init__(self):
        self.board = {'A8': Rook('A8', 'black'), 'B8': Knight('B8', 'black'), 'C8': Bishop('C8', 'black'), 'D8': King('D8', 'black'),
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
        self.current_player = 'white'
        self.next_player = 'black'
        self.turn_counter = 1

    @property
    def white_pieces(self):
        for col in 'ABCDEFGH':
            for row in '12345678':
                if self.board[col + row].color == 'white':
                    _white_pieces.append(self.board[col + row])
        return self._white_pieces

    @property
    def black_pieces(self):
        for col in 'ABCDEFGH':
            for row in '12345678':
                if self.board[col + row].color == 'black':
                    _white_pieces.append(self.board[col + row])
        return self._black_pieces

    def print_board(self):
        print('  A  B  C  D  E  F  G  H')
        counter = 8
        for row in range(8, 0, -1):
            print("{} ".format(counter), end='')
            for col in 'ABCDEFGH':
                address = col + str(row)
                if self.board[address] is None:
                    print('   ', end='')
                else:
                    print("{}".format(self.board[address].sign), end='')
            print("{}".format(counter))
            counter = counter - 1
        print('  A  B  C  D  E  F  G  H')

    def move(self, source, target):
        if self.board[source] is None:
            print("Invalid move!")
        if self.board[source].color != self.current_player:
            print("Invalid move!")
        if self.board[target] and \
                self.board[target].color == self.current_player:
                    print("Invalid move!")
        if self.board[source].move(target, self.board):
            self.board[target] = self.board[source]
            self.board[source] = None
        if self.current_player == 'black':
            self.turn_counter = self.turn_counter + 1
            self.current_player, self.next_player = self.next_player, self.current_player
        else:
            print("Invalid move!")
