# Program menentukan kategori usia

usia = int(input("Masukkan usia: "))

if usia >= 0 and usia <= 5:
    kategori = "Balita"
elif usia >= 6 and usia <= 12:
    kategori = "Anak-anak"
elif usia >= 13 and usia <= 17:
    kategori = "Remaja"
elif usia >= 18 and usia <= 59:
    kategori = "Dewasa"
elif usia >= 60:
    kategori = "Lansia"
else:
    kategori = "Usia tidak valid"

print("Kategori usia:", kategori)
