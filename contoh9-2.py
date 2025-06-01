dic_email = dict()
lst = list()

fname = input('Nama File: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File tidak bisa dibuka:', fname)
    quit()

for baris in fhand:
    kata = baris.split()
    if len(kata) < 2 or kata[0] != 'From':
        continue
    else:
        if kata[1] not in dic_email:
            dic_email[kata[1]] = 1
        else:
            dic_email[kata[1]] += 1

for key, val in list(dic_email.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:1]:
    print(val, key)