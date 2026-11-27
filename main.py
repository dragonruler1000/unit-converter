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
    "0": ("smoot"),
    "1": ("beard second"),
    "2": ("inch"),
    "3": ("square meter"),
    "4": ("square kilometer"),
    "5": ("exameter"),
    "6": ("petameter"),
    "7": ("terameter"),
    "8": ("gigameter"),
    "9": ("megameter"),
    "10": ("kilometer"),
    "11": ("hectometer"),
    "12": ("decameter"),
    "13": ("meter"),
    "14": ("decimeter"),
    "15": ("centameter"),
    "16": ("milimeter"),
    "17": ("micrometer"),
    "18": ("nanometer"),
    "19": ("picometer"),
    "20": ("femtometer"),
    "21": ("attometer"),
    "22": ("zeptometer"),
    "23": ("quacometer"),
    "24": ("mile"),
    "25": ("yard"),
    "26": ("break"),
}

posunits = {name for name in UNITS.values()}


def on_convert():
    try:
        value = float(amount.get())
    except ValueError:
        result.config(text="That's not a number. Even beard-seconds need numbers.")
        return
    result


unitframe = ttk.Frame(mainframe, padding=(3, 3, 12, 12))
unitframe.grid(column=0, row=0, sticky=(N, E, S, W))

amount = ttk.Entry(unitframe, width=20)
amount.grid(column=0, row=1, sticky=(W, E))

unit1label = ttk.Label(unitframe, text="Unit to convert from")
unit1label.grid(column=1, row=0, sticky=(W, E))

unit1 = ttk.Combobox(
    unitframe, state="readonly", width=30, values=[name for name in UNITS.values()]
)
unit1.grid(column=1, row=1, sticky=(W, E))

unit2label = ttk.Label(unitframe, text="Unit to convert to")
unit2label.grid(column=2, row=0, sticky=(W, E))

unit2 = ttk.Combobox(
    unitframe, state="readonly", width=30, values=[name for name in UNITS.values()]
)
unit2.grid(column=2, row=1, sticky=(W, E))

convertbutton = ttk.Button(unitframe, text="convert", command=gconvert)
convertbutton.grid(column=3, row=1, sticky=(W, E))

result = ttk.Label(unitframe, text="")
result.grid(column=0, row=2, sticky=(W, E))

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

notes = ttk.Frame(mainframe, padding=(3, 3, 12, 12))
notes.grid(column=0, row=4, sticky=(N, W, S, E))

note = ttk.Label(
    notes, text="For anyone wondering this converter is not designed for convinece"
)
note.grid(column=0, row=0)

apply_theme()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
