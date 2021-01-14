# Audie Milson (535180021)
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
        result += term

    return result


x = [
    [6.509, 16.41], [8.0814, 16.6266], [3.9090, 15.9], [6.1082, 16.3467], [9.9294, 16.8325], [
        9.9629, 16.8359], [2.2558, 15.3505], [3.0724, 15.6594], [1.5146, 14.9522], [5.4081, 16.2245]
]

xTanya = 7.3
xTanya1 = 5.0

orde = int(input('Masukkan Nilai N ( Orde ke -N ) untuk f(x=7.3) : '))
print("\nHasil Perhitungan Orde", orde,
      ": " "{:.4f}".format(lagrange(x, xTanya, orde)))

# Untuk menampilkan hasil per orde yang ditentukan
for i in range(1, orde):
    print("\nHasil Perhitungan Orde", i,
          ": " "{:.4f}".format(lagrange(x, xTanya, i)))
    if(i == 1):
        continue
    else:
        print('Nilai EA dibandingkan Orde sebelumnya : ',
              dapetEa(lagrange(x, xTanya, i-1), lagrange(x, xTanya, i)), '%')
        print()


orde = int(input('Masukkan Nilai N ( Orde ke -N ) untuk f(x=5.0) : '))
print("\nHasil Perhitungan Orde", orde,
      ": " "{:.4f}".format(lagrange(x, xTanya1, orde)))
# Untuk menampilkan hasil per orde yang ditentukan
for i in range(1, orde):
    print("\nHasil Perhitungan Orde", i,
          ": " "{:.4f}".format(lagrange(x, xTanya1, i)))
    if(i == 1):
        continue
    else:
        print('Nilai EA dibandingkan Orde sebelumnya : ',
              dapetEa(lagrange(x, xTanya1, i-1), lagrange(x, xTanya1, i)), '%')
        print()
