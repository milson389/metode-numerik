# Audie Milson(535180021)

userInput = int(input('Masukkan jumlah barang yang ingin dimasukkan : '))
listBarang = []
listDuplicate = []
jumlah = {}

for i in range(userInput):
    barang = input('Masukkan nama barang : ')
    listBarang.append(barang)


barang2 = set(listBarang)
result = {}
for i in barang2:
    result[i] = listBarang.count(i)

print(barang2)
for key, val in result.items():
    print(key, ':', val)
