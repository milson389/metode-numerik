def dapetEa(fp, fp1):
    return "{:.4f}".format(abs(((fp1-fp)/fp1)*100))


def lagrange(f: list, xi: float, n: int) -> float:
    result = 0
    orde = n+1
    for i in range(orde):
        term = f[i][1]
        for j in range(orde):
            if j != i:
                term *= (xi - f[j][0]) / (f[i][0] - f[j][0])
                list.append(term/f[i][1])
        result += term

    return result


f = [[10.5, 45.2], [12, 58.1], [12.4, 60.2], [12.8, 64.4]]
xTanya = 11.5
list = []

a = [[6, 5.39], [8, 5.06], [9, 4.94], [10, 4.85]]
aTanya = 7

print('\nLagrange Method\n----------------')
print("\nPrediksi nilai Keuntungan Promosi\n")
for i in range(1, 4):
    print("\nHasil Perhitungan Orde", i,
          ": " "{:.4f}".format(lagrange(f, xTanya, i)))
    if(i == 1):
        continue
    else:
        print('Nilai EA dibandingkan Orde sebelumnya : ',
              dapetEa(lagrange(f, xTanya, i-1), lagrange(f, xTanya, i)), '%')
        print()


print('\nLagrange Method\n----------------')
print("\nPrediksi nilai tabel distribusi f dengan v1 = 7 v2 = 10\n")
for i in range(1, 4):
    print("\nHasil Perhitungan Orde", i,
          ": " "{:.4f}".format(lagrange(a, aTanya, i)))
    if(i == 1):
        continue
    else:
        print('Nilai EA dibandingkan Orde sebelumnya : ',
              dapetEa(lagrange(a, aTanya, i-1), lagrange(a, aTanya, i)), '%')
        print()
