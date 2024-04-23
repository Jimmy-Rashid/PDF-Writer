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
    dimensions,
    floor_area,
    date,
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
    output_file = str(address) + " - Property Report.pdf"
    city_text = str(city.get()) + ", BC"

    reader = PdfReader(input_file)
    # print(reader.get_fields().keys())  # prints the fields in the pdf

    writer = PdfWriter()
    writer.append(reader)

    fields = {
        "date": date,
        "city": city_text,
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

    with open("Property Reports/" + output_file, "wb") as output_stream:
        writer.write(output_stream)

    # # prints keys and values in the dict
    # for x in range(7):
    #     print(f"{list(keys)[x]}"+": "+f"{fields[list(keys)[x]]}")


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

if str(city.get()).lower() == "vancouver":
    input_file = "Template Forms/Vancouver Template - Form.pdf"
else:
    input_file = "Template Forms/Burnaby Template - Form.pdf"

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
    "Owner Name",
    "Address",
    "Zoning District",
    "Lot Dimensions",
    "Floor Area",
    "Date",
]

text_bank_2 = [
    "Property located in an eligible zoning district",
    "Single-family home with vehicular access to the rear yard\nfrom a side or rear lane or residential street",
    "Corner lot approval obtained from the engineering dpartment",
    "Complies with Streamside Protection and Enhancement Area regulations",
    "Accommodates up to three units (principal, secondary, laneway home),\nwhile remaining under a single title",
    "Space for one van-accessible parking with electric vehicle charging",
    "Allows for the provision of a private outdoor space and a \nrequired pathway access from the street",
    "Laneway home has separate sewer, water, and power services",
    "Free from heritage conservation constraints",
    "Not able to build laneway home",
    "Able to build laneway home",
    "Maximum coverage dictated by setbacks",
    "Maximum coverage dictated by 45% of area",
]

for x, label_text in enumerate(text_bank_1, start=1):
    ttk.Label(mainframe, text=label_text, font=text_font).grid(
        column=1, row=x, sticky=(W, E)
    )

for x, label_text in enumerate(text_bank_2, start=1):
    ttk.Label(mainframe, text=label_text, font=text_font).grid(
        column=3, row=x, sticky=(W, E)
    )

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
    owner,
    address,
    zoning,
    dimensions,
    floor_area,
    date,
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
    ttk.Entry(mainframe, width=20, font=text_font, textvariable=entry).grid(
        column=2, row=x, sticky=(W, E)
    )

for x, check in enumerate(check_list, start=1):
    ttk.Checkbutton(mainframe, variable=check, onvalue="/Yes", offvalue="/Off").grid(
        column=4, row=x, sticky=(W, E)
    )

# ----------------------------------------------------------------


def setup():
    run(
        owner.get(),
        address.get(),
        zoning.get(),
        dimensions.get(),
        floor_area.get(),
        date.get(),
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


ttk.Button(mainframe, style="TButton", text="Generate Report", command=setup).grid(
    column=3, columnspan=2, row=14, ipady=5, sticky=(W, E)
)

for child in mainframe.winfo_children():
    child.grid_configure(padx=20, pady=10)
window.bind("<Return>", setup)

window.mainloop()
