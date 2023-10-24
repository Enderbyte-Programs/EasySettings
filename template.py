import cursesplus
import curses

VERSION = "1.0"
NAME = "template"
DESCRIPTION = "This is a template for people to write modules"

"""
How to make a module:
First, copy this template to a new file. This will be your module file. Unfortunately, everything must be in one file for now.

There are three mandatory variables and one mandatory function.

VERSION (string) : Your module's version (must be semver)
NAME (string) : The name of your module
DESCRIPTION (string) : A long description of what your module does

Now for the functions, if you don't use them, just leave them as return 0. If the function returns something that isn't 0, we will assume that something has gone wrong.

The only required function is run(). It must return an int. The stdscr argument is a curses object which you must use for any UI drawing. For this reason, curses and cursesplus are provided at the top for imports.
"""
def run(stdscr) -> int:
    return 0