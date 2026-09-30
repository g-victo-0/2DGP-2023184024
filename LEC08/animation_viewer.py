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
    (395, 756, 139, 247),
    (601, 754, 153, 243),
    (805, 754, 154, 244),
    (1004, 754, 151, 239)
]

run_frames = [
    (86, 506, 178, 235),
    (319, 515, 213, 226),
    (544, 489, 231, 250),
    (775, 489, 224, 250),
    (1017, 509, 201, 228),
    (1242, 507, 209, 231)
]

jump_frames = [
    (110, 229, 260, 176),
    (452, 247, 170, 224),
    (713, 229, 170, 260),
    (937, 229, 175, 253),
    (1168, 229, 232, 177)
]

attack_frames = [
    (45, 19, 164, 210),
    (236, 18, 214, 211),
    (450, 19, 220, 210),
    (670, 19, 220, 210),
    (890, 18, 210, 211),
    (1109, 18, 166, 211),
    (1312, 18, 164, 211)
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
