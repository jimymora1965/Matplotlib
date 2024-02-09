#crear un codigo usando la funcion cuadratica y= x**2, imprimirla. Luego  mostrar el array desde -2 hasta 2 con 500 valores. luego imprimir el promedio
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2,2,500)
y = x**2
plt.plot(x,y)
plt.title("Practicas Jimy")
plt.xlabel("Valores del arreglo")
plt.ylabel("Valores de la funcion")
plt.grid(True)#para poner cuadriculas a la grafica
plt.show() 

#ojo con estecodigo. El de arriba plotea la funcionen una  grafica y el de abajo muestra como seria el array con numpy.

print(x)

print()

#para mostrar el promedio de ese arreglo
# Calcular el promedio de los valores en x
promedio = np.mean(x)
# Mostrar el promedio
print("El promedio de los valores en x es:", promedio)
