import random
from graphics import *

#BOARD DE CULORI RANDOM

#rosu: 255 0 0
#alb: 255 255 255
#negru: 0 0 0
#albastru: 0 0 255
#galben: 255 255 0

wh,ww=600,600
r,c=10,10
th,tw=wh//r,ww//c

culori={"alb":[255,255,255],
        "negru":[0,0,0],
        "rosu":[255,0,0],
        "galben":[255,255,0],
        "albastru":[0,0,255]}


def generare_tabla_de_joc():
    board=[]
    for x in range(0,wh,th):
         for y in range(0,ww,tw):
                board_box=Rectangle(Point(x,y),Point(x+tw,y+th))
                codu_culoare=random.choice(list(culori.values()))
                r=codu_culoare[0]
                g=codu_culoare[1]
                b=codu_culoare[2]
                culoare=color_rgb(r,g,b)
                board_box.setFill(culoare)
                board_box.setOutline("grey")
                board_box.draw(win)
                board.append(board_box)
    return board

win = GraphWin("JOC BOX", ww, wh)
tabla=generare_tabla_de_joc()









