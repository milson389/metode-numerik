# Audie Milson (535180021)
import numpy as np
from prettytable import PrettyTable


def errorTrue(fx, fprediksi):
    return "{:.4f}".format(abs(((fx-fprediksi)/fx)*100))


def dapetEa(fp, fp1):
    return "{:.4f}".format(abs(((fp1-fp)/fp1)*100))


def hasilNilaiX(x, xTanya, orde):
    nilaiX = 1
    orde = int(orde)
    for i in range(orde):
        nilaiX *= xTanya-x[i]
    return nilaiX


def newtonInterpolation(x, fx, xTanya, orde):
    n = int(orde)+1
    b = np.zeros((n, n))

    for i in range(n):
        b[i][0] = fx[i]

    for i in range(1, n):
        for j in range(n-i):
            b[j][i] = ((b[j][i - 1] - b[j + 1][i - 1]) /
                       (x[j] - x[i + j]))

    jumlah = fx[0]
    for i in range(1, n):
        jumlah += hasilNilaiX(x, xTanya, i)*b[0][i]
    listHasil.append(jumlah)

    nr.add_row([i, b[0][i], hasilNilaiX(x, xTanya, i), jumlah])
    return jumlah


def lagrange(a, fa, aTanya, orde):
    result = 0
    list = []
    xn = []
    interpolasi = int(orde)+1
    for i in range(interpolasi):
        l = 1
        for j in range(interpolasi):
            if(j != i):
                l *= (aTanya-a[j])/(a[i]-a[j])
        list.append(l)
        xn.append(a[i])
        result += l*fa[i]
    lr.add_row([i, xn, list, result])
    return result


nrx = [10.5, 12, 12.4, 12.8]
fnrx = [45.2, 58.1, 60.2, 64.4]
nrxTanya = 11.5
fTrue = 55.92
listHasil = []

nr = PrettyTable()
nama_field = ['Orde', 'Nilai Bi', 'X-Xi', 'Hasil']
nr.field_names = nama_field
nr.clear_rows()

print('\nPrediksi Hasil Promosi :')
iterasi = int(input('Masukkan nilai N orde ke N yang diinginkan : '))
for i in range(0, iterasi):
    orde = i+1
    print('\nOrde ', orde)
    print("Hasil : ", "{:.4f}".format(
        newtonInterpolation(nrx, fnrx, nrxTanya, orde)))
    if(i == 0):
        continue
    else:
        print("ET (55.92) : ", errorTrue(fTrue, listHasil[i]), '%')
        print('Ea : ', dapetEa(listHasil[i-1], listHasil[i]), '%')

print(nr)


xi = [6.509, 8.0814, 3.9090, 6.1082, 9.9294,
      9.9629, 2.2558, 3.0724, 1.5146, 5.4081]
fxi = [16.41, 16.6266, 15.9, 16.3467, 16.8325,
       16.8359, 15.3505, 15.6594, 14.9522, 16.2245]
xTanya = 7.3
xTanya1 = 5.0

lr = PrettyTable()
lr.field_names = ['Orde', 'Xn', 'Li', 'Fx(i)']

print()
orde = int(input('Masukkan Nilai N ( Orde ke -N ) untuk f(x=7.3) : '))
print("\nHasil Perhitungan Orde", orde, ": ",
      "{:.4f}".format(lagrange(xi, fxi, xTanya, orde)))
lr.clear_rows()

for i in range(1, orde+1):
    lagrange(xi, fxi, xTanya, i)
print(lr)
lr.clear_rows()

orde1 = int(input('Masukkan Nilai N ( Orde ke -N ) untuk f(x=5.0) : '))
print("\nHasil Perhitungan Orde", orde1,
      ": " "{:.4f}".format(lagrange(xi, fxi, xTanya1, orde1)))
lr.clear_rows()

for i in range(1, orde+1):
    lagrange(xi, fxi, xTanya1, i)
print(lr)
lr.clear_rows()


nr.clear_rows()
iterasi = int(input('Masukkan nilai N orde ke N yang diinginkan : '))
for i in range(0, iterasi):
    orde = i+1
    print('\nOrde ', orde)
    print("Hasil : ", "{:.4f}".format(
        newtonInterpolation(xi, fxi, xTanya, orde)))
    if(i == 0):
        continue
    else:
        # print("ET (55.92) : ", errorTrue(fTrue, listHasil[i]), '%')
        print('Ea : ', dapetEa(listHasil[i-1], listHasil[i]), '%')

print(nr)

# # Soal 2
# nilai = [10.5, 12, 12.4, 12.8]
# fNilai = [45.2, 58.1, 60.2, 64.4]
# nilaiTanya = 11.5

# print("\nHasil Perhitungan Orde", len(nilai)-1,
#       ": " "{:.4f}".format(lagrange(nilai, fNilai, nilaiTanya, len(nilai)-1)))
# lr.clear_rows()

# for i in range(1, len(nilai)):
#     lagrange(nilai, fNilai, nilaiTanya, i)
# print(lr)
# lr.clear_rows()

# for i in range(1, len(nilai)):
#     print("\nHasil Perhitungan Orde", i,
#           ": " "{:.4f}".format(lagrange(nilai, fNilai, nilaiTanya, i)))
#     if(i == 1):
#         continue
#     else:
#         print('Nilai EA dibandingkan Orde sebelumnya : ',
#               dapetEa(lagrange(nilai, fNilai, nilaiTanya, i-1), lagrange(nilai, fNilai, nilaiTanya, i)), '%')
#         print()
