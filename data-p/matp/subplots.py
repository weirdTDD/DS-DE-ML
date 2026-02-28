import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 4))

plt.subplot(131)

#red dots
plt.plot(np.arange(10),np.arange(10), "ro")
plt.axis([0, 10, 0, 60])
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")

plt.subplot(132)

#yellow_dashes
plt.plot(np.arange(10),np.arange(0, 20, 2), "y--")
plt.axis([0, 10, 0, 60])
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")

plt.subplot(133)

#green_triangle
plt.plot(np.arange(10),np.arange(0, 40, 4), "g^")
plt.axis([0, 10, 0, 60])
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")

plt.suptitle("3 Subplots")

plt.show()