import random
import curses
from curses import wrapper

import src.colors as colors
import src.elements as elements
import src.drawing as drawing


def main(stdscr: curses.initscr):
    curses.start_color()
    curses.use_default_colors()

    # init color pairs
    curses.init_pair(colors.WHITE_ON_BLACK, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(colors.BLACK_ON_WHITE, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(colors.YELLOW_ON_BLACK, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(colors.RED_ON_BLACK, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(colors.BLUE_ON_BLACK, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(colors.GREEN_ON_BLACK, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(colors.CYAN_ON_BLACK, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(colors.MAGENTA_ON_BLACK, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    # Clear screen
    stdscr.clear()

    SMOKE = elements.SMOKES[0]
    
    # sub-window for snow fall
    snow_height = 1
    height = len(elements.XMAS) + len(elements.HOUSE) + len(SMOKE) + 1; width = len(elements.TRAIL[0])
    begin_y = 0; begin_x = 0
    snow = curses.newwin(height, width, begin_y, begin_x)

    # sub-window for Merry Christmas
    height = len(elements.XMAS) + 1; width = len(elements.XMAS[0])
    begin_y = 1; begin_x = 1
    xmas = curses.newwin(height, width, begin_y, begin_x)

    # sub-window for tree
    tree_state = None
    height = len(elements.TREE) + 1; width = len(elements.TREE[0])
    begin_y = len(elements.XMAS) + len(elements.HOUSE) + len(SMOKE) + 2 - len(elements.TREE); begin_x = 5
    tree = curses.newwin(height, width, begin_y, begin_x)

    # sub-window for snowman
    height = len(elements.SNOWMAN) + 1; width = len(elements.SNOWMAN[0])
    begin_y = len(elements.XMAS) + len(elements.HOUSE) + len(SMOKE) + 2 - len(elements.SNOWMAN); begin_x = 45
    snowman = curses.newwin(height, width, begin_y, begin_x)

    # sub-window for cat
    meow = False
    CAT = elements.cat_obj()
    height = len(CAT) + 1; width = len(CAT[0])
    begin_y = len(elements.XMAS) + len(elements.HOUSE) + len(SMOKE) + 2 - len(CAT); begin_x = 25
    cat = curses.newwin(height, width, begin_y, begin_x)

    # sub-window for smoke
    last_smoke = []
    height = len(SMOKE) + 1; width = len(SMOKE[0])
    begin_y = len(elements.XMAS) + 2; begin_x = 80
    smoke = curses.newwin(height, width, begin_y, begin_x)

    # sub-window for house
    height = len(elements.HOUSE) + 1; width = len(elements.HOUSE[0])
    begin_y = len(elements.XMAS) + len(SMOKE) + 2; begin_x = 65
    house = curses.newwin(height, width, begin_y, begin_x)
    
    # sub-window for trail and snow
    height = len(elements.TRAIL) + 1; width = len(elements.TRAIL[0])
    begin_y = len(elements.XMAS) + len(elements.HOUSE) + len(SMOKE) + 2; begin_x = 0
    trail = curses.newwin(height, width, begin_y, begin_x)
    
    start_line = 0
    has_colors = curses.has_colors()
    if not has_colors:
        print('Sorry! Your terminal does not support colors:(')
        start_line = 1
    start_line += 1

    # just loop counter
    count = 0

    while True:
        stdscr.refresh()

        # snow fall
        snow_state = drawing.draw_snow(window=snow, width=len(elements.TRAIL[0]), height=snow_height)
        if snow_height < len(elements.XMAS) + len(elements.HOUSE) + len(SMOKE):
            snow_height += 1
        
        # Merry Christmas
        drawing.draw_xmas(window=xmas)

        # Christmas tree
        if not count % 5:
            tree_state = snow_state
        drawing.draw_tree(window=tree, colored=has_colors, state=tree_state, rand=(not count % 5))
        random.setstate(snow_state)

        # cat
        drawing.draw_cat(window=cat, colored=has_colors, meow=meow)
        if not count % 10:
            meow = not meow

        # snowman
        drawing.draw_snowman(window=snowman, colored=has_colors)

        # smoke
        last_smoke = drawing.draw_smoke(window=smoke, rand=(not count % 10), last_smoke=last_smoke)

        # house
        drawing.draw_house(window=house, colored=has_colors)

        # trail and snow
        drawing.draw_trail(window=trail)

        # delay
        stdscr.timeout(200)

        count += 1

        # to terminate the program
        c = stdscr.getch()
        if c != -1:
            if c == curses.KEY_RESIZE:
                stdscr.clear()
                continue
            else:
                break


wrapper(main)
