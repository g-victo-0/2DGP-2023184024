from pico2d import *

import os


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
CENTER_X = CANVAS_WIDTH // 2
CENTER_Y = CANVAS_HEIGHT // 2
SCALE = 2.2
FRAME_DELAY = 0.18
REPEAT_COUNT = 5
PAUSE_TIME = 1.0


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
image_path = os.path.join(os.path.dirname(__file__), 'character_spritesheet_advanced.png')
sprite_sheet = load_image(image_path)


walk_frames = [
    (409, 781, 122, 198),
    (611, 781, 135, 198),
    (810, 781, 134, 198),
    (1010, 781, 132, 197)
]

run_frames = [
    (81, 527, 171, 194),
    (328, 527, 188, 195),
    (558, 527, 185, 195),
    (789, 527, 186, 195),
    (1026, 527, 188, 195),
    (1270, 527, 185, 195)
]

jump_frames = [
    (200, 256, 140, 151),
    (452, 260, 158, 194),
    (707, 290, 159, 199),
    (938, 269, 164, 197),
    (1213, 254, 125, 147)
]

attack_frames = [
    (58, 42, 141, 183),
    (253, 42, 164, 183),
    (449, 42, 197, 182),
    (662, 42, 214, 182),
    (902, 42, 195, 182),
    (1125, 42, 149, 183),
    (1333, 42, 146, 183)
]

animations = [walk_frames, run_frames, jump_frames, attack_frames]
animation_names = ['WALK', 'RUN', 'JUMP', 'ATTACK']


def draw_frame(frame):
    x, y, width, height = frame
    draw_width = int(width * SCALE)
    draw_height = int(height * SCALE)
    clear_canvas()
    sprite_sheet.clip_draw(x, y, width, height,
                           CENTER_X, CENTER_Y, draw_width, draw_height)
    update_canvas()
    delay(FRAME_DELAY)


def play_animation(name, frames):
    print(name)
    for repeat in range(REPEAT_COUNT):
        for frame in frames:
            draw_frame(frame)
    delay(PAUSE_TIME)


while True:
    for index in range(len(animations)):
        play_animation(animation_names[index], animations[index])
