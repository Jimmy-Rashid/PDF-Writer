address = ""
zoning = ""
dimensions = ""
floor_area = ""
date = ""
owner = ""
check_1 = ""
check_2 = ""
check_3 = ""
check_4 = ""
check_5 = ""
check_6 = ""
check_7 = ""
check_8 = ""
check_9 = ""
check_no = ""
check_yes = ""
check_setbacks = ""
check_45_percent = ""

text_bank = {
    "Address": address,
    "Zoning District": zoning,
    "Lot Dimensions": dimensions,
    "Floor Area": floor_area,
    "Date": date,
    "Owner Name:": owner,
    "Check 1": check_1,
    "Check 2": check_2,
    "Check 3": check_3,
    "Check 4": check_4,
    "Check 5": check_5,
    "Check 6": check_6,
    "Check 7": check_7,
    "Check 8": check_8,
    "Check 9": check_9,
    "Check No": check_no,
    "Check Yes": check_yes,
    "Check Setbacks": check_setbacks,
    "Check 45%": check_45_percent,
}

for x, label_text in enumerate(text_bank, start=1):
    print(label_text)