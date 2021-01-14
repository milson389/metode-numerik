# Audie Milson ( 535180021 )
import math
import numpy as np
import matplotlib.pyplot as plt


e = math.exp(1)


def func(x):
    return 0.5*x*(e**x**0.5)-2


def dapetXr(a, b):
    return (a+b)/2


xi = 1
xu = 2
xr = dapetXr(xi, xu)
es = 0.01
ea = 1
hasil = xi
iterasi = 1
listIterasi = [1]
listXr = [xr]
listError = [100]

print('iterasi ke ', iterasi)
print('nilai xr: ', xr)
print('tingkat error(ea) : ')
print()

while(ea >= es):

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


# Plot 1
plt.subplot(211)
plt.plot(listIterasi, listXr, 'b-o')
plt.title(r'Akar persamaan $f(x) =\frac{1}{2} x e^{x^{\frac{1}{2}}} -2$')
plt.ylabel('Xr')
plt.yticks([1.3, 1.4, 1.5])

# Plot 2
plt.subplot(212)
plt.plot(listIterasi, listError, 'r--o')
plt.ylabel('Error (%)')
plt.xlabel('Iterasi')
plt.yticks([0, 50, 100])
plt.show()
