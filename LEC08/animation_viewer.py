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
    (358, 784, 145, 194),
    (591, 784, 138, 194),
    (818, 784, 143, 194),
    (1051, 784, 138, 194)
]

run_frames = [
    (72, 527, 196, 196),
    (320, 528, 186, 195),
    (549, 526, 195, 197),
    (793, 527, 180, 195),
    (1015, 525, 198, 198),
    (1267, 527, 180, 195)
]

jump_frames = [
    (202, 255, 138, 151),
    (454, 261, 155, 192),
    (708, 290, 157, 197),
    (939, 268, 161, 197),
    (1214, 255, 122, 146)
]

attack_frames = [
    (57, 44, 142, 180),
    (255, 44, 162, 180),
    (452, 44, 194, 180),
    (664, 44, 212, 180),
    (905, 44, 192, 180),
    (1127, 44, 147, 180),
    (1335, 44, 144, 180)
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
