from pypdf import PdfReader, PdfWriter
from pypdf.constants import AnnotationDictionaryAttributes


date = "Test Date"
city = "Test City"
owner = "Test Owner"
zoning = "Test Zoning"
address = "Test Address"
dimensions = "Test Dimensions"
floor_area = "Test Floor Area"

input_file = "Burnaby Template - Form.pdf"
# output_file = str(address) + " - Property Report.pdf"
output_file = "Property Report.pdf"

reader = PdfReader(input_file)
# print(reader.get_fields().keys())  # prints the fields in the pdf

writer = PdfWriter()
writer.append(reader)

fields = []
for page in reader.pages:
    for annot in page.annotations:
        annot = annot.get_object()
        if annot[AnnotationDictionaryAttributes.Subtype] == "/Widget":
            fields.append(annot)
            
print(fields[0])


# for count in range(len(reader.pages)):
#     for field in range(len(fields)):
#         writer.update_page_form_field_values(
#             writer.pages[count],
#             {f"{list(keys)[field]}": f"{fields[list(keys)[field]]}"},
#             auto_regenerate=False,
#         )

# with open(output_file, "wb") as output_stream:
#     writer.write(output_stream)

# # prints keys and values in the dict
# for x in range(7):
#     print(f"{list(keys)[x]}"+": "+f"{fields[list(keys)[x]]}")
