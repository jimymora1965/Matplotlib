import numpy as np
import matplotlib.pyplot as  plt

x = np.linspace(-2,2,500)
y= x**2
y2 = x+1

# plt.plot(x,y,'b--', x,y2, 'r')#b-- afecta a y=x++2 la pone azul y discontinua,'r' afecta a  y=x+1y lo muestra 

#o lo pueo imprimir asi:
# general un label y una leyena al imprimir
plt.title("Graficando funciones")
plt.plot(x,y,'b--', label= "x**2")
plt.plot(x,y2,'r',  label = "x+1")
plt.legend(loc = "best")
print(x)#muestra el arreglo

plt.show()


