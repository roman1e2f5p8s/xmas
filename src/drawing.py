import random
import curses

from . import colors
from . import elements


def _snow_line(width: int):
    s = ''
    for i in range(width):
        p = random.uniform(0, 1)
        if p <= 0.9:
            s += ' '
        else:
            s += '*'
    
    return s


def draw_snow(window: curses.newwin, width: int, height: int):
    for i in range(height):
        s = _snow_line(width=width)
        window.addstr(i, 0, s, curses.color_pair(colors.WHITE_ON_BLACK))

    window.refresh()

    return random.getstate()


def draw_xmas(window: curses.newwin):
    for i, s in enumerate(elements.XMAS):
        window.addstr(i, 0, s, curses.color_pair(colors.WHITE_ON_BLACK))
    window.refresh()


def _draw_tree_row(window: curses.newwin, colored: bool, i: int, x: int):
    k = 2 * i + 1 # number of stars in a row
    for j in range(k):
        p = random.uniform(0, 1)
        s = '◆' if p <= 0.7 else '●'
        if s == '◆':
            window.addstr(i, x, s, curses.color_pair(colors.GREEN_ON_BLACK if colored else colors.WHITE_ON_BLACK))
        else:
            c = random.choice(colors.LIGHTS_COLORS)
            window.addstr(i, x, s, curses.color_pair(c if colored else colors.WHITE_ON_BLACK))
        x += 1 


def draw_tree(window: curses.newwin, colored: bool, state: object, rand: bool):
    if not rand:
        random.setstate(state)

    for i, x in zip(range(len(elements.TREE) - 1), range(len(elements.TREE[-2])//2, -1, -1)):
        _draw_tree_row(window, colored, i, x)

    i = len(elements.TREE) - 1
    x = len(elements.TREE[-2])//2 - 2
    s = ' ███ ' if True else '│  │'
    window.addstr(i, x, s, curses.color_pair(colors.YELLOW_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    window.refresh()


def draw_snowman(window: curses.newwin, colored: bool):
    i = 0
    x = 4
    s = '┌───┐'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    i += 1
    x = 4
    s = '┴───┴'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    i += 1
    x = 4
    s = '(^'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    x = 6
    s = '▂'
    window.addstr(i, x, s, curses.color_pair(colors.YELLOW_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    x = 7
    s = '^)'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    i += 1
    x = 0
    s = '>--('
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    x = 4
    s = '"🭶'
    window.addstr(i, x, s, curses.color_pair(colors.RED_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    x = 6
    s = '▂'
    window.addstr(i, x, s, curses.color_pair(colors.BLUE_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    x = 7
    s = '🭶🭶'
    window.addstr(i, x, s, curses.color_pair(colors.RED_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    x = 9
    s = ')--<'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    i += 1
    x = 2
    s = '('
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    x = 6
    s = '▂'
    window.addstr(i, x, s, curses.color_pair(colors.BLUE_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    x = 10
    s = ')'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    i += 1
    x = 2
    s = '\‗‗‗‗‗‗‗/'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    window.refresh()


def draw_cat(window: curses.newwin, colored: bool, meow: bool):
    i = 0
    x = 7
    s = 'MEOW' if meow else '    '
    window.addstr(i, x, s, curses.color_pair(colors.RED_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    i += 1
    x = 1
    s = '╱|🮢 ‚ '
    window.addstr(i, x, s, curses.color_pair(colors.YELLOW_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    i += 1
    x = 0
    s = '(ᵒ x ₒ)'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    i += 1
    x = 1
    s = '|🮢  \\\ '
    window.addstr(i, x, s, curses.color_pair(colors.YELLOW_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    i += 1
    x = 1
    s = '⋃ ⋃ ‗◞ )/🭶' if meow else '⋃ ⋃ ‗◞ )‗/'
    window.addstr(i, x, s, curses.color_pair(colors.YELLOW_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    window.refresh()


def draw_smoke(window: curses.newwin, rand: bool, last_smoke: list):
    if not rand:
        smoke = last_smoke
    else:
        smoke = random.choice(elements.SMOKES)

    for i, l in enumerate(smoke):
        window.addstr(i, 0, l, curses.color_pair(colors.WHITE_ON_BLACK))

    window.refresh()

    return smoke


def draw_house(window: curses.newwin, colored: bool):
    i = 0
    x = 15
    s = '┌  ┐'
    window.addstr(i, x, s, curses.color_pair(colors.YELLOW_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    i += 1
    x = 3
    s = '────────────┴──┴───'
    window.addstr(i, x, s, curses.color_pair(colors.YELLOW_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    i += 1
    x = 1
    s = '╱── ── ── ── ── ── ── ╲'
    window.addstr(i, x, s, curses.color_pair(colors.YELLOW_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    i += 1
    x = 0
    s = '╱── ── ── ── ── ── ── ──╲'
    window.addstr(i, x, s, curses.color_pair(colors.YELLOW_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    i += 1
    x = 0
    s = '──┬───────────────────┬──'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    i += 1
    x = 2
    s = '│                   │'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    i += 1
    x = 2
    s = '│'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    x = 6
    s = '╔══╗    ╔═╦═╗'
    window.addstr(i, x, s, curses.color_pair(colors.BLUE_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    x = 22
    s = '│'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    i += 1
    x = 2
    s = '│'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    x = 6
    s = '║  ║    ╠═╬═╣'
    window.addstr(i, x, s, curses.color_pair(colors.BLUE_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    x = 22
    s = '│'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    i += 1
    x = 2
    s = '│'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    x = 6
    s = '║🬃 ║    ╚═╩═╝'
    window.addstr(i, x, s, curses.color_pair(colors.BLUE_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    x = 22
    s = '│'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    i += 1
    x = 2
    s = '│'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    x = 6
    s = '╚══╝'
    window.addstr(i, x, s, curses.color_pair(colors.BLUE_ON_BLACK if colored else colors.WHITE_ON_BLACK))

    x = 22
    s = '│'
    window.addstr(i, x, s, curses.color_pair(colors.WHITE_ON_BLACK))

    window.refresh()


def draw_trail(window: curses.newwin):
    for i, l in enumerate(elements.TRAIL):
        window.addstr(i, 0, l, curses.color_pair(colors.WHITE_ON_BLACK))

    window.refresh()
