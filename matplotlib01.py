import matplotlib.pyplot as plt 
import numpy as np

"""

x= [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 60]

plt.plot(x,y)
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()


"""

#RED CIRCLES
plt.plot(np.arange(10), np.arange(10), "ro", label="Red Circles")

#YELLOW DASHES
plt.plot(np.arange(10), np.arange(0, 20, 2), "y--", label="Yellow Dashes")

#GREEN TRIANGLES
plt.plot(np.arange(10), np.arange(0, 40, 4), "g^", label="Green Triangles")

#BLUE SQUARES
plt.plot(np.arange(10), np.arange(0,60, 6), "bs", label="Blue Squares") 


#



