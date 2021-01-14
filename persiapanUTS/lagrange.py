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


def lagrange(afa, aTanya, orde):
    result = 0
    list = []
    xn = []
    interpolasi = int(orde)+1
    for i in range(interpolasi):
        l = 1
        for j in range(interpolasi):
            if(j != i):
                l *= (aTanya-afa[j][0])/(afa[i][0]-afa[j][0])
        list.append(l)
        xn.append(afa[i][0])
        result += l*afa[i][1]
    lr.add_row([i, xn, list, result])
    return result


# lagRange(xi, fxi, xiTanya, 3)
# xi = [6.509, 8.0814, 3.9090, 6.1082, 9.9294,
#       9.9629, 2.2558, 3.0724, 1.5146, 5.4081]
# fxi = [16.41, 16.6266, 15.9, 16.3467, 16.8325,
#        16.8359, 15.3505, 15.6594, 14.9522, 16.2245]
xi = [
    [6.509, 16.41], [8.0814, 16.6266], [3.9090, 15.9], [6.1082, 16.3467], [9.9294, 16.8325], [
        9.9629, 16.8359], [2.2558, 15.3505], [3.0724, 15.6594], [1.5146, 14.9522], [5.4081, 16.2245]
]

xTanya = 7.3
xTanya1 = 5.0

matrix = []
for i in range(len(xi)):
    matrix = sorted(xi)


lr = PrettyTable()
lr.field_names = ['Orde', 'Xn', 'Li', 'Fx(i)']

print()
orde = int(input('Masukkan Nilai N ( Orde ke -N ) untuk f(x=7.3) : '))
print("\nHasil Perhitungan Orde", orde, ": ",
      "{:.4f}".format(lagrange(matrix, xTanya, orde)))
lr.clear_rows()

for i in range(1, orde+1):
    lagrange(matrix, xTanya, i)
print(lr)
lr.clear_rows()
