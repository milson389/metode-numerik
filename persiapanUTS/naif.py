import numpy as np


def gaussNaive(matrixA, matrixB):
    row = len(matrixA)
    col = len(matrixA[0])

    # Forward Elimination
    for i in range(row-1):
        for j in range(i+1, row):
            faktor = matrixA[j][i]/matrixA[i][i]
            matrixA[j][i] = 0
            for k in range(i+1, row):
                matrixA[j][k] -= faktor*matrixA[i][k]
            matrixB[j] -= faktor*matrixB[i]


def backwardSub(matrixA, matrixB):
    # backward substitution
    x = []
    for i in range(len(matrixA)):
        x.append(0)

    n = len(matrixA)-1
    x[n] = matrixB[n]/matrixA[n][n]

    for i in range(n-1, -1, -1):
        jumlah = 0
        for j in range(i+1, n+1):
            jumlah += matrixA[i][j]*x[j]
        x[i] = (matrixB[i]-jumlah)/matrixA[i][i]

    for i in range(n+1):
        print('Nilai X', i+1, ' : ', "{:.4f}".format(x[i]))


# Output

a = [[2, 12, 17], [-3, -7, -8], [1, 4, 6]]
b = [-32, 6, -7]

soal = np.column_stack((a, b))

print('\nMatrix Awal : ')
print(soal)
print()
print('Matix Hasil Gauss Elim : ')
gaussNaive(a, b)
print(np.column_stack((a, b)))
print()
backwardSub(a, b)

c = [[2, 1, 1], [1, 2, -1], [3, -1, 1]]
d = [12, 3, 11]

soal1 = np.column_stack((c, d))
print('\nMatrix Awal : ')
print(soal1)
print()
print('Matix Hasil Gauss Elim : ')
gaussNaive(c, d)
print(np.column_stack((c, d)))
print()
backwardSub(c, d)

e = [[2, 1], [1, 2]]
f = [5, 4]

soal2 = np.column_stack((e, f))
print('\nMatrix Awal : ')
print(soal2)
print()
print('Matix Hasil Gauss Elim : ')
gaussNaive(e, f)
print(np.column_stack((e, f)))
print()
backwardSub(e, f)
