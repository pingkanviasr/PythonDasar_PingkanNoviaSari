try:
    angka = int(input("masukkan angka: "))
    hasil = 100 / angka
except ValueError:
    print("input harus berupa angka!")
except ZeroDivisionError:
    print("tidak bisa dibagi dengan nol!")
else:
    print(f"hasil: {hasil}")
finally:
    print("selesai")