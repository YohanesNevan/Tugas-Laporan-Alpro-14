import re  # Mengimpor library regex

# Mendefinisikan string yang akan dibagi
txt = "The rain in Spain"

# Membagi string berdasarkan spasi
x = re.split("\s", txt)
print(x)  # Mencetak hasil pembagian

# Membagi string berdasarkan spasi, tetapi hanya pada pembagian pertama
y = re.split("\s", txt, 1)
print(y)  # Mencetak hasil pembagian
