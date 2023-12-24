import time
import asyncio
import curses
from random import choice, randint

TIC_TIMEOUT = 0.1


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(randint(0, 20)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(randint(0, 3)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(randint(0, 5)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(randint(0, 3)):
            await asyncio.sleep(0)


def draw(canvas):
    curses.curs_set(False)
    canvas.border()

    symbols = ['+', '*', '.', ':']
    number_of_stars = randint(50, 200)

    row, column = curses.window.getmaxyx(canvas)

    coroutines = [blink(canvas, randint(0, row - 1), randint(0, column - 1), choice(symbols)) for _ in
                  range(number_of_stars)]

    while True:
        for coroutine in coroutines.copy():
            coroutine.send(None)
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
