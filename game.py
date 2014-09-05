from copy import deepcopy
from pieces import Pawn,  Rook,  Knight,  Bishop,  King,  Queen


class Game:

    def __init__(self):
        self.board = [
            [Rook(0, 0, 'white'), Pawn(0, 1, 'white'), None, None,
             None, None, Pawn(0, 6, 'black'), Rook(0, 7, 'black')],
            [Knight(1, 0, 'white'), Pawn(1, 1, 'white'), None, None,
             None, None, Pawn(1, 6, 'black'), Knight(1, 7, 'black')],
            [Bishop(2, 0, 'white'), Pawn(2, 1, 'white'), None, None,
             None, None, Pawn(2, 6, 'black'), Bishop(2, 7, 'black')],
            [Queen(3, 0, 'white'), Pawn(3, 1, 'white'), None, None,
             None, None, Pawn(3, 6, 'black'), Queen(3, 7, 'black')],
            [King(4, 0, 'white'), Pawn(4, 1, 'white'), None, None,
             None, None, Pawn(4, 6, 'black'), King(4, 7, 'black')],
            [Bishop(5, 0, 'white'), Pawn(5, 1, 'white'), None, None,
             None, None, Pawn(5, 6, 'black'), Bishop(5, 7, 'black')],
            [Knight(6, 0, 'white'), Pawn(6, 1, 'white'), None, None,
             None, None, Pawn(6, 6, 'black'), Knight(6, 7, 'black')],
            [Rook(7, 0, 'white'), Pawn(7, 1, 'white'), None, None,
             None, None, Pawn(7, 6, 'black'), Rook(7, 7, 'black')]
        ]
        self.backup_board = None
        self.current_player = 'white'
        self.next_player = 'black'
        self.turn_counter = 1

    def white_pieces(self):
        whites = []
        if self.backup_board is None:
            return None
        for x in range(0, 8):
            for y in range(0, 8):
                square = self.backup_board[x][y]
                if square is not None and square.color == 'white':
                    whites.append(self.backup_board[x][y])
        return whites

    def black_pieces(self):
        blacks = []
        if self.backup_board is None:
            return None
        for x in range(0, 8):
            for y in range(0, 8):
                square = self.backup_board[x][y]
                if square is not None and square.color == 'black':
                    blacks.append(self.backup_board[x][y])
        return blacks

    def king_in_check(self, player, board):
        if player == 'white':
            ally = self.white_pieces()
            enemy = self.black_pieces()
        elif player == 'black':
            ally = self.black_pieces()
            enemy = self.white_pieces()

        if ally is None or enemy is None:
            return False
        for piece in ally:
            if isinstance(piece, King):
                king_col = piece.col
                king_row = piece.row
        for att in enemy:
            if att.is_valid_move(king_col, king_row, board):
                return True
        return False

    def calculate_coords(self, source,  target):
        source_col = ord(source[0].upper()) - 65
        source_row = int(source[1]) - 1
        target_col = ord(target[0].upper()) - 65
        target_row = int(target[1]) - 1
        return (source_col, source_row, target_col, target_row)

    def stalemate(self):
        if self.current_player == 'black':
            ally = self.black_pieces()
        else:
            ally = self.white_pieces()
        if ally is None:
            return False

        for piece in ally:
            for letter in 'ABCDEFGH':
                for number in '12345678':
                    self.backup_board = deepcopy(self.board)
                    test_board = deepcopy(self.board)
                    address = chr(piece.col + ord('A')) + str(piece.row + 1)
                    if self.move(address, letter + number)and not \
                    self.king_in_check(self.current_player, self.backup_board):
                        swap = self.current_player
                        self.current_player = self.next_player
                        self.next_player = swap
                        self.turn_counter = self.turn_counter - 1
                        self.board = deepcopy(test_board)
                        return False
                    elif self.move(address, letter + number):
                        self.board = deepcopy(test_board)
                        swap = self.current_player
                        self.current_player = self.next_player
                        self.next_player = swap
                        self.turn_counter = self.turn_counter - 1
        return True

    def material_stalemate(self):
        whites = self.white_pieces()
        blacks = self.black_pieces()
        w_marker = self.poor_material(whites)
        b_marker = self.poor_material(blacks)
        if w_marker and b_marker:
            if w_marker == 1 or b_marker == 1:
                return True
            elif w_marker + b_marker in (4, 5):
                return False
            for w_piece in whites:
                if isinstance(w_piece, Bishop):
                    for b_piece in blacks:
                        if isinstance(b_piece, Bishop):
                            return self.square_color(w_piece.col,  w_piece.row) == \
                                self.square_color(b_piece.col,  b_piece.row)
        return False

    def poor_material(self, collection):
        if len(collection) == 1:
            return 1
        elif len(collection) == 2:
            if isinstance(collection[0],  Knight) or \
                isinstance(collection[1],  Knight):
                return 2
            elif isinstance(collection[0],  Bishop) or \
                isinstance(collection[1],  Bishop):
                return 3
        else:
            compare = None
            for element in collection:
                if not (isinstance(element, King) or
                isinstance(element, Bishop)):
                    return False
                elif isinstance(element,  Bishop):
                    if compare is None:
                        compare = self.square_color(element.col, element.row)
                    elif compare != self.square_color(element.col, element.row):
                        return False
            return 3

    def square_color(self, col,  row):
        if col % 2 == 0 and row % 2 == 0:
            color = 'white'
        if col % 2 == 0 and row % 2 != 0:
            color = 'black'
        if col % 2 != 0 and row % 2 == 0:
            color = 'black'
        if col % 2 != 0 and row % 2 != 0:
            color = 'white'
        return color

    def promotion(self, source, target):
        coords = self.calculate_coords(source, target)
        target_col,  target_row = coords[2],  coords[3]
        if isinstance(self.board[target_col][target_row], Pawn):
            if target_row == 0 or target_row == 7:
                return True
        return False

    def move(self, source, target):
        coords = self.calculate_coords(source, target)
        source_col, source_row = coords[0], coords[1]
        target_col, target_row = coords[2], coords[3]
        if source_col < 0 or source_col > 7 or \
            source_row < 0 or source_row > 7 or \
            target_col < 0 or target_col > 7 or \
            target_row < 0 or target_row > 7:
            return False
        if self.board[source_col][source_row] is None:
            return False
        if self.current_player != self.board[source_col][source_row].color:
            return False
        self.backup_board = deepcopy(self.board)
        if self.backup_board[source_col][source_row]. \
         is_valid_move(target_col, target_row, self.backup_board):
            self.backup_board[source_col][source_row]. \
                move(target_col, target_row, self.backup_board)
            self.backup_board[target_col][target_row] = \
                self.backup_board[source_col][source_row]
            self.backup_board[source_col][source_row] = None
            if self.king_in_check(self.current_player, self.backup_board):
                return False
            else:
                self.board = deepcopy(self.backup_board)
                swap = self.current_player 
                self.current_player = self.next_player
                self.next_player = swap
                self.turn_counter = self.turn_counter + 1
        else:
            return False
        return True
