import shutil
import template as activemod#Shut up, Visual Studio
import cursesplus
import curses
import sys
import os
import glob
"""
loader = input()
exec(f"import {loader} as activemod")
activemod.init()
activemod.run()
activemod.close()"""

rundirectory = os.path.dirname(os.path.realpath(__file__))
os.chdir(rundirectory)#Make sure we have access to libraries

class ModFile:
    name = "Unknown"
    version = "Unknown"
    description = "Unknown"
    def __init__(self,file):
        self.file = file
    def read_info(self):
        with open(self.file) as f:
            data = f.readlines()
        aline = ""
        for line in data:
            if line.startswith("NAME"):
                aline = line
                break
        self.name = aline.split("=")[1].strip().replace("\"","")

        vline = ""
        for line in data:
            if line.startswith("VERSION"):
                vline = line
                break
        self.version = vline.split("=")[1].strip().replace("\"","")

        vline = ""
        for line in data:
            if line.startswith("DESCRIPTION"):
                vline = line
                break
        self.description = vline.split("=")[1].strip().replace("\"","")
        return self
    def is_valid(self) -> bool:
        return detect_valid_mod(self.file)

def detect_valid_mod(file:str) -> bool:
    if not os.path.isfile(file) or file.endswith("main.py") or file.endswith("template.py"):
        return False#It can't be valid if it doesn't exists
    with open(file) as f:
        data = f.readlines()
    good = 0
    for line in data:
        if "VERSION" in line:
             good += 1
        elif "DESCRIPTION" in line:
            good += 1
        elif "NAME" in line:
            good += 1
        elif "def run(stdscr)" in line:
            good += 1
    return good == 4
 
def extract_mod_name(file:str) -> str:
        with open(file) as f:
            data = f.readlines()
        aline = ""
        for line in data:
            if line.startswith("NAME"):
                aline = line
                break
        return aline.split("=")[1].strip().replace("\"","")
def run_settings(stdscr):
    available_files = [g for g in glob.glob(rundirectory+"/*.py") if not "template.py" in g and not "main.py" in g and detect_valid_mod(g)]
    while True:
        chosen_mod = cursesplus.coloured_option_menu(stdscr,["BACK"]+[extract_mod_name(g)+" : "+ModFile(g).read_info().description for g in available_files],colouring=[["back",cursesplus.RED]],title="Please choose a settings module")
        if chosen_mod == 0:
            break
        else:
            odir = os.getcwd()
            exec(f"import {os.path.split(available_files[chosen_mod-1])[1].split('.py')[0]} as activemod;e = activemod.run(stdscr)")
            #cursesplus.messagebox.showinfo(stdscr,[activemod.NAME,activemod.DESCRIPTION,activemod.VERSION])
            #e = activemod.run(stdscr)
            os.chdir(odir)

def manage_mods(stdscr):
    
    while True:
        available_files = [g for g in glob.glob(rundirectory+"/*.py") if not "template.py" in g and not "main.py" in g and detect_valid_mod(g)]
        chosen_mod = cursesplus.coloured_option_menu(stdscr,["BACK","Add module"]+available_files,colouring=[["back",cursesplus.RED],["add",cursesplus.GREEN]],title="Please choose a module to manage it")
        if chosen_mod == 0:
            break
        elif chosen_mod == 1:
            afile = cursesplus.filedialog.openfiledialog(stdscr,"Please choose a settings module",[["*.py","Python files"],["*","All files"]],os.path.expanduser("~"))
            if not ModFile(afile).is_valid():
                cursesplus.messagebox.showerror(stdscr,["The selected file is not a valid settings module.","Or the selected file contains a forbidden name"])
            else:
                shutil.copyfile(afile,os.getcwd()+"/"+os.path.split(afile)[1])
        else:
            activem = available_files[chosen_mod-2]
            wtd = cursesplus.displayops(stdscr,["BACK","View module info","Delete module"])
            if wtd == 0:
                continue
            elif wtd == 1:
                m = ModFile(activem)
                if not m.is_valid():
                    cursesplus.messagebox.showerror(stdscr,["The selected module is not a valid settings moduke"])
                    os.remove(m.file)
                else:
                    m.read_info()
                    stdscr.erase()
                    cursesplus.filline(stdscr,0,cursesplus.set_colour(cursesplus.WHITE,cursesplus.BLACK))
                    stdscr.addstr(0,0,f"VIEWING INFO FOR {m.file}",cursesplus.set_colour(cursesplus.WHITE,cursesplus.BLACK))
                    stdscr.addstr(2,0,"Module name")
                    stdscr.addstr(3,0,"Module version")
                    stdscr.addstr(4,0,"Module description")
                    stdscr.addstr(5,0,"Module size")
                    stdscr.addstr(6,0,"File path")
                    stdscr.addstr(2,20,m.name)
                    stdscr.addstr(3,20,m.version)
                    stdscr.addstr(4,20,m.description)
                    stdscr.addstr(5,20,cursesplus.filedialog.parse_size(os.path.getsize(m.file)))
                    stdscr.addstr(6,20,m.file)
                    stdscr.addstr(8,0,"PRESS ANY KEY TO PROCEED")
                    stdscr.getch()
            elif wtd == 2:
                os.remove(m.file)
def main(stdscr):
    while True:
        copt = cursesplus.coloured_option_menu(stdscr,["Start","Manage modules","Quit"],"Please choose an option",[["quit",cursesplus.RED],["start",cursesplus.GREEN]])
        if copt == 2:
            return
        elif copt == 0:
            run_settings(stdscr)
        elif copt == 1:
            manage_mods(stdscr)

curses.wrapper(main)