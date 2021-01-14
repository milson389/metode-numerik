import math


def func(x, y):
    return (0.5*x**3) + 3


def func1(x, y):
    return y * x - y


def func2(x, y):
    return (x+y-2)


def euler(f, xAwal, yAwal, stepSize, xTarget, yEksak):
    temp = 0
    index = 0
    ea = 100
    while (xAwal < xTarget):
        print('X : ', xAwal)
        print('Y Euler : ', yAwal)
        if (index > 0):
            ea = abs((yEksak[index] - yAwal) / yEksak[index]) * 100
            print('EA : ', ea, '%')
        print()
        temp = yAwal
        yAwal += stepSize * f(xAwal, yAwal)
        xAwal += stepSize
        index += 1
        ea = abs((yEksak[index] - yAwal) / yEksak[index]) * 100

    print('X : ', xAwal)
    print('Y Euler : ', yAwal)
    print('EA : ', ea, '%')
    print()
    print('Nilai Y saat X = ', xTarget, ' adalah ', yAwal)


def heun(f, xAwal, yAwal, stepSize, xTarget, yEksak):
    temp = 0
    index = 0
    ea = 100
    while (xAwal < xTarget):
        print('X : ', xAwal)
        print('Y Euler : ', yAwal)
        if (index > 0):
            ea = abs((yEksak[index] - yAwal) / yEksak[index]) * 100
            print('EA : ', ea, '%')
        print()
        temp = yAwal
        k1 = f(xAwal, yAwal)
        k2 = f(xAwal + stepSize, yAwal + stepSize * k1)
        yAwal += stepSize * ((k1 + k2)/2)
        xAwal += stepSize
        index += 1
        ea = abs((yEksak[index] - yAwal) / yEksak[index]) * 100

    print('X : ', xAwal)
    print('Y : ', yAwal)
    print('EA : ', ea, '%')
    print()
    print('Nilai Y saat X = ', xTarget, ' adalah ', yAwal)


x1 = 0
y1 = 2
h1 = 0.3
xAkhir1 = 1.5
eksakY = [2, 1.7749, 1.657, 1.6096, 1.6188, 1.6873]
print('\nMetode Euler ( Runge Kutta Orde 1 ) : ')
print('======================================')
euler(func1, x1, y1, h1, xAkhir1, eksakY)
print('======================================')
print()

x0 = 0
y0 = 2
xAkhir = 1.5
h = 0.3
print('\nRunge Kutta Orde 2 : ')
print('======================')
heun(func1, x0, y0, h, xAkhir, eksakY)
print('======================')
print()
