# Fungsi untuk menghitung total gaji bulanan
def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    total_gaji = 0
    jam_normal = 8

    for i in range(hari_kerja):
        if jam_kerja_per_hari > jam_normal:
            jam_lembur = jam_kerja_per_hari - jam_normal
            gaji_harian = (jam_normal * tarif_per_jam) + (jam_lembur * tarif_per_jam * 1.5)
        else:
            gaji_harian = jam_kerja_per_hari * tarif_per_jam

        total_gaji += gaji_harian

    return total_gaji


# Program utama
tarif = float(input("Masukkan tarif gaji per jam        : "))
jam_per_hari = int(input("Masukkan jam kerja per hari       : "))
hari = int(input("Masukkan jumlah hari kerja/bulan  : "))

total = hitung_gaji(tarif, jam_per_hari, hari)

print("\nTotal gaji bulanan: Rp", total)
