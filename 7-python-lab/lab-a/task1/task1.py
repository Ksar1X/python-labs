import numpy as np
import matplotlib.pyplot as plt

x = [1, 3, 5, 7]
y = np.array ([27, 30, 21, 29])

plt.plot(x, y, color = 'green')
plt.title('Temperature plot')
plt.xlabel('day')
plt.ylabel('temperature')
plt.grid(True)
plt.show()
