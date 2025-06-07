# Latihan 1.3
# Menghitung waktu yang dibutuhkan dengan compound interest

def hitung_waktu_compound_interest(principal, target, rate):
    tahun = 0
    while principal < target:
        principal *= (1 + rate/100)
        tahun += 1
    return tahun

principal = 200_000_000  # 200 juta
target = 400_000_000  # 400 juta
rate = 10  # bunga 10% per tahunnya

# Hitung waktu yang dibutuhkan dan inilah hasilnya cik woilah
tahun_diperlukan = hitung_waktu_compound_interest(principal, target, rate)
print(f"Waktu yang dibutuhkan: {tahun_diperlukan} tahun")

print("\n=== Hak Cipta: Ramji Junfaris ===\n")