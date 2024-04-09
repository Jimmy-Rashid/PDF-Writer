from pypdf import PdfReader, PdfWriter

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import datetime

window = Tk()
window.update_idletasks()
window.title("Property Report Creator")

mainframe = ttk.Frame(window, padding="5 5 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Main function
# ----------------------------------------------------------------


def run(
    address,
    zoning,
    dimensions,
    floor_area,
    date,
    owner,
    check_1,
    check_2,
    check_3,
    check_4,
    check_5,
    check_6,
    check_7,
    check_8,
    check_9,
    check_no,
    check_yes,
    check_setbacks,
    check_45_percent,
):
    city.set(city.get() + ", BC")
    input_file = "Burnaby Template - Form.pdf"
    output_file = str(address) + " - Property Report.pdf"

    reader = PdfReader(input_file)
    # print(reader.get_fields().keys())  # prints the fields in the pdf

    writer = PdfWriter()
    writer.append(reader)

    fields = {
        "date": date,
        "city": city,
        "owner": owner,
        "zoning": zoning,
        "check_1": check_1,
        "check_2": check_2,
        "check_3": check_3,
        "check_4": check_4,
        "check_5": check_5,
        "check_6": check_6,
        "check_7": check_7,
        "check_8": check_8,
        "check_9": check_9,
        "address_1": address,
        "address_2": address,
        "check_no": check_no,
        "check_yes": check_yes,
        "dimensions": dimensions,
        "floor_area": floor_area,
        "check_setbacks": check_setbacks,
        "check_45_percent": check_45_percent,
    }

    keys = fields.keys()

    for count in range(len(reader.pages)):
        for field in range(len(fields)):
            writer.update_page_form_field_values(
                writer.pages[count],
                {f"{list(keys)[field]}": f"{fields[list(keys)[field]]}"},
                auto_regenerate=False,
            )

    with open(output_file, "wb") as output_stream:
        writer.write(output_stream)

    # # prints keys and values in the dict
    # for x in range(7):
    #     print(f"{list(keys)[x]}"+": "+f"{fields[list(keys)[x]]}")


# ----------------------------------------------------------------

# Reads AutoProp report
# ----------------------------------------------------------------

# file = filedialog.askopenfile(mode="r")
# autoprop_reader = PdfReader(file.name)

file = "autoprop reader/AUTOPROP-R-7170-DOW-AV--Burnaby-V5J-3W9.pdf"
autoprop_reader = PdfReader(file)

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
dimensions = StringVar(value="")
floor_area = StringVar(value="")

date = StringVar(value=f"{datetime.datetime.now().strftime('%B %d, %Y')}")

for line in page_2.splitlines():
    if line.find("Zoning") != -1:
        zoning.set(line.split(" ")[1])
    if line.find("Dimensions") != -1:
        dimensions.set(" ".join(line.split(" ")[3:6]))
    if line.find("Floor Area") != -1:
        floor_area.set(line.split(" ")[2])

# ----------------------------------------------------------------

# Labels
# ----------------------------------------------------------------

text_bank_1 = [
    "Address",
    "Zoning District",
    "Lot Dimensions",
    "Floor Area",
    "Date",
    "Owner Name",
]

text_bank_2 = [
    "Check 1",
    "Check 2",
    "Check 3",
    "Check 4",
    "Check 5",
    "Check 6",
    "Check 7",
]

text_bank_3 = [
    "Check 8",
    "Check 9",
    "Check No",
    "Check Yes",
    "Check Setbacks",
    "Check 45%",
]

for x, label_text in enumerate(text_bank_1, start=1):
    ttk.Label(mainframe, text=label_text).grid(column=1, row=x, sticky=(W, E))

for x, label_text in enumerate(text_bank_2, start=1):
    ttk.Label(mainframe, text=label_text).grid(column=3, row=x, sticky=(W, E))
    
for x, label_text in enumerate(text_bank_3, start=1):
    ttk.Label(mainframe, text=label_text).grid(column=5, row=x, sticky=(W, E))

# ----------------------------------------------------------------

# Entry
# ----------------------------------------------------------------

owner = StringVar(value="")
check_1 = StringVar(value="/Off")
check_2 = StringVar(value="/Off")
check_3 = StringVar(value="/Off")
check_4 = StringVar(value="/Off")
check_5 = StringVar(value="/Off")
check_6 = StringVar(value="/Off")
check_7 = StringVar(value="/Off")
check_8 = StringVar(value="/Off")
check_9 = StringVar(value="/Off")
check_no = StringVar(value="/Off")
check_yes = StringVar(value="/Off")
check_setbacks = StringVar(value="/Off")
check_45_percent = StringVar(value="/Off")

entries = [
    address,
    zoning,
    dimensions,
    floor_area,
    date,
    owner,
]

check_list = [
    check_1,
    check_2,
    check_3,
    check_4,
    check_5,
    check_6,
    check_7,
    check_8,
    check_9,
    check_no,
    check_yes,
    check_setbacks,
    check_45_percent,
]

for x, entry in enumerate(entries, start=1):
    ttk.Entry(mainframe, width=20, textvariable=entry).grid(
        column=2, row=x, sticky=(W, E)
    )

for x, check in enumerate(check_list, start=1):
    if x <= 7:
        ttk.Checkbutton(
            mainframe, variable=check, onvalue="/Yes", offvalue="/Off"
        ).grid(column=4, row=x, sticky=(W, E))
    else:
        ttk.Checkbutton(
            mainframe, variable=check, onvalue="/Yes", offvalue="/Off"
        ).grid(column=6, row=x-7, sticky=(W, E))

# ----------------------------------------------------------------


def setup():
    run(
        address.get(),
        zoning.get(),
        dimensions.get(),
        floor_area.get(),
        date.get(),
        owner.get(),
        check_1.get(),
        check_2.get(),
        check_3.get(),
        check_4.get(),
        check_5.get(),
        check_6.get(),
        check_7.get(),
        check_8.get(),
        check_9.get(),
        check_no.get(),
        check_yes.get(),
        check_setbacks.get(),
        check_45_percent.get(),
    )


ttk.Button(mainframe, text="Generate Report", command=setup).grid(
    column=5, columnspan=2, row=7, sticky=(W, E)
)

for child in mainframe.winfo_children():
    child.grid_configure(padx=20, pady=10)
window.bind("<Return>", setup)

window.mainloop()
