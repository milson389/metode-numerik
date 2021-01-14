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


lr = PrettyTable()
lr.field_names = ['Orde', 'Xn', 'Li', 'Fx(i)']

xi = [[1, 8.1], [5, 4.1], [7, 3.7], [8, 3.56], [9, 3.46], [10, 3.37]]

xTanya = 7.3
xTanya1 = 5.0

matrix = []
for i in range(len(xi)):
    matrix = sorted(xi)


lr = PrettyTable()
lr.field_names = ['Orde', 'Xn', 'Li', 'Fx(i)']

print()
orde = 4
print("\nHasil Perhitungan Orde", orde, ": ",
      "{:.4f}".format(lagrange(matrix, xTanya, orde)))
lr.clear_rows()

for i in range(1, orde+1):
    lagrange(matrix, xTanya, i)
print(lr)
lr.clear_rows()
