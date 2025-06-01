# 1) Membuat dan mencetak tuple
kota = ("Jakarta", "Jogja", "Surabaya")
print("kota:", kota)
print("kota[0]:", kota[0])
print("kota[1]:", kota[1])
print("kota[2]:", kota[2])
print()

# 2) Membagi tuple ke dalam string
str1, str2, str3 = kota
print("str1:", str1)
print("str2:", str2)
print("str3:", str3)
print()

# 3) Membuat tuple dari string
tpl = tuple("Belajar Python")
print("tpl:", tpl)
print()

# 4) Membuat tuple semua huruf kecuali huruf pertama
tpl1 = tuple("Belajar Python"[1:])
print("tpl1:", tpl1)
print()

# 5) Mencetak tuple secara terbalik
name = ("Jaka", "Joko", "Jono")
rev_name = name[::-1]
print("urutan:", name)
print("urutan_terbalik:", rev_name)