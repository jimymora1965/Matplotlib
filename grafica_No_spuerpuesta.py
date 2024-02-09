import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(14,5))#para aumentar el tamaño de las figuras en consola

x = np.linspace(-2,2,500)
y = x**2
y2 = x+1

plt.subplot(1,2,1)
plt.plot(x,y,"b--")
plt.xlabel("x1",fontsize=14)
plt.ylabel("y1",fontsize=14)

plt.subplot(1,2,2)
plt.plot(x,y2,"r")
plt.xlabel("x2",fontsize=14)
plt.ylabel("y2",fontsize=14)

plt.show()
print(x)

