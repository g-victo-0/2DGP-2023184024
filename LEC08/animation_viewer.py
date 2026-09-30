from pico2d import *

import os


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
CENTER_X = CANVAS_WIDTH // 2
CENTER_Y = CANVAS_HEIGHT // 2
SCALE = 1.5
FRAME_DELAY = 0.08
REPEAT_COUNT = 5
PAUSE_TIME = 1.0


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
image_path = os.path.join(os.path.dirname(__file__), 'character_spritesheet_advanced.png')
sprite_sheet = load_image(image_path)


walk_frames = [
    (392, 753, 145, 253),
    (598, 751, 159, 249),
    (802, 751, 160, 250),
    (1001, 751, 157, 245)
]

run_frames = [
    (83, 503, 184, 241),
    (316, 512, 219, 268),
    (541, 488, 235, 292),
    (764, 488, 262, 292),
    (1014, 506, 242, 274),
    (1244, 504, 210, 237)
]

jump_frames = [
    (94, 235, 279, 295),
    (432, 244, 193, 286),
    (682, 277, 204, 253),
    (930, 250, 226, 280),
    (1144, 236, 262, 294)
]
