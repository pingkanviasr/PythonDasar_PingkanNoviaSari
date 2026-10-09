umur, ktp = 20, True
if umur >= 17:
    if ktp:
        print("boleh memilih")
    else:
        print("buat ktp dulu")

umur = 16
s = "dewasa" if umur >= 17 else "anak"
print(s)

hari = "sabtu"

match hari:
    case "sabtu" | "minggu":
        print("libur")
    case "senin":
        print("semangat")
    case _:
        print("hari kerja")