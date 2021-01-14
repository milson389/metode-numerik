# Audie Milson ( 535180021 )
import math
import numpy as np
import matplotlib.pyplot as plt


def hitungB(f1, f0, x1, x0):
    return ((f1-f0)/(x1-x0))


def ordeSatu(f0, f1, x0, x1, x):
    b1 = hitungB(f1, f0, x1, x0)
    return f0 + b1*(x-x0)


def ordeDua(hasilSatu, f2, f1, f0,  x2, x1, x0, x):
    b1 = hitungB(f1, f0, x1, x0)
    bagian2 = hitungB(f2, f1, x2, x1)
    b2 = (bagian2-b1)/(x2-x0)
    return hasilSatu + b2*(x-x0)*(x-x1)


def ordeTiga(hasilDua, f3, f2, f1, f0, x3, x2, x1, x0, x):
    b1 = hitungB(f1, f0, x1, x0)
    bagian2 = hitungB(f2, f1, x2, x1)
    b2 = (bagian2-b1)/(x2-x0)
    bagian3 = (hitungB(f3, f2, x3, x2)-bagian2)/(x3-x1)
    b3 = (bagian3-b2)/(x3-x0)
    return hasilDua + b3*(x-x0)*(x-x1)*(x-x2)


def errorTrue(fx, fprediksi):
    return "{:.4f}".format(abs(((fx-fprediksi)/fx)*100))


def dapetEa(fp, fp1):
    return "{:.4f}".format(abs(((fp1-fp)/fp1)*100))


# Contoh Soal
x = 11.5
fx = 55.92
x0 = 10.5
fx0 = 45.2
x1 = 12
fx1 = 58.1
x2 = 12.4
fx2 = 60.2
x3 = 12.8
fx3 = 64.4

fPrediksi = ordeSatu(fx0, fx1, x0, x1, x)
fPrediksi2 = ordeDua(fPrediksi, fx2, fx1, fx0, x2, x1, x0, x)
fPrediksi3 = ordeTiga(fPrediksi2, fx3, fx2, fx1, fx0, x3, x2, x1, x0, x)

print("\nOrde 1 \n------")
print("Hasil Prediksi : ", "{:.2f}".format(fPrediksi))
print("Error True : ", errorTrue(fx, fPrediksi), "%")

print("\nOrde 2 \n------")
print("Hasil Prediksi : ", "{:.4f}".format(fPrediksi2))
print("Error True (hasil asli = 55.92) : ", errorTrue(fx, fPrediksi2), "%")
print("EA : ", dapetEa(fPrediksi, fPrediksi2), '%')

print("\nOrde 3 \n------")
print("Hasil Prediksi : ", "{:.4f}".format(fPrediksi3))
print("Error True (hasil asli = 55.92) : ", errorTrue(fx, fPrediksi3), "%")
print("EA : ", dapetEa(fPrediksi2, fPrediksi3), '%')

# Contoh soal 4
v = 7
v0 = 6
fV0 = 5.39
v1 = 8
fV1 = 5.06
v2 = 9
fV2 = 4.94
v3 = 10
fV3 = 4.85

prediksi1 = ordeSatu(fV0, fV1, v0, v1, v)
prediksi2 = ordeDua(prediksi1, fV2, fV1, fV0, v2, v1, v0, v)
prediksi3 = ordeTiga(prediksi2, fV3, fV2, fV1, fV0, v3, v2, v1, v0, v)

print("\nPrediksi nilai tabel distribusi f dengan v1 = 7 v2 = 10\n-------------------------------------------------------- ")
print("\nOrde 1 \n------")
print("Hasil Prediksi : ", "{:.3f}".format(prediksi1))
print("\nOrde 2 \n------")
print("Hasil Prediksi : ", "{:.2f}".format(prediksi2))
print("EA : ", dapetEa(prediksi1, prediksi2), '%')
print("\nOrde 3 \n------")
print("Hasil Prediksi : ", "{:.2f}".format(prediksi3))
print("EA : ", dapetEa(prediksi2, prediksi3), '%')

# Metode Lagrange
# xi = [10.5, 12, 12.4, 12.8]
# fxi = [45.2, 58.1, 60.2, 64.4]
# xiTanya = 11.5

# x = [6, 8, 9, 10]
# fx = [5.39, 5.06, 4.94, 4.85]
# xTanya = 7
list = []
prev = []


def lagrange(a, fa, aTanya, orde):
    result = 0
    interpolasi = int(orde)+1
    for i in range(interpolasi):
        l = fa[i]
        for j in range(interpolasi):
            if(j != i):
                l *= (aTanya-a[j])/(a[i]-a[j])
                list.append("{:.4f}".format(l/fa[i]))
        result += l
    return result


# lagRange(xi, fxi, xiTanya, 3)
# print(list)
xi = [6.509, 8.0814, 3.9090, 6.1082, 9.9294,
      9.9629, 2.2558, 3.0724, 1.5146, 5.4081]
fxi = [16.41, 16.6266, 15.9, 16.3467, 16.8325,
       16.8359, 15.3505, 15.6594, 14.9522, 16.2245]
xTanya = 7.3
xTanya1 = 5.0

orde = int(input('Masukkan Nilai N ( Orde ke -N ) untuk f(x=7.3) : '))
print("\nHasil Perhitungan Orde", orde,
      ": " "{:.4f}".format(lagrange(xi, fxi, xTanya, orde)))

# Untuk menampilkan hasil per orde yang ditentukan
for i in range(orde):
    print("\nHasil Perhitungan Orde", i+1,
          ": " "{:.4f}".format(lagrange(xi, fxi, xTanya, i+1)))
    if(i == 1):
        continue
    else:
        print('Nilai EA dibandingkan Orde sebelumnya : ',
              dapetEa(lagrange(xi, fxi, xTanya, i-1), lagrange(xi, fxi, xTanya, i)), '%')
        print()
