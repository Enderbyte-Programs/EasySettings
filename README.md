# EasySettings
A highly extensible TUI settings program.

## The Philosophy of this software

On command-line linux and on servers, it can be very difficult to manage your settings. You have to screw about in a hundred little config files. This program seeks to use modules- small programs contributed by other people to control settings. This uses the cursesplus UI so it is fairly user-friendly, at least compared to the current system. Currently, there is only one example module based of the template. 

### Cursesplus

UIs in the program are made by ncurses. I made a library called cursesplus. This has option menus and file dialogues that make things a little but easier to program.
