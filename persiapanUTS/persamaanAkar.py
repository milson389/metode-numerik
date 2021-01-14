# Audie Milson (535180021)
# Owen (535180016)
# James Anderson (535180027)
# Michael Joses D. (535180037)
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.misc import derivative
from prettytable import PrettyTable

e = math.exp(1)
# 'Akar persamaan $f(x) =x^\frac{5}{2} + \frac{1}{2}x^\frac{1}{2} -0.6$'


def func(x):
    # return x**2.5+0.5*(x**0.5)-0.6
    return 3*x + math.sin(x) - math.exp(x)


def turunanFunc(x):
    # a = x
    # x = sp.Symbol('x')
    # rumusFungsi = x**2.5+0.5*(x**0.5)-0.6
    # f = (sp.diff(rumusFungsi, x))
    # hasil = sp.lambdify(x, f)
    # return hasil(a)
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


def bisectionMethod(tebakan1, tebakan2, toleransiE):
    iterasi = 0
    print('\nBisection Method \n----------------')
    xi = float(tebakan1)
    xu = float(tebakan2)
    es = float(toleransiE)
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


def interpolasiLinier(tebakan1, tebakan2, toleransiE):
    iterate = 0
    print('\nInterpolasi Linier \n----------------')
    xi = float(tebakan1)
    xu = float(tebakan2)
    es = float(toleransiE)
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


def newtonRhaphson(tebakanAwal, toleransiEr):
    global iteraNewton
    print("\nNewton Rhapson \n--------------")
    xi = float(tebakanAwal)
    es = float(toleransiEr)
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


def secantMethod(nilaiPrev, nilaiCurr, nilaiEr):
    print('Secant Method \n-------------')
    global iteraSecant
    previousX = float(nilaiPrev)
    currentX = float(nilaiCurr)
    es = float(nilaiEr)
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


tebakan1 = 0
tebakan2 = 1.5
tebakanSecant = 0.2
es = 0.01

bisectionMethod(tebakan1, tebakan2, es)
bM = PrettyTable()
bM.field_names = ["Iterasi", "Nilai Xr", "Tingkat Error(ea %)"]

for i in range(len(listIterasi)):
    bM.add_row([listIterasi[i], "{:.4f}".format(
        listXr[i]), "{:.4f}".format(listError[i])])

print(bM)


interpolasiLinier(tebakan1, tebakan2, es)
iL = PrettyTable()
iL.field_names = ["Iterasi", "Nilai Xr", "Tingkat Error(ea %)"]

for j in range(len(listIterate)):
    iL.add_row([listIterate[j], "{:.4f}".format(
        listXrReg[j]), "{:.4f}".format(listErrorReg[j])])

print(iL)


newtonRhaphson(tebakan1, es)
nR = PrettyTable()
nR.field_names = ["Iterasi", "Nilai Xi", "Nilai Xi+1", "Tingkat Error(ea %)"]

for k in range(len(listIteraNewton)):
    nR.add_row([listIteraNewton[k], "{:.4f}".format(listXiCurrNew[k]), "{:.4f}".format(
        listXiNewton[k]), "{:.4f}".format(listErrorNew[k])])

print(nR)


secantMethod(tebakan1, tebakanSecant, es)
sM = PrettyTable()
sM.field_names = ["Iterasi", "Nilai Xi-1",
                  "Nilai Xi", "Nilai Xi+1", "Tingkat Error(ea %)"]

for l in range(len(listIteraSecant)):
    sM.add_row([listIteraSecant[l], "{:.4f}".format(listXiPrevSecant[l]), "{:.4f}".format(
        listXiCurrSecant[l]), "{:.4f}".format(listXiSecant[l]), "{:.4f}".format(listErrorSecant[l])])

print(sM)


# plt.subplot(221)
# plt.plot(listIterasi, listError, 'r-o')
# plt.title('Bisection Method')
# plt.ylabel('Error (%)')
# plt.xlabel('Iterasi')

# plt.subplot(222)
# plt.plot(listIterate, listErrorReg, 'g-o')
# plt.title('Interpolasi Linier')
# plt.ylabel('Error (%)')
# plt.xlabel('Iterasi')
# plt.xticks(listIterate)

# plt.subplot(223)
# plt.plot(listIteraNewton, listErrorNew, 'b-o')
# plt.title('Newton Rhapson')
# plt.ylabel('Error (%)')
# plt.xlabel('Iterasi')
# plt.xticks(listIteraNewton)

# plt.subplot(224)
# plt.plot(listIteraSecant, listErrorSecant, 'y-o')
# plt.title('Secant Method')
# plt.ylabel('Error (%)')
# plt.xlabel('Iterasi')
# plt.xticks(listIteraSecant)

plt.subplot(211)
plt.title('Akar persamaan f(x) = 3x + sin(x) - exp(x)')
plt.yticks([0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
plt.plot(listIterasi, listXr, 'b-o', listIterate,
         listXrReg, 'y-o', listIteraNewton, listXiNewton, 'g-o', listIteraSecant, listXiSecant, 'r-o')
plt.legend(['Biseksi', 'Regulafalsi', 'Newton Raphson', 'Secant'])

plt.subplot(212)
plt.plot(listIterasi, listError, 'b-o', listIterate, listErrorReg,
         'y-o', listIteraNewton, listErrorNew, 'g-o', listIteraSecant, listErrorSecant, 'r-o')
plt.yticks([0, 20, 40, 60, 80, 100])
plt.legend(['Biseksi', 'Regulafalsi', 'Newton Raphson', 'Secant'])

plt.tight_layout()
plt.show()
