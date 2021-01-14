import matplotlib.pyplot as plt
import numpy as np
import math


def func(x):
    return (4*math.sin(x)) - math.exp(x)
    # return (x**3)-(13*x)-12


x = []
y = []
# for i in range(-8, 8, 2):
#     x.append(i)
#     y.append(func(i))

# plt.plot(x,y)
# plt.grid()
# plt.show()

x = [-0.5, 0, 0.5]
y = []

for i in x:
    y.append(func(i))

plt.plot(x, y)
plt.show()
