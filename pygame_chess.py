import pygame
import sys
from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from game import Game

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (70, 70, 70)
DARK_ORANGE = (255, 140, 0)
LIGHT_ORANGE = (255, 165, 0)
SILVER = (192, 192, 192)
GREEN = (0, 155, 0)
CLEAR_RECT = (550, 250, 450, 700)

pygame.init()
DISPLAY = pygame.display.set_mode((1000, 600))
DISPLAY.fill(GREEN)
pygame.display.set_caption('chess ')

SIZE = 66
startx = 10
starty = 10

blackr = pygame.image.load('blackr.png')
blackb = pygame.image.load('blackb.png')
blackn = pygame.image.load('blackn.png')
blackk = pygame.image.load('blackk.png')
blackq = pygame.image.load('blackq.png')
blackp = pygame.image.load('blackp.png')
whiter = pygame.image.load('whiter.png')
whiteb = pygame.image.load('whiteb.png')
whiten = pygame.image.load('whiten.png')
whitek = pygame.image.load('whitek.png')
whiteq = pygame.image.load('whiteq.png')
whitep = pygame.image.load('whitep.png')

chess_set = {'whiter': whiter, 'whiten': whiten, 'whiteb': whiteb,
             'whiteq': whiteq, 'whitek': whitek, 'whitep': whitep,
             'blackr': blackr, 'blackn': blackn, 'blackb': blackb,
             'blackq': blackq, 'blackk': blackk, 'blackp': blackp
             }


def drawBoard():
    for x in range(0, 8):
        for y in range(0, 8):
            if x % 2 == 0 and y % 2 == 0:
                rectangle = (startx + x*SIZE, starty + y*SIZE, SIZE, SIZE)
                pygame.draw.rect(DISPLAY, WHITE, rectangle)
            elif x % 2 == 0 and y % 2 != 0:
                rectangle = (startx + x*SIZE, starty + y*SIZE, SIZE, SIZE)
                pygame.draw.rect(DISPLAY, GRAY, rectangle)
            elif x % 2 != 0 and y % 2 == 0:
                rectangle = (startx + x*SIZE, starty + y*SIZE, SIZE, SIZE)
                pygame.draw.rect(DISPLAY, GRAY, rectangle)
            elif x % 2 != 0 and y % 2 != 0:
                rectangle = (starty + x*SIZE, starty + y*SIZE, SIZE, SIZE)
                pygame.draw.rect(DISPLAY, WHITE, rectangle)


def in_board(coords):
    return coords[0] >= startx and coords[0] <= startx + 8*SIZE and \
        coords[1] >= starty and coords[1] <= starty + 8*SIZE


def mark(coords, color):
    dimx = int((coords[0]-startx)/SIZE)
    dimy = int((coords[1]-starty)/SIZE)
    rectangle = (startx + dimx*SIZE + 3, starty + dimy*SIZE + 3,
                 SIZE - 7, SIZE - 7)
    pygame.draw.rect(DISPLAY, color, rectangle, 8)


def demark(coords, color):
    if color is None:
        width = 0
        offset = 0
    else:
        width = 8
        offset = 3
    dimx = int((coords[0]-startx)/SIZE)
    dimy = int((coords[1]-starty)/SIZE)
    if dimx % 2 == 0 and dimy % 2 == 0:
        color = WHITE
    if dimx % 2 == 0 and dimy % 2 != 0:
        color = GRAY
    if dimx % 2 != 0 and dimy % 2 == 0:
        color = GRAY
    if dimx % 2 != 0 and dimy % 2 != 0:
        color = WHITE
    rectangle = (startx + dimx*SIZE + offset, starty + dimy*SIZE + offset,
                 SIZE - width + 1, SIZE - width + 1)
    pygame.draw.rect(DISPLAY, color, rectangle, width)


def maketext(text, style, tcolor):
    surf = style.render(text, True, tcolor)
    return surf, surf.get_rect()


def find_address(coords):
    dimx = int((coords[0]-startx)/SIZE)
    dimy = int((coords[1]-starty)/SIZE)
    return chr(dimx + ord('A')) + str(8-dimy)


def show_msg(text, coords, color):
    style = pygame.font.Font('freesansbold.ttf', 35)
    titlesurf, titlerect = maketext(text, style, color)
    titlerect.center = (coords[0] + int(SIZE/2), coords[1] + int(SIZE/2))
    DISPLAY.blit(titlesurf, titlerect)
    pygame.display.update()


def new_game_button():
    pygame.draw.rect(DISPLAY, SILVER, (600, 10, 250, SIZE))
    show_msg('NEW GAME', (700, 10), BLACK)


def resign_button():
    pygame.draw.rect(DISPLAY, SILVER, (600, 90, 250, SIZE))
    show_msg('RESIGN', (700, 90), BLACK)


def quit_button():
    pygame.draw.rect(DISPLAY, SILVER, (600, 170, 250, SIZE))
    show_msg('QUIT', (700, 170), BLACK)


def you_sure():
    show_msg('Are you sure? Press y/n: ', (750, 250), LIGHT_ORANGE)
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False


