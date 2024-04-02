from pypdf import PdfReader, PdfWriter

from tkinter import *
from tkinter import ttk

window = Tk()
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
    city = "Burnaby" + ", BC"
    input_file = "Burnaby Template - Form.pdf"
    # output_file = str(address) + " - Property Report.pdf"
    output_file = "Property Report.pdf"

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

# Labels
# ----------------------------------------------------------------

text_bank = [
    "Address",
    "Zoning District",
    "Lot Dimensions",
    "Floor Area",
    "Date",
    "Owner Name",
    "Check 1",
    "Check 2",
    "Check 3",
    "Check 4",
    "Check 5",
    "Check 6",
    "Check 7",
    "Check 8",
    "Check 9",
    "Check No",
    "Check Yes",
    "Check Setbacks",
    "Check 45%",
]

for x, label_text in enumerate(text_bank, start=1):
    ttk.Label(mainframe, text=label_text).grid(column=1, row=x, sticky=(W, E))

# ----------------------------------------------------------------

# Entry
# ----------------------------------------------------------------

date = StringVar(value="")
owner = StringVar(value="")
zoning = StringVar(value="")
address = StringVar(value="")
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
floor_area = StringVar(value="")
dimensions = StringVar(value="")
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

for x, check in enumerate(check_list, start=7):
    ttk.Checkbutton(mainframe, variable=check, onvalue="/Yes", offvalue="/Off").grid(
        column=2, row=x, sticky=(W, E)
    )

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
    column=2, row=20, sticky=(W, E)
)

for child in mainframe.winfo_children():
    child.grid_configure(padx=20, pady=10)
# width_entry.focus()
window.bind("<Return>", setup)

window.mainloop()
