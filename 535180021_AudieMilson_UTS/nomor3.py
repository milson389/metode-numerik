# Audie Milson(535180021)

userInput = int(input('Masukkan jumlah barang yang ingin dimasukkan : '))
listBarang = []
listDuplicate = []
jumlah = {}

for i in range(userInput):
    barang = input('Masukkan nama barang : ')
    listBarang.append(barang)


print(set(listBarang))
dictionary = {i: listBarang.count(i) for i in listBarang}
barang2 = dictionary.items()
for key, value in barang2:
    print(key, ':', value)
