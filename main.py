import numpy as np
import matplotlib.pyplot as plt
import random

N = int(input("Введите колличество шагов: "))
M = int(input("Введите максимальный размер шага: "))
x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)


for i in range(1, N):
    x[i] = x[i-1] + random.uniform(-M, M)
    y[i] = y[i-1] + random.uniform(-M, M)
    z[i] = z[i-1] + random.uniform(-M, M)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)

plt.show()
