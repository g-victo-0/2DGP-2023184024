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
