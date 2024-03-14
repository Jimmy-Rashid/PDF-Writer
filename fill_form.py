from pypdf import PdfReader, PdfWriter

date = 0
owner = 0
zoning = 0
address = 0
dimensions = 0
floor_area = 0

reader = PdfReader("Form.pdf")
fields = reader.get_fields()
# count = len(reader.pages)
page = reader.pages[0]

writer = PdfWriter()
writer.append(reader)
writer.update_page_form_field_values(
    writer.pages[0],
    {"date": date},
    {"owner": owner},
    {"zoning": zoning},
    {"address": address},
    {"dimensions": dimensions},
    {"floor_area": floor_area},
    auto_regenerate=False,
)

output_file = address + " - Property Report"

with open(output_file, "wb") as output_stream:
    writer.write(output_stream)
