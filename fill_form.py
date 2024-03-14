from pypdf import PdfReader, PdfWriter

date = "Test Text"
owner = "Test Text"
zoning = "Test Text"
address = "Test Text"
dimensions = "Test Text"
floor_area = "Test Text"

input_file = "Form.pdf"
output_file = str(address) + " - Property Report.pdf"

reader = PdfReader(input_file)

writer = PdfWriter()
writer.append(reader)

fields = {
    "date": date,
    "owner": owner,
    "zoning": zoning,
    "address": address,
    "dimensions": dimensions,
    "floor_area": floor_area,
}

keys = fields.keys()
field_counter = 0

for count in range(len(reader.pages)):
    if field_counter < len(fields):
        field_dict = {f'{list(keys)[field_counter]}' : f'{fields[list(keys)[field_counter]]}'}
        writer.update_page_form_field_values(
            writer.pages[count],
            field_dict,
            auto_regenerate=False,
        )
        field_counter += 1
        print(field_dict)

with open(output_file, "wb") as output_stream:
    writer.write(output_stream)
