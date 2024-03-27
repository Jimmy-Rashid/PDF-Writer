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

date = StringVar()
owner = StringVar()
zoning = StringVar()
address = StringVar()
floor_area = StringVar()
dimensions = StringVar()

entries = [address, zoning, dimensions, floor_area, date, owner]

for x, entry in enumerate(entries, start=1):
    width_entry = ttk.Entry(mainframe, width=20, textvariable=entry)
    width_entry.grid(column=2, row=x, sticky=(W, E))

# ----------------------------------------------------------------


def setup():
    run(
        address.get(),
        zoning.get(),
        dimensions.get(),
        floor_area.get(),
        date.get(),
        owner.get(),
    )


ttk.Button(mainframe, text="Generate Report", command=setup).grid(
    column=2, row=7, sticky=(W, E)
)

for child in mainframe.winfo_children():
    child.grid_configure(padx=20, pady=10)
width_entry.focus()
window.bind("<Return>", setup)

window.mainloop()
