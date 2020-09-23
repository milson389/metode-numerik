# Audie Milson (535180021)

# Nomor 1
for i in range(1, 101):
    if((i % 3 == 0) and (i % 5 == 0)):
        print("FizzBuzz")
    elif(i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)

# Nomor 2
kalimatInput = input('Masukkan contoh kalimat Input: ').lower()
kata = list(kalimatInput)
vokal = ['a', 'i', 'u', 'e', 'o']
hurufVokal = []
hurufMati = []

for i in kata:
    if(i in vokal):
        hurufVokal.append(i)
    elif(i == ' '):
        continue
    else:
        hurufMati.append(i)


jumlahA = 0
jumlahI = 0
jumlahU = 0
jumlahE = 0
jumlahO = 0

for j in hurufVokal:
    if (j == 'a'):
        jumlahA += 1
    elif(j == 'i'):
        jumlahI += 1
    elif(j == 'u'):
        jumlahU += 1
    elif(j == 'e'):
        jumlahE += 1
    else:
        jumlahO += 1

print(kata)
print('a = ', jumlahA)
print('i = ', jumlahI)
print('u = ', jumlahU)
print('e = ', jumlahE)
print('o = ', jumlahO)
print()
print('Huruf mati = ', len(hurufMati))

# Nomor 3
inputAngka = input(
    'Masukkan maksimum 4 digit angka yang lebih besar dari 2000 : ')
daftarAngka = list(inputAngka)

angka = {
    "0": " ",
    "1": " satu ",
    "2": " dua ",
    "3": " tiga ",
    "4": " empat ",
    "5": " lima ",
    "6": " enam ",
    "7": " tujuh ",
    "8": " delapan ",
    "9": " sembilan "
}


hasil1 = angka[daftarAngka[0]]
hasil1 += 'ribu'

hasil2 = angka[daftarAngka[1]]
hasil3 = angka[daftarAngka[2]]
hasil4 = angka[daftarAngka[3]]

if (hasil2 == ' '):
    hasil2 = ''
else:
    hasil2 += 'ratus'

if(hasil3 == ' satu ' and hasil4 == ' '):
    hasil3 = ' sepuluh '
    hasil4 = ' '
elif(hasil3 == ' satu ' and hasil4 == ' satu '):
    hasil3 = ' se'
    hasil4 = 'belas '
elif(hasil3 == ' satu ' and hasil4 != ' satu '):
    hasil3 = angka[daftarAngka[2]]
    hasil4 = 'belas '
elif(hasil3 != 'satu' and hasil3 != ' '):
    hasil3 = angka[daftarAngka[2]]
    hasil3 += 'puluh'
    hasil4 = angka[daftarAngka[3]]

print(hasil1+hasil2+hasil3+hasil4)

# Nomor 4
kataAwal = input('Masukkan kata pertama : ').lower()
kataKedua = input('Masukkan kata kedua : ').lower()

charAwal = list(kataAwal)
charInput = list(kataKedua)

charPertama = []
charKedua = []

for i in charAwal:
    if(i == ' '):
        continue
    else:
        charPertama.append(i)

for j in charInput:
    if(j == ' '):
        continue
    else:
        charKedua.append(j)

# print(charPertama)
# print(charKedua)

if(sorted(charPertama) == sorted(charKedua)):
    print("kedua String ANAGRAM!")
else:
    print("kedua String BUKAN ANAGRAM!")
