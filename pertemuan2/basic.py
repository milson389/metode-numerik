# variables
import math

a = 7
b = 3.141592
c = "Hello World"
d = 'The quick brown fox'

# menghasilkan output
print(a)
print("Nilai pi = ", b)
print(c)
print("Some people says, ", d)

# user input
x = input("Masukkan sebuah bilangan: ")
print(x)
print(type(x))

# ubah tipe data jadi int
y = int(x) + 5
print(y)

# operator
x = 15
y = 6

z = x + y
print(z)

z = x - y
print(z)

z = x * y
print(z)

z = x / y
print(z)

z = x % y  # modulus
print(z)

z = x ** y  # pangkat
print(z)

# import untuk matkul metnum
print(math.log(100))  # logaritma natural, basis e
print(math.log10(1000))  # log basis 10
print(math.log2(1000))  # log basis 2
print(math.sqrt(4250))  # akar
print(math.pi)
print(math.e)  # math.e ** 5 sama dengan math.exp(5)
print(math.exp(5))

# membuat function


def luas(a, t):
    L = 0.5*a*t
    return L


alas = float(input("Masukkan alas: "))
tinggi = float(input("Masukkan tinggi: "))

print("Luas = ", luas(alas, tinggi))

# list
arr = [15, 21, 23, 45, 53]  # list, elemen di dalamnya masih bisa diubah
print(arr[0])  # zero-indexed
print(arr[1])
print(len(arr))  # panjang list
print(arr)
arr.append(63)  # memasukkan value ke list
arr.append(78)
arr.append(3)
print(arr)

names = ["Ari", 1.34115, "Budi", 45, "Charlie"]
print(names)
print(names[0:2])  # yang diambil dari 0 sampai sebelum index 2
print(names[1:])  # mencetak dari 1 sampai habis
print(names[:3])  # mencetak sampai index sebelum 3

# tuples
tup = (4, 5, 6)  # tuples, element di dalamnya tidak bisa diubah

# dictionary, terdiri dari key dan value
a = {
    "username": "labfti",
    "uid": 500,
    "home": "/home/labfti"
}

print(a)
print(a['username'])

# array 2d
b = [[3, 4], [5, 6], [7, 8]]
print(b[1][0])

# conditional
a = int(input("Input a number: "))
b = int(input("Input another number: "))

# jika kondisinya panjang gunakan tanda kurung buka kurung tutup
if a < b:
    z = b
else:
    z = a

print("The maximum is", z)

num = int(input("Input a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

num = 1000
if(num == 1000):
    print("A thousand")
elif not(num > 0 or num > 100):
    print("More than 100")
else:
    print("Nope")


# Loops
for i in range(1, 10):  # dari 1-9
    print(i)

for i in range(10):  # dari 0-9
    print(i)

for i in range(1, 100, 10):  # 1 sampai 100 dengan selisih 10
    print(i)

for i in names:  # mencetak isi array dengan looping
    print(i)

for i in names[0:3]:  # mencetak isi array dengan looping
    print(i)

# While loop
a = 0
while(a < 5):
    print(a)
    a += 1

# Looping tuples
tup = (5, 4, 3, 2, 1)
for t in tup:
    print(t)
