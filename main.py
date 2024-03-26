from fill_form import run

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Property Report Creator")

mainframe = ttk.Frame(window, padding="5 5 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Labels
# ----------------------------------------------------------------

ttk.Label(mainframe, text="Enter Address:").grid(column=1, row=1, sticky=(W, E))
# ttk.Label(mainframe, text="Enter City:").grid(
#     column=1, row=2, sticky=(W, E)
# )
ttk.Label(mainframe, text="Enter Zoning District:").grid(column=1, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Enter Lot Dimensions:").grid(column=1, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Enter Floor Area:").grid(column=1, row=4, sticky=(W, E))
ttk.Label(mainframe, text="Enter Date:").grid(column=1, row=5, sticky=(W, E))
ttk.Label(mainframe, text="Enter Owner Name:").grid(column=1, row=6, sticky=(W, E))

# ----------------------------------------------------------------

# Entry
# ----------------------------------------------------------------

address = StringVar()
width_entry = ttk.Entry(mainframe, width=20, textvariable=address)
width_entry.grid(column=2, row=1, sticky=(W, E))

zoning = StringVar()
width_entry = ttk.Entry(mainframe, width=20, textvariable=zoning)
width_entry.grid(column=2, row=2, sticky=(W, E))

dimensions = StringVar()
width_entry = ttk.Entry(mainframe, width=20, textvariable=dimensions)
width_entry.grid(column=2, row=3, sticky=(W, E))

floor_area = StringVar()
width_entry = ttk.Entry(mainframe, width=20, textvariable=floor_area)
width_entry.grid(column=2, row=4, sticky=(W, E))

date = StringVar()
width_entry = ttk.Entry(mainframe, width=20, textvariable=date)
width_entry.grid(column=2, row=5, sticky=(W, E))

owner = StringVar()
width_entry = ttk.Entry(mainframe, width=20, textvariable=owner)
width_entry.grid(column=2, row=6, sticky=(W, E))

# ----------------------------------------------------------------

address = str(address.get())
zoning = str(zoning.get())
dimensions = str(dimensions.get())
floor_area = str(floor_area.get())
date = str(date.get())
owner = str(owner.get())

ttk.Button(mainframe, text="Generate Report", command=run).grid(
    column=2, row=7, sticky=(W, E)
)

for child in mainframe.winfo_children():
    child.grid_configure(padx=20, pady=10)
width_entry.focus()
window.bind("<Return>", run)

window.mainloop()
