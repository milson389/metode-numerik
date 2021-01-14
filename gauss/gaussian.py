import numpy as np

a = [[2, 1, 1], [1, 2, -1], [3, -1, 1]]
b = [12, 3, 11]

soal = np.column_stack((a, b))

row = len(a)
col = len(a[0])

# Forward Elimination
for i in range(row-1):
    for j in range(i+1, row):
        faktor = a[j][i]/a[i][i]
        a[j][i] = 0
        for k in range(i+1, row):
            a[j][k] -= faktor*a[i][k]
        b[j] -= faktor*b[i]

# Backward substitution
x = []
for i in range(row):
    x.append(0)

n = row-1
x[n] = b[n]/a[n][n]

for i in range(n-1, -1, -1):
    jumlah = 0
    for j in range(i+1, row):
        jumlah += a[i][j]*x[j]
    x[i] = (b[i]-jumlah)/a[i][i]

# Output
print('\nMatrix : ')
print(soal)
print()

