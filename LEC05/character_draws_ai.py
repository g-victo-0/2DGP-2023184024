from pico2d import *

import math
import os


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_DELAY = 0.01
character = None


def initialize():
    global character
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    image_path = os.path.join(os.path.dirname(__file__), 'character.png')
    character = load_image(image_path)


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)


def move_line(start_x, start_y, end_x, end_y, steps=100):
    for step in range(steps + 1):
        ratio = step / steps
        x = start_x + (end_x - start_x) * ratio
        y = start_y + (end_y - start_y) * ratio
        draw_character(x, y)


def draw_circle():
    print('CIRCLE')
    center_x = 400
    center_y = 300
    radius = 200

    for degree in range(0, 360, 5):
        radian = math.radians(degree)
        x = center_x + radius * math.cos(radian)
        y = center_y + radius * math.sin(radian)
        draw_character(x, y)


def draw_rectangle():
    print('RECTANGLE')
    move_line(50, 550, 750, 550)
    move_line(750, 550, 750, 50)
    move_line(750, 50, 50, 50)
    move_line(50, 50, 50, 550)
