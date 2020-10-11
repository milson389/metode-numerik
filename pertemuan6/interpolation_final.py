# Audie Milson(535180021)
# Interpolasi Newton
import numpy as np


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

    return jumlah


x = [10.5, 12, 12.4, 12.8]
fx = [45.2, 58.1, 60.2, 64.4]
xTanya = 11.5
fTrue = 55.92
print('\nNewton Divided Difference Interpolation\n---------------------------------------')
print('\nPrediksi Hasil Promosi :')
for i in range(1, 4):
    print('\nOrde ', i)
    print("Hasil : ", "{:.4f}".format(newtonInterpolation(x, fx, xTanya, i)))
    if(i == 1):
        continue
    else:
        print("ET (55.92) : ", errorTrue(
            fTrue, newtonInterpolation(x, fx, xTanya, i)), '%')
        print("EA : ", dapetEa(newtonInterpolation(x, fx, xTanya, i-1),
                               newtonInterpolation(x, fx, xTanya, i)), '%')


v = [6, 8, 9, 10]
fv = [5.39, 5.06, 4.94, 4.85]
vTanya = 7

print('\nPrediksi Nilai Tabel Distribusi F v1=7, v2=10 :')
for i in range(1, 4):
    print('\nOrde ', i)
    print("Hasil : ", "{:.4f}".format(newtonInterpolation(v, fv, vTanya, i)))
    if(i == 1):
        continue
    else:
        print("EA : ", dapetEa(newtonInterpolation(v, fv, vTanya, i-1),
                               newtonInterpolation(v, fv, vTanya, i)), '%')


# Metode Lagrange
xi = [6, 8, 9, 10]
fxi = [5.39, 5.06, 4.94, 4.85]

xTanya = 7


def lagRange(x, fx, xTanya, orde):
    result = 0
    interpolasi = int(orde)+1
    for i in range(interpolasi):
        l = 1
        for j in range(interpolasi):
            if(j != i):
                l *= (xTanya-xi[j])/(xi[i]-xi[j])
        result += l*fxi[i]
    return result


hasilLR1 = lagRange(xi, fxi, xTanya, 1)
hasilLR2 = lagRange(xi, fxi, xTanya, 2)
hasilLR3 = lagRange(xi, fxi, xTanya, 3)

print('\nLagrange Method\n----------------')
print("\nPrediksi nilai tabel distribusi f dengan v1 = 7 v2 = 10\n")
for i in range(1, 4):
    print("\nHasil Perhitungan Orde", i,
          ": " "{:.4f}".format(lagRange(xi, fxi, xTanya, i)))
    if(i == 1):
        continue
    else:
        print('Nilai EA dibandingkan Orde sebelumnya : ',
              dapetEa(lagRange(xi, fxi, xTanya, i-1), lagRange(xi, fxi, xTanya, i)), '%')
        print()
