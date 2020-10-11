import math
import numpy as np
import matplotlib.pyplot as pyplot
from prettytable import PrettyTable


def func(x):
    return (x**4)+(2.8*x**3)-(0.38*x**2)-(6.3*x)-4.2
    # return (x**3) + (4*x**2)-10
    # return (x**3)-(13*x)-12


def jarak(x1, x):
    # x1 = nilai titik tebakan ke 2
    # x = nilai titik tebakan pertama
    fx1 = func(x1)
    fx = func(x)
    return (fx1-fx)/(x1-x)


def diskriminan(a, b, c):
    return math.sqrt((b**2)-(4*a*c))


iterasi = 0
listX0 = []
listX1 = []
listX2 = []
listX3 = []
listError = []


def mullerMethod():
    global iterasi
    print("\nAlgoritma Muller\n----------------")
    # Algoritma Muller 3 titik hampiran awal
    x0 = float(input('Masukkan tebakan awal pertama : '))
    x1 = float(input('Masukkan tebakan awal kedua : '))
    x2 = float(input('Masukkan tebakan awal ketiga : '))
    es = float(input('Masukkan presentase toleransi error : '))
    ea = 100
    ho = 0
    h1 = 0
    nilaiX3 = 0
    listX0.append(x0)
    listX1.append(x1)
    listX2.append(x2)

    while(ea > es):
        # Mencari fungsi nilai fungsi tebakan awal
        fx0 = func(x0)
        fx1 = func(x1)
        fx2 = func(x2)
        # menghitung h- dan h1
        h0 = x1-x0
        h1 = x2-x1
        # menghitung jarak
        jarak1 = jarak(x1, x0)
        jarak2 = jarak(x2, x1)
        # menghitung nilai koefisien - koefisien dalam rumus kuadratis
        a = (jarak2-jarak1)/(h1+h0)
        b = (a*h1) + jarak2
        c = fx2
        # menghitung diskriminan
        d = diskriminan(a, b, c)
        addBD = b + d
        subBD = b-d
        if(abs(addBD) > abs(subBD)):
            nilaiX3 = x2 + ((-2*c)/addBD)
        elif(abs(addBD) < abs(subBD)):
            nilaiX3 = x2 + ((-2*c)/subBD)
        ea = abs((nilaiX3-x2)/nilaiX3)*100
        iterasi += 1
        print('iterasi : ', iterasi)
        print('Ea : ', "{:.5f}".format(ea))
        listX0.append(x0)
        listX1.append(x1)
        listX2.append(x2)
        listX3.append(nilaiX3)
        listError.append(ea)
        x0 = x1
        x1 = x2
        x2 = nilaiX3


mullerMethod()
mM = PrettyTable()
mM.field_names = ["iterasi", "x0", "x1", "x2", "nilai X", "Error (%)"]

for i in range(iterasi):
    mM.add_row([i+1, "{:.5f}".format(listX0[i]), "{:.5f}".format(listX1[i]), "{:.5f}".format(
        listX2[i]), "{:.5f}".format(listX3[i]), "{:.5f}".format(listError[i])])

print(mM)
