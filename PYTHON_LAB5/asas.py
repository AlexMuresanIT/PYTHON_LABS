from graphics import *
from random import randint
WINDOW_WIDTH, WINDOW_HEIGHT = 560, 560
COLUMNS, ROWS = 16, 16
TILE_WIDTH, TILE_HEIGHT = WINDOW_WIDTH // COLUMNS, WINDOW_HEIGHT // ROWS
def draw_board():
    board = []
    for y in range(0, WINDOW_HEIGHT, TILE_HEIGHT):
        for x in range(0, WINDOW_WIDTH, TILE_WIDTH):
            board_box= Rectangle(Point(x, y), Point(x + TILE_WIDTH, y + TILE_HEIGHT))
            r =randint (0,255)
            g=randint (0,255)
            b =randint (0,255)
            culoare= color_rgb(r,g,b)
            board_box.setFill(culoare)
            board_box.setOutline("grey")
            board_box.draw(win)
            board.append(board_box)


    return board
win =GraphWin ("PALETA_CULORI", WINDOW_WIDTH, WINDOW_HEIGHT)
tabla= draw_board()