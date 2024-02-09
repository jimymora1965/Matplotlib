""" import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [7,6,5,4,3,2,1]

plt.plot(x,y)

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Ejemplo Jimy")

plt.show()
 """
 
print("Para aumentar el tamaño de los ejes X y Y")
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [7, 6, 5, 4, 3, 2, 1]

plt.plot(x, y)

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Ejemplo Jimy")

# Establecer límites de los ejes y ticks personalizados
plt.xticks(range(11))  # Ticks de 0 a 10 en el eje x
plt.yticks(range(11))  # Ticks de 0 a 10 en el eje y

plt.show()
