
data_diri = ('Ramzy Junfaris Hamonangan', '23343015', 'Binjai, Sumatra Utara')

print("NIM :", data_diri[1])
print("NAMA :", data_diri[0])
print("ALAMAT :", data_diri[2])

nim_tuple = ()
for karakter in data_diri[1]:
    nim_tuple += (karakter,)
print("NIM:", nim_tuple)

nama_depan = data_diri[0].split()[0].lower()
nama_depan_tuple = ()
for huruf in nama_depan:
    nama_depan_tuple += (huruf,)
print("NAMA DEPAN:", nama_depan_tuple)

nama_terbalik_tuple = ()
nama_terbalik_list = data_diri[0].split()
nama_terbalik_list.reverse()
for bagian in nama_terbalik_list:
    nama_terbalik_tuple += (bagian,)
print("NAMA TERBALIK:", nama_terbalik_tuple)
