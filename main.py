from gpanel import *
from time import sleep

makeGPanel(0, 100, 0, 100)

SIZE = 10
PIPR = 0.8

LEFT = 0.2
CENTRE = 0.5
RIGHT = 0.8

TOP = RIGHT
BOTTOM = LEFT

def draw_face(x, y):
    setColor("black")
    fillRectangle(x, y, x + SIZE, y + SIZE)

def draw_pip(x, y, relx, rely):
    setColor("white")
    px = x + relx * SIZE
    py = y + rely * SIZE
    pos(px, py)
    fillCircle(PIPR)
    
def draw_pips(x, y, number):
    def pip(relx, rely):
        draw_pip(x, y, relx, rely)

    if number == 1:
        pip(CENTRE, CENTRE)
    elif number == 2:
        pip(LEFT, TOP)
        pip(RIGHT, BOTTOM)
    elif number == 3:
        pip(LEFT, TOP)
        pip(CENTRE, CENTRE)
        pip(RIGHT, BOTTOM)
    elif number == 4:
        pip(LEFT, TOP)
        pip(LEFT, BOTTOM)
        pip(RIGHT, TOP)
        pip(RIGHT, BOTTOM)
    elif number == 5:
        pip(LEFT, TOP)
        pip(LEFT, BOTTOM)
        pip(RIGHT, TOP)
        pip(RIGHT, BOTTOM)
        pip(CENTRE, CENTRE)
    elif number == 6:
        pip(LEFT, TOP)
        pip(LEFT, BOTTOM)
        pip(RIGHT, TOP)
        pip(RIGHT, BOTTOM)
        pip(LEFT, CENTRE)
        pip(RIGHT, CENTRE)
    
draw_face(30, 30)
draw_pips(30, 30, 6)
