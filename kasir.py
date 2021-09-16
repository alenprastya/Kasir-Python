print("TOKO Esteh")
print("Pilihan lah Menu")
print("1. Es Teh")
harga_esteh = 5000
diskon = 10/100
print("2. Nutrisari")
harga_nutrisari = 3000
print("3. Jus Mangga")
harga_jus = 10000
opsi = int(input("pilihlah salah satu menu : "))

# Pembelian Es Teh
if opsi == 1:
    print("Anda Memilih Es teh")
jumlah_pesanan = int(input("Masukan Jumlah Pesanan : "))
if jumlah_pesanan == 1:
    uang = int(input("Masukan Jumlah Uang anda : "))
    print("Total Kembali :", uang-harga_esteh)

elif jumlah_pesanan > 1:
    print("Selamat Anda Mendapatkan diskon 10%")
    uang = int(input("Masukan Jumlah Uang : "))
    print("***************************")
    total_diskon = diskon * (jumlah_pesanan * harga_esteh)
    print("Total Diskon adalah :", total_diskon)
    total_belanja = (jumlah_pesanan*harga_esteh)-total_diskon
    print("Total  Belanja anda adalah : ", total_belanja)
    print("Total Uang Kembali : ", uang-total_belanja)
    print("****************************")
# Batas Pembelian Es Teh
