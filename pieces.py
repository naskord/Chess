class Pawn:
    def __init__(self, position, color):
        self.position = position
        self.previous_position = None
        self.color = color
        self.moved = False
        self.sign = 'P' + self.color[0] + ' '

    def is_valid_position(self, position):
        if position[0].upper() < 'A' or \
            position[0].upper() > 'H' or \
                int(position[1]) < 1 or int(position[1]) > 8:
                    return False
        if self.color == 'white' and self.moved:
            return position == chr(ord(self.position[0]) + 1) + str(int(self.position[1]) + 1) or \
                position == chr(ord(self.position[0]) - 1) + str(int(self.position[1]) + 1) or \
                position == chr(ord(self.position[0])) + str(int(self.position[1]) + 1)
        if self.color == 'white':
            return position == chr(ord(self.position[0]) + 1) + str(int(self.position[1]) + 1) or \
                position == chr(ord(self.position[0]) - 1) + str(int(self.position[1]) + 1) or \
                position == chr(ord(self.position[0])) + str(int(self.position[1]) + 1) or \
                position == chr(ord(self.position[0])) + str(int(self.position[1]) + 2)
        if self.color == 'black' and self.moved:
            return position == chr(ord(self.position[0]) + 1) + str(int(self.position[1]) - 1) or \
                position == chr(ord(self.position[0]) - 1) + str(int(self.position[1]) - 1) or \
                position == chr(ord(self.position[0])) + str(int(self.position[1]) - 1)
        if self.color == 'black':
            return position == chr(ord(self.position[0]) + 1) + str(int(self.position[1]) - 1) \
                or position == chr(ord(self.position[0]) - 1) + str(int(self.position[1]) - 1) \
                or position == chr(ord(self.position[0])) + str(int(self.position[1]) - 1) \
                or position == chr(ord(self.position[0])) + str(int(self.position[1]) - 2)

    def is_valid_move(self, position, board):
        if self.color == 'white':
            positions = [chr(ord(self.position[0]) + 1) + str(int(self.position[1]) + 1),
                         chr(ord(self.position[0]) - 1) + str(int(self.position[1]) + 1)]
            for temporary_position in positions:
                if position == temporary_position:
                    if board[temporary_position] is None:
                        return False
                    if board[temporary_position].color == self.color:
                        return False
                    return True
            return position == chr(ord(self.position[0])) + str(int(self.position[1]) + 1) and\
                not board[chr(ord(self.position[0])) + str(int(self.position[1]) + 1)] \
                or not self.moved and not board[chr(ord(self.position[0])) + str(int(self.position[1]) + 2)]
        else:
            positions = [chr(ord(self.position[0]) + 1) + str(int(self.position[1]) - 1),
                         chr(ord(self.position[0]) - 1) + str(int(self.position[1]) - 1)]
            for temporary_position in positions:
                if position == temporary_position:
                    if board[temporary_position] is None:
                        return False
                    if board[temporary_position].color == self.color:
                        return False
                    return True
            return position == chr(ord(self.position[0])) + str(int(self.position[1]) - 1) and\
                not board[chr(ord(self.position[0])) + str(int(self.position[1]) - 1)] \
                or not self.moved and not board[chr(ord(self.position[0])) + str(int(self.position[1]) - 2)]

    def move(self, position, board):
        if self.is_valid_position(position) and self.is_valid_move(position, board):
            self.previous_position = self.position
            self.position = position
            self.moved = True
            return True
        else:
            print('Invalid move!')


class Knight:
    def __init__(self, position, color):
        self.position = position
        self.previous_position = None
        self.color = color
        self.moved = False
        self.sign = 'N' + self.color[0] + ' '

    def is_valid_position(self, position):
        if position[0].upper() < 'A' or \
            position[0].upper() > 'H' or \
                int(position[1]) < 1 or int(position[1]) > 8:
                    return False
        return position == chr(ord(self.position[0]) + 1) + str(int(self.position[1]) + 2) \
            or position == chr(ord(self.position[0]) + 1) + str(int(self.position[1]) - 2) \
            or position == chr(ord(self.position[0]) - 1) + str(int(self.position[1]) + 2) \
            or position == chr(ord(self.position[0]) - 1) + str(int(self.position[1]) - 2) \
            or position == chr(ord(self.position[0]) + 2) + str(int(self.position[1]) + 1) \
            or position == chr(ord(self.position[0]) + 2) + str(int(self.position[1]) - 1) \
            or position == chr(ord(self.position[0]) - 2) + str(int(self.position[1]) + 1) \
            or position == chr(ord(self.position[0]) - 2) + str(int(self.position[1]) - 1)

    def is_valid_move(self, position, board):
        if board[position] is None:
            return True
        else:
            if board[position].color == self.color:
                return False
            return True

    def move(self, position, board):
        if self.is_valid_position(position) and self.is_valid_move(position, board):
            self.previous_position = self.position
            self.position = position
            self.moved = True
            return True
        else:
            print('Invalid move!')


