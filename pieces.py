class Pawn:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.moved = False
        self.sign = 'P' + self.color[0]

    def calculate_vectors(self):
        if self.color == 'white':
            vectors = [(-1, 1), (0, 1), (1, 1), (0, 2)]
        else:
            vectors = [(-1, -1), (0, -1), (1, -1), (0, -2)]
        if self.moved:
            return vectors[:3]
        return vectors

    def is_valid_move(self, col, row, board):
        vectors = self.calculate_vectors()
        if col is None and row is None:
            return False
        vector = (col - self.col, row - self.row)
        if vector == vectors[0] or vector == vectors[2]:
            if board[col][row] is None or board[col][row].color == self.color:
                return False
            return True
        if self.col + vectors[1][0] < 0 or self.col + vectors[1][0] > 7 or \
           self.row + vectors[1][1] < 0 or self.row + vectors[1][1] > 7:
            return False
        if board[self.col + vectors[1][0]][self.row + vectors[1][1]] is not None:
            return False
        if vector in vectors:
            if board[col][row] is not None:
                return False
            return True
        return False

    def move(self, col, row, board):
        self.col, self.row, self.moved = col, row, True


class Knight:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.moved = False
        self.sign = 'N' + self.color[0]

    def calculate_vectors(self):
        return [(-2, 1), (-1, 2), (1, 2), (2, 1),
                (2, -1), (1, -2), (-1, -2), (-2, -1)]

    def is_valid_move(self, col, row, board):
        vectors = self.calculate_vectors()
        vector = (col - self.col, row - self.row)
        if vector in vectors and (board[col][row] is None or
           board[col][row].color != self.color):
            return True
        return False

    def move(self, col, row, board):
        self.col, self.row, self.moved = col, row, True


class Bishop:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.moved = False
        self.sign = 'B' + self.color[0]

    def calculate_vectors(self, col, row):
        vectors = []
        if abs(col - self.col) != abs(row - self.row):
            return vectors
        for step in range(1, abs(col - self.col)+1):
            if col > self.col and row > self.row:
                vectors.append((step, step))
            if col > self.col and row < self.row:
                vectors.append((step, -step))
            if col < self.col and row > self.row:
                vectors.append((-step, step))
            if col < self.col and row < self.row:
                vectors.append((-step, -step))
        return vectors

    def is_valid_move(self, col, row, board):
        vectors = self.calculate_vectors(col, row)
        vector = (col - self.col, row - self.row)
        if vector in vectors:
            for step in vectors:
                changed_col = self.col + step[0]
                changed_row = self.row + step[1]
                if board[changed_col][changed_row] is not None:
                    if changed_col == col and board[col][row].color != self.color:
                        return True
                    return False
            return True
        return False

    def move(self, col, row, board):
        self.col, self.row, self.moved = col, row, True


class Rook:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.moved = False
        self.sign = 'R' + self.color[0]

    def calculate_vectors(self, col, row):
        vectors = []
        if (col, row) == (self.col, self.row) or \
           (col != self.col and row != self.row):
            return vectors
        for step in range(1, max(abs(col-self.col), abs(row-self.row))+1):
            if col == self.col and row > self.row:
                vectors.append((0, step))
            if col == self.col and row < self.row:
                vectors.append((0, -step))
            if col < self.col and row == self.row:
                vectors.append((-step, 0))
            if col > self.col and row == self.row:
                vectors.append((step, 0))
        return vectors

    def is_valid_move(self, col, row, board):
        vectors = self.calculate_vectors(col, row)
        vector = (col - self.col, row - self.row)
        if vector in vectors:
            for step in vectors:
                changed_col = self.col + step[0]
                changed_row = self.row + step[1]
                if board[changed_col][changed_row] is not None:
                    if (changed_col, changed_row) == (col, row) and\
                       board[col][row].color != self.color:
                        return True
                    return False
            return True
        return False

    def move(self, col, row, board):
        self.col, self.row, self.moved = col, row, True


