from pypdf import PdfReader, PdfWriter

input_file = "test/template test/template_test.pdf"
output_file = "test/template test/output_test.pdf"

reader = PdfReader(input_file)
# print(reader.get_fields().keys())  # prints the fields in the pdf
fields = reader.get_fields().values()

writer = PdfWriter()
writer.append(reader)

writer.update_page_form_field_values(
    writer.pages[0],
    {fields: "test/Images/98280016_p0.jpg"},
    auto_regenerate=False,
)

with open(output_file, "wb") as output_stream:
    writer.write(output_stream)