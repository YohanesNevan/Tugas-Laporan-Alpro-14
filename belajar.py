import re

# Membuka file mbox-short.txt
handle = open('mbox-short.txt')

count = 0  # Inisialisasi penghitung

# Iterasi setiap baris dalam file
for line in handle:
    line = line.rstrip()  # Menghapus spasi atau newline di akhir baris
    if re.search('From:', line):  # Mencari pola "From:" dalam baris
        count += 1  # Menambah penghitung jika ditemukan
        print(line)  # Mencetak baris yang cocok

# Mencetak jumlah total baris yang cocok
print("Count: ", count)

import re  # Mengimpor library regex

# Membuka file mbox-short.txt
handle = open('mbox-short.txt')

count = 0  # Inisialisasi penghitung

# Iterasi setiap baris dalam file
for line in handle:
    line = line.rstrip()  # Menghapus spasi atau newline di akhir baris
    if re.search('^From:', line):  # Mencari pola "From:" di awal baris
        count += 1  # Menambah penghitung jika ditemukan
        print(line)  # Mencetak baris yang cocok

# Mencetak jumlah total baris yang cocok
print("Count: ", count)



