# coding=utf-8
# Comentarios unilinea en Python 3
""" Comentarios
    multilinea
    en
    Python
    3
"""
# Se importan librerias para usar
# import random
# import sys  # Funciones del sistema
# import os  # Funciones del sistema operativo

# importación con alias
# Libreria para gráficar
# import matplotlib.pyplot as plt

# Impresión de consola
print("Hola mundo")

# Variables
# Sus nombres no deben comenzar en mayusculas
caracter = 'a'
cadena = "hola"
numeroEntero = 9
numeroReal = 93.3
booleanoVerdadero = True
booleanoFalso = False
# Multiple declaracion y asignación
x, y = 10, 20

print(cadena)
print(x, y)

# Operadores aritméticos
# + - * / % ** //
print ("5 + 2 = ", 5 + 2)  # Suma
print ("5 - 2 = ", 5 - 2)  # Resta
print ("5 * 2 = ", 5 * 2)  # Multiplicación
print ("5 / 2 = ", 5 / 2)  # División
print ("5 % 2 = ", 5 % 2)  # Módulo
print ("5 ** 2 = ", 5 ** 2)  # Potencia
print ("5 // 2 = ", 5 // 2)  # Division redondeada


# Definición de funcion main
def main():
    print("Dentro del main")
    # Obtener entrada del teclado
    # Muestra el texo y guarda la entrada del teclado en la variable
    nombre = input('Nombre: ')
    # Se puede utilizar input sin parametros
    print('Hola ', nombre)
    edad = input('Edad: ')
    # Obtener tipo de dato de una variable
    print(type(edad))
    # Convertir a un tipo de dato específico
    edad = int(edad)
    print(type(edad))
    edad = float(edad)
    print(type(edad))

    # Condiciones
    # Checa si la variable es mayor o igual al otro valor
    # En caso que la condicion sea verdadera se ejecutará la parte indentada dentro del if
    if edad >= 18:
        print("Eres mayor de edad")
    # En caso de no cumplise la condicion se efectuara la parte indentata del else
    else:
        print("Eres menor de edad")

    # Operadores lógicos
    print(True and False)
    print(True or False)
    print(not False)


# Llamada a función
main()
