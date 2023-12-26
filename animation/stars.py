import asyncio
from random import randint, choice
import curses


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


def get_stars(canvas, row, column):
    symbols = ['+', '*', '.', ':']
    number_of_stars = randint(50, 200)

    return [blink(canvas, randint(0, row - 1), randint(0, column - 1), choice(symbols)) for _ in
            range(number_of_stars)]
