# Audie Milson (535180021)
# Owen (535180016)
# James Anderson (535180027)
# Michael Joses D. (535180037)
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.misc import derivative

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


iterasi = 1
iterate = 1
iteraNewton = 1
iteraSecant = 1

listIterasi = []
listIterate = []
listIteraNewton = []
listIteraSecant = []

listXr = []
listXrReg = []
listXiNewton = []
listXiSecant = []

listError = [100]
listErrorReg = [100]
listErrorNew = [100]
listErrorSecant = [100]


def bisectionMethod():
    global iterasi
    print('\nBisection Method \n----------------')
    xi = float(input('Masukkan nilai tebakan Awal Xi : '))
    xu = float(input('Masukkan nilai tebakan kedua Xu : '))
    es = int(input('Masukkan nilai toleransi kesalahan yang diinginkan : '))
    ea = 100
    xr = dapetXr(xi, xu)
    print()
    print('iterasi ke ', iterasi)
    print('nilai xr: ', xr)
    print('tingkat error (ea) : ')
    print()
    listXr.append(xr)
    listIterasi.append(iterasi)
    while(ea > es):
        prevXr = xr
        # Evaluasi
        if(func(xi)*func(xr) < 0):
            xu = xr
        elif (func(xi)*func(xr) > 0):
            xi = xr
        else:
            xr = xr

        xr = dapetXr(xi, xu)
        ea = abs(((xr - prevXr)/xr))*100
        print('iterasi ke ', iterasi+1)
        print('nilai xr: ', xr)
        print('tingkat error (ea) : ', ea, '%')
        print()
        iterasi += 1
        listIterasi.append(iterasi)
        listXr.append(xr)
        listError.append(ea)


def interpolasiLinier():
    global iterate
    print('Interpolasi Linier \n------------------')
    xi = float(input('Masukkan nilai tebakan Awal Xi : '))
    xu = float(input('Masukkan nilai tebakan kedua Xu : '))
    es = int(input('Masukkan nilai toleransi kesalahan yang diinginkan : '))
    ea = 100
    xr = dapetXrInterpolasi(xi, xu)
    print()
    print('iterasi ke ', iterate)
    print('nilai xr: ', xr)
    print('tingkat error (ea) : ')
    print()
    listXrReg.append(xr)
    listIterate.append(iterate)
    while(ea >= es):
        prevXr = xr
        # Evaluasi
        if(func(xi)*func(xr) < 0):
            xu = xr
        elif (func(xi)*func(xr) > 0):
            xi = xr
        else:
            xr = xr
            break

        xr = dapetXrInterpolasi(xi, xu)
        ea = abs(((xr - prevXr)/xr))*100
        print('iterasi ke ', iterate+1)
        print('nilai xr: ', xr)
        print('tingkat error (ea) : ', ea, '%')
        print()
        iterate += 1
        listIterate.append(iterate)
        listXrReg.append(xr)
        listErrorReg.append(ea)


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
    listXiNewton.append(nextX)
    listIteraNewton.append(iteraNewton)
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
    listXiSecant.append(theNextX)
    listIteraSecant.append(iteraSecant)

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


bisectionMethod()
interpolasiLinier()
newtonRhaphson()
secantMethod()

plt.plot(listIterasi, listError, 'r-o')
plt.title('Bisection Method')
plt.ylabel('Error (%)')
plt.xlabel('Iterasi')
plt.xticks(listIterasi)
plt.show()

plt.plot(listIterate, listErrorReg, 'g-o')
plt.title('Interpolasi Linier')
plt.ylabel('Error (%)')
plt.xlabel('Iterasi')
plt.xticks(listIterate)
plt.show()

plt.plot(listIteraNewton, listErrorNew, 'b-o')
plt.title('Newton Rhapson')
plt.ylabel('Error (%)')
plt.xlabel('Iterasi')
plt.xticks(listIteraNewton)
plt.show()

plt.plot(listIteraSecant, listErrorSecant, 'y-o')
plt.title('Secant Method')
plt.ylabel('Error (%)')
plt.xlabel('Iterasi')
plt.xticks(listIteraSecant)
plt.show()
