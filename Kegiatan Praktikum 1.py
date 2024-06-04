import re  # Mengimpor library regex

# Mendefinisikan string yang akan dicari
txt = "Sang mata-mata sedang memata-matai kasus kaca mata di toko Matahari"

# Mencari semua kemunculan kata "mata" dalam string
x = re.findall("mata", txt)

# Mencari semua kemunculan kata "saya" dalam string
y = re.findall("saya", txt)

# Mencetak semua kemunculan kata "mata"
for i in x:
    print(i)

# Mengecek apakah ada kemunculan kata "saya" dan mencetak pesan sesuai
if y:
    print("Ada yang cocok!")
else:
    print("Tidak ada yang cocok!")