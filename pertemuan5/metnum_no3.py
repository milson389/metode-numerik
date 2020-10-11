# -*- coding: utf-8 -*-
"""Metnum_No3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hkuugPj8Do1Y8Eh0W9NThE2eym4jG4oO
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.misc import derivative
from prettytable import PrettyTable

e = math.exp(1)


def func(x):
    return x**2.5+0.5*(x**0.5)-0.6


def turunanFunc(x):
    a = x
    x = sp.Symbol('x')
    rumusFungsi = x**2.5+0.5*(x**0.5)-0.6
    f = (sp.diff(rumusFungsi, x))
    hasil = sp.lambdify(x, f)
    return hasil(a)


def dapetXr(a, b):
    return (a+b)/2


def dapetXrInterpolasi(a, b):
    return b - (func(b)*(a-b)) / (func(a)-func(b))


def nilaiX(x):
    # a = xi, b = turunan xi
    a = func(x)
    b = turunanFunc(x)
    nextXi = x - (a/b)
    return nextXi


def nextX(prev, curr):
    return curr - (func(curr)*(curr-prev))/(func(curr)-func(prev))


iterasi = 0
listIterasi = []
listXr = []
listError = []

def bisectionMethod():
    global iterasi
    print('\nBisection Method \n----------------')
    xi = float(input('Masukkan nilai tebakan Awal Xi : '))
    xu = float(input('Masukkan nilai tebakan kedua Xu : '))
    es = int(input('Masukkan nilai toleransi kesalahan yang diinginkan : '))
    ea = 100

    while(ea > es):
        iterasi += 1
        print('\niterasi ke ', iterasi)
        xr = dapetXr(xi, xu)
        print('nilai xr : ', xr)

        if(iterasi > 1):
            ea = abs((xr-prevXr)/xr)*100
            print('tingkat error (ea) : ', ea, '%')

        listIterasi.append(iterasi)
        listXr.append(xr)
        listError.append(ea)

        if(func(xi)*func(xr) < 0):
            xu = xr
        elif (func(xi)*func(xr) > 0):
            xi = xr
        else:
            break

        prevXr = xr
        print()


bisectionMethod()
bM = PrettyTable()
bM.field_names = ["Iterasi", "Nilai Xr", "Tingkat Error(ea %)"]

for i in range(len(listIterasi)):
    bM.add_row([listIterasi[i], "{:.4f}".format(
        listXr[i]), "{:.4f} %".format(listError[i])])

print(bM)

plt.plot(listIterasi, listError, 'r-o')
plt.title('Bisection Method')
plt.ylabel('Error (%)')
plt.xlabel('Iterasi')
plt.show()

import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.misc import derivative
from prettytable import PrettyTable

e = math.exp(1)


def func(x):
    return x**2.5+0.5*(x**0.5)-0.6


def turunanFunc(x):
    a = x
    x = sp.Symbol('x')
    rumusFungsi = x**2.5+0.5*(x**0.5)-0.6
    f = (sp.diff(rumusFungsi, x))
    hasil = sp.lambdify(x, f)
    return hasil(a)


def dapetXr(a, b):
    return (a+b)/2


def dapetXrInterpolasi(a, b):
    return b - (func(b)*(a-b)) / (func(a)-func(b))


def nilaiX(x):
    # a = xi, b = turunan xi
    a = func(x)
    b = turunanFunc(x)
    nextXi = x - (a/b)
    return nextXi


def nextX(prev, curr):
    return curr - (func(curr)*(curr-prev))/(func(curr)-func(prev))



iterate = 0
listIterate = []
listXrReg = []
listErrorReg = []


def interpolasiLinier():
    global iterate
    print('\nInterpolasi Linier \n----------------')
    xi = float(input('Masukkan nilai tebakan Awal Xi : '))
    xu = float(input('Masukkan nilai tebakan kedua Xu : '))
    es = int(input('Masukkan nilai toleransi kesalahan yang diinginkan : '))
    ea = 100

    while(ea > es):
        iterate += 1
        print('\niterasi ke ', iterate)
        xr = dapetXrInterpolasi(xi, xu)
        print('nilai xr : ', xr)

        if(iterate > 1):
            ea = abs((xr-prevXr)/xr)*100
            print('tingkat error (ea) : ', ea, '%')

        listIterate.append(iterate)
        listXrReg.append(xr)
        listErrorReg.append(ea)

        if(func(xi)*func(xr) < 0):
            xu = xr
        elif (func(xi)*func(xr) > 0):
            xi = xr
        else:
            break

        prevXr = xr
        print()


interpolasiLinier()
iL = PrettyTable()
iL.field_names = ["Iterasi", "Nilai Xr", "Tingkat Error(ea %)"]

for j in range(len(listIterate)):
    iL.add_row([listIterate[j], "{:.4f}".format(
        listXrReg[j]), "{:.4f}".format(listErrorReg[j])])

print(iL)

plt.plot(listIterate, listErrorReg, 'g-o')
plt.title('Interpolasi Linier')
plt.ylabel('Error (%)')
plt.xlabel('Iterasi')
plt.xticks(listIterate)
plt.show()

import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.misc import derivative
from prettytable import PrettyTable

e = math.exp(1)


def func(x):
    return x**2.5+0.5*(x**0.5)-0.6


def turunanFunc(x):
    a = x
    x = sp.Symbol('x')
    rumusFungsi = x**2.5+0.5*(x**0.5)-0.6
    f = (sp.diff(rumusFungsi, x))
    hasil = sp.lambdify(x, f)
    return hasil(a)


def dapetXr(a, b):
    return (a+b)/2


def dapetXrInterpolasi(a, b):
    return b - (func(b)*(a-b)) / (func(a)-func(b))


def nilaiX(x):
    # a = xi, b = turunan xi
    a = func(x)
    b = turunanFunc(x)
    nextXi = x - (a/b)
    return nextXi


def nextX(prev, curr):
    return curr - (func(curr)*(curr-prev))/(func(curr)-func(prev))


iteraNewton = 1
listIteraNewton = []
listXiNewton = []
listXiCurrNew = []
listErrorNew = [100]


def newtonRhaphson():
    global iteraNewton
    print("\nNewton Rhapson \n--------------")
    xi = float(input('Masukkan nilai tebakan awal Xi : '))
    es = int(input('Masukkan % tingkat toleransi error es : '))
    ea = 100
    nextX = nilaiX(xi)
    print()
    print("Iterasi ke", iteraNewton)
    print("Xi =", xi)
    print('Xi+1 =', nextX)
    print()
    listIteraNewton.append(iteraNewton)
    listXiNewton.append(nextX)
    listXiCurrNew.append(xi)

    while(ea > es):
        xi = nextX
        nextX = nilaiX(xi)
        print()
        print("Iterasi ke", iteraNewton+1)
        print("Xi =", xi)
        print('Xi+1 =', nextX)
        ea = abs((nextX-xi)/nextX)*100
        print('nilai error : ', ea, '%')
        print()
        iteraNewton += 1
        listIteraNewton.append(iteraNewton)
        listErrorNew.append(ea)
        listXiNewton.append(nextX)
        listXiCurrNew.append(xi)


newtonRhaphson()
nR = PrettyTable()
nR.field_names = ["Iterasi", "Nilai Xi", "Nilai Xi+1", "Tingkat Error(ea %)"]

for k in range(len(listIteraNewton)):
    nR.add_row([listIteraNewton[k], "{:.4f}".format(listXiCurrNew[k]), "{:.4f}".format(
        listXiNewton[k]), "{:.4f}".format(listErrorNew[k])])

print(nR)

plt.plot(listIteraNewton, listErrorNew, 'b-o')
plt.title('Newton Rhapson')
plt.ylabel('Error (%)')
plt.xlabel('Iterasi')
plt.xticks(listIteraNewton)
plt.show()

import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.misc import derivative
from prettytable import PrettyTable

e = math.exp(1)


def func(x):
    return x**2.5+0.5*(x**0.5)-0.6


def turunanFunc(x):
    a = x
    x = sp.Symbol('x')
    rumusFungsi = x**2.5+0.5*(x**0.5)-0.6
    f = (sp.diff(rumusFungsi, x))
    hasil = sp.lambdify(x, f)
    return hasil(a)


def dapetXr(a, b):
    return (a+b)/2


def dapetXrInterpolasi(a, b):
    return b - (func(b)*(a-b)) / (func(a)-func(b))


def nilaiX(x):
    # a = xi, b = turunan xi
    a = func(x)
    b = turunanFunc(x)
    nextXi = x - (a/b)
    return nextXi


def nextX(prev, curr):
    return curr - (func(curr)*(curr-prev))/(func(curr)-func(prev))


iteraSecant = 1
listIteraSecant = []
listXiSecant = []
listXiPrevSecant = []
listXiCurrSecant = []
listErrorSecant = [100]


def secantMethod():
    print('Secant Method \n-------------')
    global iteraSecant
    previousX = float(input('Masukkan nilai Xi-1 : '))
    currentX = float(input('Masukkan nilai Xi : '))
    es = int(input('Masukkan % tingkat toleransi kesalahan yang diinginkan : '))
    ea = 100
    theNextX = nextX(previousX, currentX)
    print()
    print('Iterasi ke ', iteraSecant)
    print('nilai : ', theNextX)
    print('Nilai Xi : ', currentX)
    print('Nilai prev Xi : ', previousX)
    print('tingkat error (ea) : ')
    print()
    listIteraSecant.append(iteraSecant)
    listXiSecant.append(theNextX)
    listXiCurrSecant.append(currentX)
    listXiPrevSecant.append(previousX)

    while(ea > es):
        previousX = currentX
        currentX = theNextX
        theNextX = nextX(previousX, currentX)
        ea = abs(((theNextX - currentX)/theNextX))*100
        print()
        print('Iterasi ke ', iteraSecant+1)
        print('nilai : ', theNextX)
        print('Nilai Xi : ', currentX)
        print('Nilai prev Xi : ', previousX)
        print('tingkat error (ea) : ', ea, '%')
        print()
        iteraSecant += 1
        listIteraSecant.append(iteraSecant)
        listXiSecant.append(theNextX)
        listErrorSecant.append(ea)
        listXiCurrSecant.append(currentX)
        listXiPrevSecant.append(previousX)


secantMethod()
sM = PrettyTable()
sM.field_names = ["Iterasi", "Nilai Xi-1",
                  "Nilai Xi", "Nilai Xi+1", "Tingkat Error(ea %)"]

for l in range(len(listIteraSecant)):
    sM.add_row([listIteraSecant[l], "{:.4f}".format(listXiPrevSecant[l]), "{:.4f}".format(
        listXiCurrSecant[l]), "{:.4f}".format(listXiSecant[l]), "{:.4f}".format(listErrorSecant[l])])

print(sM)

plt.plot(listIteraSecant, listErrorSecant, 'y-o')
plt.title('Secant Method')
plt.ylabel('Error (%)')
plt.xlabel('Iterasi')
plt.xticks(listIteraSecant)
plt.show()