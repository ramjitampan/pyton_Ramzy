# Latihan 1.2
# Perhitungan keuntungan Gerard

def hitung_keuntungan(harga_beli, harga_jual, berat):
    modal = harga_beli * berat
    hasil_jual = harga_jual * berat
    keuntungan = hasil_jual - modal
    persentase = (keuntungan / modal) * 100
    return keuntungan, persentase

# Soal Nomor 1
harga_beli_1 = 650000
harga_jual_1 = 685000
berat_1 = 25
keuntungan_1, persentase_1 = hitung_keuntungan(harga_beli_1, harga_jual_1, berat_1)
print(f"Keuntungan Gerard: Rp {keuntungan_1}, {persentase_1:.2f}%")

# Soal Nomor 2
#Jika Gerard membeli lagi sebanyak 15 kg dengan harga beli 685000 dan harga jual naik sebanyak 715000
harga_beli_2 = 685000
berat_2 = 15
harga_jual_2 = 715000

modal_total = (harga_beli_1 * berat_1) + (harga_beli_2 * berat_2)
hasil_jual_total = harga_jual_2 * (berat_1 + berat_2)
keuntungan_total = hasil_jual_total - modal_total
persentase_total = (keuntungan_total / modal_total) * 100

print(f"Keuntungan Gerard setelah membeli lagi🤑: Rp {keuntungan_total}, {persentase_total:.2f}%")

print("\n=== Hak Cipta: Ramji Junfaris ===\n")