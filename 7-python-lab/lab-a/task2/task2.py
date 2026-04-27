import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 5, 0.5)
y = np.arange(0, 25, 2.5)

plt.plot(x,y, marker = 's', color =  'red')
plt.text(float(x[0]), float(y[0]), f'({x[0]}, {y[0]})', fontsize = 12)
plt.text(float(x[-1]), float(y[-1]), '(5, 25)', fontsize = 12)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()