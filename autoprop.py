from pypdf import PdfReader, PdfWriter

from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog

import datetime

window = Tk()
window.update_idletasks()
window.title("Property Report Creator")

mainframe = ttk.Frame(window, padding="5 20 5 20")
mainframe.grid(column=0, row=0, sticky=(N))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

text_font = font.Font(size=12, weight="normal")

style = ttk.Style()
style.configure("TButton", font=text_font)

# Main function
# ----------------------------------------------------------------


def run(
    owner,
    address,
    zoning,
    lot_dimensions,
    lot_area,
    date,
):
    input_file = "Template Forms/Powerhouse 4-Plex Template.pdf"
    output_file = str(address) + " - Proposal.pdf"

    reader = PdfReader(input_file)

    writer = PdfWriter()
    writer.append(reader)

    fields = {
        "owner": owner,
        "zoning": zoning,
        "address": address,
        "lot_dimensions": lot_dimensions,
        "lot_area": lot_area,
    }
    
    for x in range(1, 19):
        date_number = "date_" +str(x)
        fields[date_number] = date

    keys = fields.keys()

    for count in range(len(reader.pages)):
        for field in range(len(fields)):
            writer.update_page_form_field_values(
                writer.pages[count],
                {f"{list(keys)[field]}": f"{fields[list(keys)[field]]}"},
                auto_regenerate=False,
            )

    with open("Property Reports/" + output_file, "wb") as output_stream:
        writer.write(output_stream)


# ----------------------------------------------------------------

# Reads AutoProp report
# ----------------------------------------------------------------

file = filedialog.askopenfile(mode="r")
autoprop_reader = PdfReader(file.name)

page_1 = autoprop_reader.pages[0].extract_text()
page_2 = autoprop_reader.pages[1].extract_text()

list_1 = []
list_2 = []

for line in page_1.splitlines():
    list_1.append(line)

address = StringVar(value=f"{list_1[1]}")
city = StringVar(value=f"{list_1[2]}")
country = StringVar(value=f"{list_1[4]}")  # unused in report
postal_code = StringVar(value=f"{list_1[3]}")  # unused in report
property_id = StringVar(value=f"{list_1[5].split(' ')[1]}")  # unused in report

zoning = StringVar(value="")
lot_dimensions = StringVar(value="")
lot_area = StringVar(value="")

date = StringVar(value=f"{datetime.datetime.now().strftime('%B %d, %Y')}")

for line in page_2.splitlines():
    if line.find("Zoning") != -1:
        zoning.set(line.split(" ")[1])
    if line.find("Dimensions") != -1:
        lot_dimensions.set(" ".join(line.split(" ")[3:6]))
    if line.find("Floor Area") != -1:
        lot_area.set(line.split(" ")[2])

# ----------------------------------------------------------------

# Labels
# ----------------------------------------------------------------

text_bank_1 = [
    "Owner Name",
    "Address",
    "Zoning District",
    "Lot Dimensions",
    "Lot Area",
    "Date",
]

for x, label_text in enumerate(text_bank_1, start=1):
    ttk.Label(mainframe, text=label_text, font=text_font).grid(
        column=1, row=x, sticky=(W, E)
    )

# ----------------------------------------------------------------

# Entry
# ----------------------------------------------------------------

owner = StringVar(value="")
date = StringVar(value=f"{datetime.datetime.now().strftime('%B %d, %Y')}")

entries = [
    owner,
    address,
    zoning,
    lot_dimensions,
    lot_area,
    date,
]

for x, entry in enumerate(entries, start=1):
    ttk.Entry(mainframe, width=20, font=text_font, textvariable=entry).grid(
        column=2, row=x, sticky=(W, E)
    )

# ----------------------------------------------------------------


def setup():
    run(
        owner.get(),
        address.get(),
        zoning.get(),
        lot_dimensions.get(),
        lot_area.get(),
        date.get(),
    )


ttk.Button(mainframe, style="TButton", text="Generate Report", command=setup).grid(
    column=1, columnspan=2, row=7, ipady=5, sticky=(W, E)
)

for child in mainframe.winfo_children():
    child.grid_configure(padx=20, pady=10)
window.bind("<Return>", setup)

window.mainloop()
