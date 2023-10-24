import cursesplus
import curses

VERSION = "1.0"
NAME = "module"
DESCRIPTION = "This module does stuff and things"

def run(stdscr) -> int:
    cursesplus.messagebox.showinfo(stdscr,["Hello!"])
    return 0