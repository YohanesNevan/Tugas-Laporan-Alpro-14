import re  # Mengimpor library regex

# Mendefinisikan string yang akan dicari
txt = "Sang mata-mata sedang memata-matai kasus kaca mata di toko Matahari"

# Mencari keberadaan spasi pertama dalam string
x = re.search("\s", txt)

# Mencari keberadaan kata "saya" dalam string
y = re.search("saya", txt)

# Mengecek apakah spasi ditemukan dan mencetak posisinya
if x:
    print("Spasi ditemukan di:", x.start())
else:
    print("Spasi tidak ditemukan.")

# Mengecek apakah kata "saya" ditemukan dan mencetak hasilnya
if y:
    print("Kata 'saya' ditemukan.")
else:
    print("Kata 'saya' tidak ditemukan.")
    
import re  # Mengimpor library regex

# Membuka file mbox-short.txt
handle = open('mbox-short.txt')

# Iterasi setiap baris dalam file
for line in handle:
    line = line.rstrip()  # Menghapus spasi atau newline di akhir baris
    # Mencari baris yang dimulai dengan "X-", diikuti oleh karakter apa saja (.), kemudian ": ", dan diikuti oleh angka atau titik
    if re.search('^X-.*: [0-9.]+', line):
        print(line)  # Mencetak baris yang cocok

