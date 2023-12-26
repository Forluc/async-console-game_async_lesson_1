import asyncio
import os

from animation.curses_tools import draw_frame, get_frame_size, read_controls


async def animate_starship(canvas, start_row, start_column):
    rocket_dir = os.path.join('animation', 'rocket')

    with open(os.path.join(rocket_dir, 'rocket_frame_1.txt'), 'r') as rocket:
        active_frame = rocket.read()
    with open(os.path.join(rocket_dir, 'rocket_frame_2.txt'), 'r') as rocket:
        next_frame = rocket.read()

    frame_height, frame_width = get_frame_size(active_frame)
    canvas_height, canvas_width = canvas.getmaxyx()
    border_width = 1

    row, column = start_row + 1, start_column - round(frame_width / 2)

    motion_space_width = canvas_width - frame_width - border_width
    motion_space_height = canvas_height - frame_height - border_width

    while True:
        draw_frame(canvas, row, column, active_frame, negative=True)
        row_offset, column_offset, space_pressed = read_controls(canvas)

        row = min(row + row_offset, motion_space_height) if row_offset > 0 else max(row + row_offset, 1)
        column = min(column + column_offset, motion_space_width) if column_offset > 0 else max(column + column_offset, 1)

        draw_frame(canvas, row, column, next_frame)
        active_frame, next_frame = next_frame, active_frame
        await asyncio.sleep(0)
