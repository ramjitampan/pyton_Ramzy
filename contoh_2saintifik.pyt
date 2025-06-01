#nilai kurs 1 us$ ke IDR
kursusd = 13950

#Informasi program
print('program konversi US$ ke IDR')
print('kurs saat ini 1 US$ = Rp.', kursusd, 'rupiah')
#input jum;ah nilainya US$ yang mau di tukar
jumlahusd=float (input('masukan jumlah uang yang mau ditukar ke rupiah:'))
#hitung nilainya dalam rupiah
dalamrupiah = jumlahusd * kursusd
#tampilkan hasilnya
print('nilai', jumlahusd, 'US$ setara dengan Rp.', dalamrupiah, 'rupiah')

print("\n=== Hak Cipta: Ramji Junfaris ===\n")