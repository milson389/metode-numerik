# Audie Milson ( 535180021 )
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.misc import derivative
from prettytable import PrettyTable

e = math.exp(1)


def func(x):
    return 3*x + math.sin(x) - math.exp(x)


def turunanFunc(x):
    return math.cos(x)-(e**x)+3


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
iterate = 0
iteraNewton = 1
iteraSecant = 1

listIterasi = []
listIterate = []
listIteraNewton = []
listIteraSecant = []

listXr = []
listXrReg = []
# Newton
listXiNewton = []
listXiCurrNew = []

# Secant
listXiSecant = []
listXiPrevSecant = []
listXiCurrSecant = []


listError = []
listErrorReg = []
listErrorNew = [100]
listErrorSecant = [100]


def bisectionMethod():
    global iterasi
    print('\nBisection Method \n----------------')
    xi = 0
    xu = 1.5
    es = 0.01
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


def interpolasiLinier():
    global iterate
    print('\nInterpolasi Linier \n----------------')
    xi = 0.0
    xu = 1.5
    es = 0.01
    ea = 100

    while(ea > es):
        iterate += 1
        print('\niterasi ke ', iterate)
        xr = dapetXrInterpolasi(xi, xu)
        print('nilai xr : ', xr)

        if(iterate > 1):
            ea = abs((xr-prevXr)/xr)*100
            print('tingkat error (ea) : ', "{:.4f}".format(ea), '%')

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


def newtonRhaphson():
    global iteraNewton
    print("\nNewton Rhapson \n--------------")
    xi = 0.0
    es = 0.01
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
        xi = round(nextX, 5)
        nextX = round(nilaiX(xi), 5)
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


def secantMethod():
    print('Secant Method \n-------------')
    global iteraSecant
    previousX = 0.0
    currentX = 0.2
    es = 0.01
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
        print('tingkat error (ea) : ', "{:.4f}".format(ea), '%')
        print()
        iteraSecant += 1
        listIteraSecant.append(iteraSecant)
        listXiSecant.append(theNextX)
        listErrorSecant.append(ea)
        listXiCurrSecant.append(currentX)
        listXiPrevSecant.append(previousX)


bisectionMethod()
interpolasiLinier()
newtonRhaphson()
secantMethod()

plt.subplot(211)
plt.title('Akar persamaan f(x) = 3x + sin(x) - exp(x)')
plt.yticks([0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
plt.plot(listIterasi, listXr, 'b-o', listIterate,
         listXrReg, 'y-o', listIteraSecant, listXiSecant, 'r-o')
plt.legend(['Biseksi', 'Regulafalsi', 'Secant'])

plt.subplot(212)
plt.plot(listIterasi, listError, 'b-o', listIterate, listErrorReg,
         'y-o', listIteraSecant, listErrorSecant, 'r-o')
plt.yticks([0, 20, 40, 60, 80, 100])
plt.legend(['Biseksi', 'Regulafalsi', 'Secant'])
plt.tight_layout()
plt.show()
