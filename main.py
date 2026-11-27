from tkinter import *
from tkinter import ttk
from convert import convert
import os, sys

base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

root = Tk(className="DragonLENGTH")
root.title("Dragon LENGTH")

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


LENGTH = {
    "0": ("smoot"),
    "1": ("beard second"),
    "2": ("inch"),
    "3": ("exameter"),
    "4": ("petameter"),
    "5": ("terameter"),
    "6": ("gigameter"),
    "7": ("megameter"),
    "8": ("kilometer"),
    "9": ("hectometer"),
    "10": ("decameter"),
    "11": ("meter"),
    "12": ("decimeter"),
    "13": ("centameter"),
    "14": ("milimeter"),
    "15": ("micrometer"),
    "16": ("nanometer"),
    "17": ("picometer"),
    "18": ("femtometer"),
    "19": ("attometer"),
    "20": ("zeptometer"),
    "21": ("quacometer"),
    "22": ("mile"),
    "23": ("yard"),
    "24": ("break"),
    "25": ("lightyear"),
    "26": ("furlong"),
}

poslength = {name for name in LENGTH.values()}


def on_convert():
    try:
        value = float(amount.get())
    except ValueError:
        lenresult.config(text="That's not a number. Even beard-seconds need numbers.")
        return
    lenresult


unitframe = ttk.Frame(mainframe, padding=(3, 3, 12, 12))
unitframe.grid(column=0, row=0, sticky=(N, E, S, W))

amount = ttk.Entry(unitframe, width=20)
amount.grid(column=0, row=1, sticky=(W, E))

lenunit1label = ttk.Label(unitframe, text="Unit to convert from")
lenunit1label.grid(column=1, row=0, sticky=(W, E))

lenunit1 = ttk.Combobox(
    unitframe, state="readonly", width=30, values=[name for name in LENGTH.values()]
)
lenunit1.grid(column=1, row=1, sticky=(W, E))

unit2label = ttk.Label(unitframe, text="Unit to convert to")
unit2label.grid(column=2, row=0, sticky=(W, E))

lenunit2 = ttk.Combobox(
    unitframe, state="readonly", width=30, values=[name for name in LENGTH.values()]
)
lenunit2.grid(column=2, row=1, sticky=(W, E))

lenconvertbutton = ttk.Button(unitframe, text="convert", command=gconvert)
lenconvertbutton.grid(column=3, row=1, sticky=(W, E))

lenresult = ttk.Label(unitframe, text="")
lenresult.grid(column=0, row=2, sticky=(W, E))

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