class Bishop:

    def __init__(self, position, color):
        self.position = position
        self.previous_position = None
        self.color = color
        self.moved = False
        self.sign = 'B' + self.color[0] + ' '

    def is_valid_position(self, position):
        if position[0].upper() < 'A' or \
            position[0].upper() > 'H' or \
                int(position[1]) < 1 or int(position[1]) > 8:
                    return False
        return abs(ord(position[0].upper()) - ord(self.position[0])) == \
            abs(int(position[1]) - int(self.position[1]))

    def is_valid_move(self, position, board):
        col = self.position[0]
        row = self.position[1]
        if board[position] and board[position].color == self.color:
            return False

        if self.position[0] > position[0] and self.position[1] > position[1]:
            for step in range(1, abs(int(self.position[1]) - int(position[1]))):
                col = chr(ord(col) - 1)
                row = str(int(row) - 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True
        if self.position[0] > position[0] and self.position[1] < position[1]:
            for step in range(1, abs(int(self.position[1]) - int(position[1]))):
                col = chr(ord(col) - 1)
                row = str(int(row) + 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True
        if self.position[0] < position[0] and self.position[1] > position[1]:
            for step in range(1, abs(int(self.position[1]) - int(position[1]))):
                col = chr(ord(col) + 1)
                row = str(int(row) - 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True
        if self.position[0] < position[0] and self.position[1] < position[1]:
            for step in range(1, abs(int(self.position[1]) - int(position[1]))):
                col = chr(ord(col) + 1)
                row = str(int(row) + 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True

    def move(self, position, board):
        if self.is_valid_position(position) and self.is_valid_move(position, board):
            self.previous_position = self.position
            self.position = position
            return True
        else:
            print('Invalid move!')


class Rook:

    def __init__(self, position, color):
        self.position = position
        self.previous_position = None
        self.color = color
        self.moved = False
        self.sign = 'R' + self.color[0] + ' '

    def is_valid_position(self, position):
        if position[0].upper() < 'A' or \
            position[0].upper() > 'H' or \
                int(position[1]) < 1 or int(position[1]) > 8:
            return False
        return position[0] == self.position[0] or \
            position[1] == self.position[1]

    def is_valid_move(self, position, board):
        col = self.position[0]
        row = self.position[1]
        if board[position] and board[position].color == self.color:
            return False
        if self.position[0] == position[0] and self.position[1] < position[1]:
            for step in range(1, abs(int(self.position[1]) - int(position[1]))):
                row = str(int(row) + 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True
        if self.position[0] == position[0] and self.position[1] > position[1]:
            for step in range(1, abs(int(self.position[1]) - int(position[1]))):
                row = str(int(row) - 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True
        if self.position[0] < position[0] and self.position[1] == position[1]:
            for step in range(1, abs(ord(self.position[0]) - ord(position[0]))):
                col = chr(ord(col) + 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True
        if self.position[0] > position[0] and self.position[1] == position[1]:
            for step in range(1, abs(ord(self.position[0]) - ord(position[0]))):
                col = chr(ord(col) - 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True

    def move(self, position, board):
        if self.is_valid_position(position) and self.is_valid_move(position, board):
            self.previous_position = self.position
            self.position = position
            return True
        else:
            print('Invalid move!')


class Queen:

    def __init__(self, position, color):
        self.position = position
        self.previous_position = None
        self.color = color
        self.moved = False
        self.sign = 'Q' + self.color[0] + ' '

    def is_valid_position(self, position):
        if position[0].upper() < 'A' or \
            position[0].upper() > 'H' or \
                int(position[1]) < 1 or int(position[1]) > 8:
            return False
        return abs(ord(position[0].upper()) - ord(self.position[0])) == \
            abs(int(position[1]) - int(self.position[1])) or \
            position[0] == self.position[0] or \
            position[1] == self.position[1]

    def is_valid_move(self, position, board):
        col = self.position[0]
        row = self.position[1]
        if board[position] and board[position].color == self.color:
            return False
        if self.position[0] > position[0] and self.position[1] > position[1]:
            for step in range(1, abs(int(self.position[1]) - int(position[1]))):
                col = chr(ord(col) - 1)
                row = str(int(row) - 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True
        if self.position[0] > position[0] and self.position[1] < position[1]:
            for step in range(1, abs(int(self.position[1]) - int(position[1]))):
                col = chr(ord(col) - 1)
                row = str(int(row) + 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True
        if self.position[0] < position[0] and self.position[1] > position[1]:
            for step in range(1, abs(int(self.position[1]) - int(position[1]))):
                col = chr(ord(col) + 1)
                row = str(int(row) - 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True
        if self.position[0] < position[0] and self.position[1] < position[1]:
            for step in range(1, abs(int(self.position[1]) - int(position[1]))):
                col = chr(ord(col) + 1)
                row = str(int(row) + 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True
        col = self.position[0]
        row = self.position[1]
        if self.position[0] == position[0] and self.position[1] < position[1]:
            for step in range(1, abs(int(self.position[1]) - int(position[1]))):
                row = str(int(row) + 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True
        if self.position[0] == position[0] and self.position[1] > position[1]:
            for step in range(1, abs(int(self.position[1]) - int(position[1]))):
                row = str(int(row) - 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True
        if self.position[0] < position[0] and self.position[1] == position[1]:
            for step in range(1, abs(ord(self.position[0]) - ord(position[0]))):
                col = chr(ord(col) + 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True
        if self.position[0] > position[0] and self.position[1] == position[1]:
            for step in range(1, abs(ord(self.position[0]) - ord(position[0]))):
                col = chr(ord(col) - 1)
                temporary_position = col + row
                if board[temporary_position]:
                    return False
            return True

    def move(self, position, board):
        if self.is_valid_position(position):
            self.previous_position = self.position
            self.position = position
            return True
        else:
            print('Invalid move!')


class King:

    def __init__(self, position, color):
        self.position = position
        self.previous_position = None
        self.color = color
        self.moved = False
        self.sign = 'K' + self.color[0] + ' '

    def is_valid_position(self, position):
        if position[0].upper() < 'A' or \
                position[0].upper() > 'H' or \
                int(position[1]) < 1 or int(position[1]) > 8:
                return False
        if moved:
            return position == chr(ord(self.position[0]) + 1) + str(int(self.position[1]) + 1) \
                or position == chr(ord(self.position[0]) + 1) + str(int(self.position[1])) \
                or position == chr(ord(self.position[0]) + 1) + str(int(self.position[1]) - 1) \
                or position == chr(ord(self.position[0]) - 1) + str(int(self.position[1]) + 1) \
                or position == chr(ord(self.position[0]) - 1) + str(int(self.position[1])) \
                or position == chr(ord(self.position[0]) - 1) + str(int(self.position[1]) - 1) \
                or position == chr(ord(self.position[0])) + str(int(self.position[1]) + 1) \
                or position == chr(ord(self.position[0])) + str(int(self.position[1]) - 1)
        else:
            return position == chr(ord(self.position[0]) + 1) + str(int(self.position[1]) + 1) \
                or position == chr(ord(self.position[0]) + 1) + str(int(self.position[1])) \
                or position == chr(ord(self.position[0]) + 1) + str(int(self.position[1]) - 1) \
                or position == chr(ord(self.position[0]) - 1) + str(int(self.position[1]) + 1) \
                or position == chr(ord(self.position[0]) - 1) + str(int(self.position[1])) \
                or position == chr(ord(self.position[0]) - 1) + str(int(self.position[1]) - 1) \
                or position == chr(ord(self.position[0])) + str(int(self.position[1]) + 1) \
                or position == chr(ord(self.position[0])) + str(int(self.position[1]) - 1) \
                or position == chr(ord(self.position[0]) - 2) + str(int(self.position[1])) \
                or position == chr(ord(self.position[0]) + 2) + str(int(self.position[1]) - 1)

    def is_valid_move(self, position, board):
        positions = [chr(ord(self.position[0]) + 1) + str(int(self.position[1]) + 1),
                     chr(ord(self.position[0]) + 1) + str(int(self.position[1])),
                     chr(ord(self.position[0]) + 1) + str(int(self.position[1]) - 1),
                     chr(ord(self.position[0]) - 1) + str(int(self.position[1]) + 1),
                     chr(ord(self.position[0]) - 1) + str(int(self.position[1])),
                     chr(ord(self.position[0]) - 1) + str(int(self.position[1]) - 1),
                     chr(ord(self.position[0])) + str(int(self.position[1]) + 1),
                     chr(ord(self.position[0])) + str(int(self.position[1]) - 1)
                     ]

    def move(self, position, board):
        if self.is_valid_position(position):
            self.previous_position = self.positiond
            self.position = position
            return True
        else:
            print('Invalid move!')