def promote(game, target):
    show_msg('Promote pawn.Press: ', (750, 300), LIGHT_ORANGE)
    show_msg('r for Rook', (750, 340), LIGHT_ORANGE)
    show_msg('k for Knight ', (750, 380), LIGHT_ORANGE)
    show_msg('b for Bishop ', (750, 420), LIGHT_ORANGE)
    show_msg('q for Queen ', (750, 460), LIGHT_ORANGE)
    col = ord(target[0])-ord('A')
    row = int(target[1])-1
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.board[col][row] = Rook(col, row,
                                                game.board[col][row].color)
                    flag = False
                elif event.key == pygame.K_k:
                    game.board[col][row] = Knight(col, row,
                                                  game.board[col][row].color)
                    flag = False
                elif event.key == pygame.K_b:
                    game.board[col][row] = Bishop(col, row,
                                                  game.board[col][row].color)
                    flag = False
                elif event.key == pygame.K_q:
                    game.board[col][row] = Queen(col, row,
                                                 game.board[col][row].color)
                    flag = False


def now_what():

    show_msg('And now what? Press: ', (750, 300), LIGHT_ORANGE)
    show_msg('n for new game', (750, 370), LIGHT_ORANGE)
    show_msg('q to quit ', (750, 430), LIGHT_ORANGE)
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    run_game()

                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


def show_pieces(game):
    for x in range(0, 8):
        for y in range(0, 8):
            if game.board[x][y]:
                key = game.board[x][y].color + game.board[x][y].sign[0].lower()
                coordinates = (startx + x*SIZE, starty + (7-y)*SIZE)
                DISPLAY.blit(chess_set[key], coordinates)
            else:
                demark((startx + x*SIZE, starty + (7-y)*SIZE), None)


def check_mate_draw(game):
    if game.king_in_check(game.current_player, game.board):
        if game.stalemate():
            show_pieces(game)
            pygame.draw.rect(DISPLAY, GREEN, CLEAR_RECT)
            show_msg(game.next_player + ' wins!', (750, 250), LIGHT_ORANGE)
            now_what()
        else:
            pygame.draw.rect(DISPLAY, GREEN, CLEAR_RECT)
            show_msg(game.current_player + '\'s turn', (700, 250), WHITE)
            show_msg(game.current_player + ' is in check', (750, 310),
                     LIGHT_ORANGE)
    elif game.stalemate() or game.material_stalemate():
            pygame.draw.rect(DISPLAY, GREEN, CLEAR_RECT)
            show_msg('draw', (750, 250), LIGHT_ORANGE)
            now_what()


def handle_buttons(game, coords):
    if coords[0] >= 600 and coords[0] <= 850 \
       and coords[1] >= 10 and coords[1] <= 70:
        pygame.draw.rect(DISPLAY, GREEN, CLEAR_RECT)
        if you_sure():
            run_game()
        else:
            pygame.draw.rect(DISPLAY, GREEN, CLEAR_RECT)
            show_msg(game.current_player + '\'s turn', (700, 250), WHITE)
    elif coords[0] >= 600 and coords[0] <= 850 and \
         coords[1] >= 90 and coords[1] <= 150:
        pygame.draw.rect(DISPLAY, GREEN, CLEAR_RECT)
        if you_sure():
            pygame.draw.rect(DISPLAY, GREEN, CLEAR_RECT)
            show_msg(game.next_player + ' wins!', (750, 250), LIGHT_ORANGE)
            now_what()
        else:
            pygame.draw.rect(DISPLAY, GREEN, CLEAR_RECT)
            show_msg(game.current_player + '\'s turn', (700, 250), WHITE)
    elif coords[0] >= 600 and coords[0] <= 850 and \
         coords[1] >= 170 and coords[1] <= 230:
        pygame.draw.rect(DISPLAY, GREEN, CLEAR_RECT)
        if you_sure():
            pygame.quit()
            sys.exit()
        else:
            pygame.draw.rect(DISPLAY, GREEN, CLEAR_RECT)
            show_msg(game.current_player + '\'s turn', (700, 250), WHITE)


def run_game():
    pygame.draw.rect(DISPLAY, GREEN, CLEAR_RECT)
    drawBoard()
    game = Game()
    show_msg(game.current_player + '\'s turn', (700, 250), WHITE)
    source_selected = False
    while True:
        show_pieces(game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                 pygame.mouse.get_pressed() == (1, 0, 0):
                coords = pygame.mouse.get_pos()
                if in_board(coords):
                    if not source_selected:
                        mark(coords, DARK_ORANGE)
                        source = find_address(coords)
                        source_selected = True
                        coords_source = coords
                    elif source_selected and source == find_address(coords):
                        demark(coords, white)
                        source_selected = False
                    elif source_selected:
                        target = find_address(coords)
                        pygame.draw.rect(DISPLAY, GREEN, CLEAR_RECT)
                        if not game.move(source, target):
                            demark(coords_source, None)
                            show_msg('Invalid move', (700, 310), WHITE)
                        else:
                            demark(coords, None)
                            if game.promotion(source, target):
                                promote(game, target)
                                pygame.draw.rect(DISPLAY, GREEN, CLEAR_RECT)
                        source_selected = False
                        show_msg(game.current_player + '\'s turn',
                                 (700, 250), WHITE)
                        check_mate_draw(game)
                handle_buttons(game, coords)
        new_game_button()
        resign_button()
        quit_button()
        pygame.display.update()

run_game()
