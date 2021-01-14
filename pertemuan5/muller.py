import math
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable


def func(x):
    return x**3-x-1
    # return (x**4)+(2.8*x**3)-(0.38*x**2)-(6.3*x)-4.2
    # return (x**3) + (4*x**2)-10
    # return (x**3)-(13*x)-12


def jarak(kedua, pertama):
    # x1 = nilai titik tebakan ke 2
    # x = nilai titik tebakan pertama
    fx1 = func(kedua)
    fx = func(pertama)
    return (fx1-fx)/(kedua-pertama)


def diskriminan(a, b, c):
    return math.sqrt((b**2)-(4*a*c))


def mullerMethod(tebakan1, tebakan2, tebakan3, error, tabel, daftarX3, daftarError):
    iterasi = 0
    print("\nAlgoritma Muller\n----------------")
    # Algoritma Muller 3 titik hampiran awal
    x0 = float(tebakan1)
    x1 = float(tebakan2)
    x2 = float(tebakan3)
    es = float(error)
    ea = 100
    ho = 0
    h1 = 0
    nilaiX3 = 0

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
        daftarX3.append(nilaiX3)
        daftarError.append(ea)
        iterasi += 1
        print('iterasi : ', iterasi)
        print('Ea : ', "{:.5f}".format(ea))
        tabel.add_row([iterasi, "{:.5f}".format(x0), "{:.5f}".format(x1), "{:.5f}".format(
            x2), h0, h1, jarak1, jarak2, a, b, c, d, "{:.5f}".format(nilaiX3), "{:.5f}".format(ea)])
        x0 = x1
        x1 = x2
        x2 = nilaiX3


t1 = -0.5
t2 = 1
t3 = 0.5
es = 0.01
mM = PrettyTable()
listX3_1 = []
listError_1 = []
mM.field_names = ["iterasi", "x0", "x1", "x2", "ho", "h1", "jarak1", "jarak2",
                  "a", "b", "c", "diskriminan", "nilai X", "Error (%)"]
mullerMethod(t1, t2, t3, es, mM, listX3_1, listError_1)
print(mM)

sumbuX = np.arange(1, len(listError_1)+1)
plt.subplot(211)
plt.title('Metode Muller')
plt.plot(sumbuX, listError_1, 'b-o')
plt.xticks(sumbuX)
plt.xlabel('Iterasi')
plt.ylabel('Error (%)')
plt.grid()

plt.subplot(212)
plt.plot(sumbuX, listX3_1, 'r-o')
plt.xticks(sumbuX)
plt.xlabel('Iterasi')
plt.ylabel('Nilai X')
plt.grid()
plt.tight_layout()
plt.show()

# q1 = 1
# q2 = 2
# q3 = 1.5
# es = 0.02
# mM1 = PrettyTable()
# listX3_2 = []
# listError_2 = []
# mM1.field_names = ["iterasi", "x0", "x1", "x2",
#                    "a", "b", "c", "diskriminan", "nilai X", "Error (%)"]
# mullerMethod(q1, q2, q3, es, mM1, listX3_2, listError_2)
# print(mM1)

# sumbuX = np.arange(1, len(listError_2)+1)
# plt.subplot(211)
# plt.title('Metode Muller (1)')
# plt.plot(sumbuX, listError_2, 'b-o')
# plt.xticks(sumbuX)
# plt.xlabel('Iterasi')
# plt.ylabel('Error (%)')
# plt.grid()

# plt.subplot(212)
# plt.plot(sumbuX, listX3_2, 'r-o')
# plt.xticks(sumbuX)
# plt.xlabel('Iterasi')
# plt.ylabel('Nilai X')
# plt.grid()
# plt.tight_layout()
# plt.show()

# q1 = -1.5
# q2 = 0
# q3 = 1.5
# es = 0.01
# mM2 = PrettyTable()
# listX3_3 = []
# listError_3 = []
# mM2.field_names = ["iterasi", "x0", "x1", "x2",
#                    "a", "b", "c", "diskriminan", "nilai X", "Error (%)"]
# mullerMethod(q1, q2, q3, es, mM2, listX3_3, listError_3)
# print(mM2)

# sumbuX = np.arange(1, len(listError_3)+1)
# plt.subplot(211)
# plt.title('Metode Muller (2)')
# plt.plot(sumbuX, listError_3, 'b-o')
# plt.xticks(sumbuX)
# plt.xlabel('Iterasi')
# plt.ylabel('Error (%)')
# plt.grid()

# plt.subplot(212)
# plt.plot(sumbuX, listX3_3, 'r-o')
# plt.xticks(sumbuX)
# plt.xlabel('Iterasi')
# plt.ylabel('Nilai X')
# plt.grid()
# plt.tight_layout()
# plt.show()
