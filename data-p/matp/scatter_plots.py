import numpy as np
import matplotlib.pyplot as plt

x = np.array([np.random.rand() for j in range(20)])
y = np.array([np.random.rand() for j in range(20)])
plt.scatter(x,y)
plt.axis([0,1,0,1])

plt.show()