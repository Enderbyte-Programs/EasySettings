import cursesplus
import curses

VERSION = "1.0"
NAME = "test"
DESCRIPTION = "This is another testing module"

def run(stdscr) -> int:
    cursesplus.messagebox.showinfo(stdscr,["Hi!","I am test"])
    return 0
