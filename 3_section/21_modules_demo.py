import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


plt.show()
print(pd.read_csv('../files_to_process/pokemon.csv').head(50).to_string())
print('------------------------------------------------')

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.ylabel('some numbers')
plt.show()
print('------------------------------------------------')


t = np.arange(0., 5., 0.2)
print(t)
print('------------------------------------------------')

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.ylabel('some numbers')
plt.show()
print('------------------------------------------------')

min_v = 0
max_v = 4 * np.pi
step = 0.1

x = np.arange(min_v, max_v, step)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('angle')
plt.ylabel('sin(angle)')
plt.show()
