from tkinter import *
from tkinter import ttk
from convert import convert
import os, sys

base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

root = Tk(className="DragonUNITS")
root.title("Dragon UNITS")

root.tk.call("source", os.path.join(base, "themes", "awthemes-10.4.0", "awdark.tcl"))
root.tk.call("source", os.path.join(base, "themes", "awthemes-10.4.0", "awlight.tcl"))

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))


def gconvert():
    print("-------")
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
    "3": ("foot"),
    "4": ("quettameter"),
    "5": ("ronnameter"),
    "6": ("yottameter"),
    "7": ("zettameter"),
    "8": ("exameter"),
    "9": ("petameter"),
    "10": ("terameter"),
    "11": ("gigameter"),
    "12": ("megameter"),
    "13": ("kilometer"),
    "14": ("hectometer"),
    "15": ("dekameter"),
    "16": ("meter"),
    "17": ("decimeter"),
    "18": ("centameter"),
    "19": ("milimeter"),
    "20": ("micrometer"),
    "21": ("nanometer"),
    "22": ("picometer"),
    "23": ("femtometer"),
    "24": ("attometer"),
    "25": ("zeptometer"),
    "26": ("yoctometer"),
    "27": ("rontometer"),
    "28": ("quectometer"),
    "29": ("mile"),
    "30": ("yard"),
    "31": ("break"),
    "32": ("lightyear"),
    "33": ("furlong"),
    "34": ("chain"),
    "35": ("x-unit"),
    "36": ("handbreadth"),
    "37": ("parsec"),
    "38": ("square meter"),
    "39": ("square kilometer"),
    "40": ("township"),
    "41": ("circular inch"),
    "42": ("sabin"), 
    "43": ("varas castellanas cuad"),
    "44": ("acre"),
    "45": ("hectare"),
    "46": ("barn"),
    "47": ("rood"),
    "48": ("arpent"),
    "49": ("plaza"),
    "50": ("cuerda"),
    "51": ("section")
}

posUNITS = {name for name in UNITS.values()}


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
