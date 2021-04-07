# coding=utf-8
# Gráficas en Python 3
# Utilizando la libreria Matplotlib se puede obtener desde pip
import matplotlib.pyplot as plt

# Arreglos con los puntos a gráficar en el eje x,y
arrayX = [1, 2, 3, 4]
arrayY = [6, 7, 9, 12]
# Asigna los arreglos en la gráfica
plt.plot(arrayX, arrayY)

# Ingresa el título de la gráfica
plt.title('Título')
# Leyenda para el eje x, y
plt.xlabel('eje X')
plt.ylabel('eje Y')

# Muestra la gráfica
plt.show()
