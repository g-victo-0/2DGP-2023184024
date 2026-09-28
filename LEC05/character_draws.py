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
        radian = math.radians(degree)
        x = 400 + 200 * math.cos(radian)
        y = 300 + 200 * math.sin(radian)
        draw_character(x,y)
    pass

def move_top():
    print('TOP')
    for x in range(50,750,5):
        draw_character(x,550)
    pass
def move_right():
    print('RIGHT')
    for y in range(550,50,-5):
        draw_character(750,y)
    pass
def move_bottom():
    print('BOTTOM')
    for x in range(750,50,-5):
        draw_character(x,50)
    pass
