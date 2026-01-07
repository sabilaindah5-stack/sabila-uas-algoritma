# Fungsi untuk mencetak pola segitiga bintang
def cetak_pola(baris):
    for i in range(1, baris + 1):
        print("*" * i)

# Program utama
jumlah_baris = int(input("Masukkan jumlah baris: "))
cetak_pola(jumlah_baris)
