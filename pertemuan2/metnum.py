import matplotlib.pyplot as plt
import numpy as np

# Untuk perhitungan numerik bisa menggunakan beberapa library berikut
# NumPy, SciPy, Matplotlib
# cara instalasi dari cmd, menggunakan perintah :
# pip install numpy scipy matplotlib

# matplotlib
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.show()

# numpy
t = np.arange(0.0, 5.0, 0.2)
print(t)

# r-- untuk memunculkan garis merah putus2
# resolusi bagus
# plt.figure(dpi=300)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.title('Grafik macam macam')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.legend(['Garis lurus', 'Kuadratik', 'Pangkat 3'])
plt.grid(True)
plt.show()


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


# lambda function
# f= lambda t: np.exp(-t) * np.cos(2*np.pi*t)
print(f(6))

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.subplot(211)
plt.subplot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.subplot(t2, np.cos(2*np.pi*t2), 'r--')

plt.show()
