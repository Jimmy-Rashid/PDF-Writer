from pypdf import PdfReader, PdfWriter

date = "Test Date"
city = "Test City"
owner = "Test Owner"
zoning = "Test Zoning"
address = "Test Address"
dimensions = "Test Dimensions"
floor_area = "Test Floor Area"

# "/Off" for empty squares, "/Yes" for checked
(
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
) = ["/Off"] * 13

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
