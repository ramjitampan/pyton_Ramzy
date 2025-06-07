
nama_file = input("Enter a file name: ")
try:
    file_buka = open(nama_file)
except:
    print("File tidak bisa dibuka:", nama_file)
    exit()

jumlah_jam = {}

for baris in file_buka:
    if baris.startswith("From "):
        bagian = baris.split()
        waktu = bagian[5]
        jam = waktu.split(":")[0]
        if jam in jumlah_jam:
            jumlah_jam[jam] += 1
        else:
            jumlah_jam[jam] = 1

daftar_jam = list(jumlah_jam.items())
daftar_jam.sort()

for jam, jumlah in daftar_jam:
    print(jam, jumlah)
