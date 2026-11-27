from tkinter import *
from tkinter import ttk
from convert import convert
import os, sys

base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

root = Tk(className="DragonUnits")
root.title("Dragon Units")

root.tk.call("source", os.path.join(base, "themes", "awthemes-10.4.0", "awdark.tcl"))
root.tk.call("source", os.path.join(base, "themes", "awthemes-10.4.0", "awlight.tcl"))

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))


def gconvert():
    x = amount.get()
    print(x)
    src = unit1.get()
    print(src)
    dst = unit2.get()
    print(dst)
    try:
        value = float(amount.get())
    except ValueError:
        result.config(text="That's not a number. Even beard-seconds need numbers. =P")
        return
    print(repr(value), type(value))
    result1 = convert(value, unit1.get(), unit2.get())
    result.config(text=result1)


UNITS = {
    "1": ("smoot"),
    "2": ("beard second"),
    "3": ("meter"),
    "4": ("inch"),
    "5": ("centameter"),
    "6": ("milimeter"),
    "7": ("kilometer"),
    "8": ("square meter"),
    "9": ("square kilometer"),
    "10": ("exameter"),
    "11": ("petameter"),
    "12": ("terameter"),
    "13": ("gigameter")
}

posunits = {name for name in UNITS.values()}


def on_convert():
    try:
        value = float(amount.get())
    except ValueError:
        result.config(text="That's not a number. Even beard-seconds need numbers.")
        return
    result


amount = ttk.Entry(mainframe, width=20)
amount.grid(column=0, row=0, sticky=(W, E))

unit1 = ttk.Combobox(
    mainframe, state="readonly", width=30, values=[name for name in UNITS.values()]
)
unit1.grid(column=1, row=0, sticky=(W, E))

unit2 = ttk.Combobox(
    mainframe, state="readonly", width=30, values=[name for name in UNITS.values()]
)
unit2.grid(column=2, row=0, sticky=(W, E))

convertbutton = ttk.Button(mainframe, text="convert", command=gconvert)
convertbutton.grid(column=3, row=0, sticky=(W, E))

result = ttk.Label(mainframe, text="")
result.grid(column=0, row=1, sticky=(W, E))

s = ttk.Style()


def apply_theme():
    s.theme_use(theme.get())


themesel = ttk.Frame(mainframe, padding=(3, 3, 12, 12))
themesel.grid(column=0, row=3, sticky=(N, W, E, S))

theme = StringVar(value="awdark")
dark = ttk.Radiobutton(
    themesel, text="Dark", variable=theme, value="awdark", command=apply_theme
)
dark.grid(column=1, row=0)
light = ttk.Radiobutton(
    themesel, text="Light", variable=theme, value="awlight", command=apply_theme
)
light.grid(column=1, row=1)

apply_theme()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