class Queen:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.moved = False
        self.sign = 'Q' + self.color[0]

    def calculate_vectors(self, col, row):
        vectors = []
        if abs(col - self.col) == abs(row - self.row):
            for step in range(1, abs(col - self.col)+1):
                if col > self.col and row > self.row:
                    vectors.append((step, step))
                if col > self.col and row < self.row:
                    vectors.append((step, -step))
                if col < self.col and row > self.row:
                    vectors.append((-step, step))
                if col < self.col and row < self.row:
                    vectors.append((-step, -step))
            return vectors
        if (col, row) == (self.col, self.row) or \
           (col != self.col and row != self.row):
            return vectors
        for step in range(1, max(abs(col-self.col), abs(row-self.row))+1):
            if col == self.col and row > self.row:
                vectors.append((0, step))
            if col == self.col and row < self.row:
                vectors.append((0, -step))
            if col < self.col and row == self.row:
                vectors.append((-step, 0))
            if col > self.col and row == self.row:
                vectors.append((step, 0))
        return vectors

    def is_valid_move(self, col, row, board):
        vectors = self.calculate_vectors(col, row)
        vector = (col - self.col, row - self.row)
        if vector in vectors:
            for step in vectors:
                changed_col = self.col + step[0]
                changed_row = self.row + step[1]
                if board[changed_col][changed_row] is not None:
                    if changed_col == col and changed_row == row and \
                       board[col][row].color != self.color:
                        return True
                    return False
            return True
        return False

    def move(self, col, row, board):
        self.col, self.row, self.moved = col, row, True


class King:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.moved = False
        self.sign = 'K' + self.color[0]

    def calculate_vectors(self, col, row):
        vectors = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1),
                   (-1, -1), (-1, 0), (2, 0), (-2, 0)]
        if self.moved:
            return vectors[:8]
        return vectors

    def long_castle(self, col, row, board):
        if (col - self.col, row - self.row) != (-2, 0):
            return False
        enemy = []
        for x in range(0, 8):
            for y in range(0, 8):
                square = board[x][y]
                if square is not None and square.color != self.color:
                    enemy.append(square)
        for piece in enemy:
            if piece.is_valid_move(self.col, self.row, board) or \
                    piece.is_valid_move(self.col-1, self.row, board):
                return False
        if self.moved or board[0][row].moved or board[1][row] is not None:
            return False
        return board[self.col-1][self.row] is None and \
            board[self.col - 2][self.row] is None

    def short_castle(self, col, row, board):
        if (col - self.col, row - self.row) != (2, 0):
            return False
        enemy = []
        for x in range(0, 8):
            for y in range(0, 8):
                square = board[x][y]
                if square is not None and square.color != self.color:
                    enemy.append(square)
        for piece in enemy:
                if piece.is_valid_move(self.col, self.row, board) or \
                   piece.is_valid_move(self.col+1, self.row, board):
                    return False
        if self.moved or board[7][row].moved:
            return False
        return board[self.col + 1][self.row] is None and board[self.col + 2][self.row] is None

    def is_valid_move(self, col, row, board):
        vectors = self.calculate_vectors(col, row)
        vector = (col - self.col, row - self.row)
        if vector not in vectors:
            return False
        if (self.short_castle(col, row, board) or
           self.long_castle(col, row, board)):
            return True
        if vector == (2, 0) or vector == (-2, 0):
            return False
        return board[col][row] is None or board[col][row].color != self.color

    def move(self, col, row, board):
        if self.short_castle(col, row, board):
            board[7][row].move(self.col+1, self.row, board)
            board[self.col+1][self.row] = board[7][row]
            board[7][row] = None
            board[self.col][self.row].col = self.col
            board[self.col][self.row].row = self.row
            board[self.col][self.row].moved = True
        if self.long_castle(col, row, board):
            board[0][row].move(self.col-1, self.row, board)
            board[self.col-1][self.row] = board[0][row]
            board[0][row] = None
            board[self.col-1][self.row].col = self.col - 1
            board[self.col-1][self.row].row = self.row
            board[self.col-1][self.row].moved = True
        self.col, self.row, self.moved = col, row, True
