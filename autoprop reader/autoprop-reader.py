from pypdf import PdfReader, PdfWriter

reader = PdfReader("autoprop reader/AUTOPROP-R-7170-DOW-AV--Burnaby-V5J-3W9.pdf")

pages = reader.pages
pdf_length = len(reader.pages)

page_1 = reader.pages[0].extract_text()
page_2 = reader.pages[1].extract_text()

list_1 = []
list_2 = []

for line in page_1.splitlines():
    list_1.append(line)

address = list_1[1]
city = list_1[2]
postal_code = list_1[3]
country = list_1[4]
property_id = list_1[5].split(" ")[1]  # unused in report

for line in page_2.splitlines():
    if line.find("Zoning") != -1:
        zoning = line.split(" ")[1]
    else:
        zoning = ""

    if line.find("Dimensions") != -1:
        dimensions = " ".join(line.split(" ")[3:6])
        print(dimensions)
    else:
        dimensions = ""

    if line.find("Floor Area") != -1:
        floor_area = line.split(" ")[2]
    else:
        floor_area = ""
