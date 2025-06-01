
def cek_semua_sama(tuple_data):
    hasil = True
    elemen_pertama = tuple_data[0]
    for item in tuple_data:
        if item != elemen_pertama:
            hasil = False
            break
    return hasil

data_tuple = (77, 77, 77, 77, 77)
print(cek_semua_sama(data_tuple))
