import time
import curses
from animation.starship import animate_starship
from animation.stars import get_stars
from animation.fire import fire

TIC_TIMEOUT = 0.1


def draw(canvas):
    canvas.border()
    curses.curs_set(False)
    canvas.nodelay(True)

    height, width = curses.window.getmaxyx(canvas)
    center_row = round(height / 2)
    center_column = round(width / 2)

    blaze = fire(canvas, center_row, center_column)
    stars = get_stars(canvas, height, width)
    starship = animate_starship(canvas, center_row, center_column)

    coroutines = [blaze, *stars, starship]

    while coroutines:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
