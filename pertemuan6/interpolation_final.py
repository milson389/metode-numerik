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
def lagrange(f: list, xi: float, n: int) -> float:
    result = 0
    orde = n+1
    for i in range(orde):
        term = f[i][1]
        for j in range(orde):
            if j != i:
                term *= (xi - f[j][0]) / (f[i][0] - f[j][0])
                list.append(term/f[i][1])
        result += term

    return result


f = [[10.5, 45.2], [12, 58.1], [12.4, 60.2], [12.8, 64.4]]
xTanya = 11.5
list = []

a = [[6, 5.39], [8, 5.06], [9, 4.94], [10, 4.85]]
aTanya = 7

# lagrange(f, xTanya, 3)
# print(list)


print('\nLagrange Method\n----------------')
print("\nPrediksi nilai tabel distribusi f dengan v1 = 7 v2 = 10\n")
for i in range(1, 4):
    print("\nHasil Perhitungan Orde", i,
          ": " "{:.4f}".format(lagrange(f, xTanya, i)))
    if(i == 1):
        continue
    else:
        print('Nilai EA dibandingkan Orde sebelumnya : ',
              dapetEa(lagrange(f, xTanya, i-1), lagrange(f, xTanya, i)), '%')
        print()


print('\nLagrange Method\n----------------')
print("\nPrediksi nilai tabel distribusi f dengan v1 = 7 v2 = 10\n")
for i in range(1, 4):
    print("\nHasil Perhitungan Orde", i,
          ": " "{:.4f}".format(lagrange(a, aTanya, i)))
    if(i == 1):
        continue
    else:
        print('Nilai EA dibandingkan Orde sebelumnya : ',
              dapetEa(lagrange(a, aTanya, i-1), lagrange(a, aTanya, i)), '%')
        print()
