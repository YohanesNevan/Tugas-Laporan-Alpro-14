import re  # Mengimpor library regex

# Mendefinisikan string yang akan diubah
txt = "Sang mata-mata sedang memata-matai kasus kaca mata di toko Matahari"

# Mengganti semua spasi dalam string dengan tanda "-"
x = re.sub("\s", "-", txt)
print(x)  # Mencetak hasil penggantian

# Mengganti dua spasi pertama dalam string dengan tanda "*"
y = re.sub("\s", "*", txt, 2)
print(y)  # Mencetak hasil penggantian
