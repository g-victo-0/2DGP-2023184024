from pico2d import *

import math

open_canvas(800, 600)
character = load_image('character.png')


def draw_character(x,y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.05)

def draw_circle():
    print("CIRCLE")

    for degree in range(0,360,5):
        pass
    pass
