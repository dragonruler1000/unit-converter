from tkinter import *
from tkinter import ttk

root = Tk(className="DragonUnits")
root.title("Dragon Units")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))

UNITS = {
    "1": ("Inches"),
    "2": ("Centameters"),
    "3": ("Feet"),
    
}

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
