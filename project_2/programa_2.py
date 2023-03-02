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

# Importación con alias
# Libreria para gráficar
# import matplotlib.pyplot as plt

# Impresión de consola
print("Impresión de consola")
print("Hola mundo")
print("\n")

# Variables
print("\nVariables")
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
print("\n")

# Operadores aritméticos
# + - * / % ** //
print("\nOperadores aritméticos")
print ("5 + 2 = ", 5 + 2)  # Suma
print ("5 - 2 = ", 5 - 2)  # Resta
print ("5 * 2 = ", 5 * 2)  # Multiplicación
print ("5 / 2 = ", 5 / 2)  # División
print ("5 % 2 = ", 5 % 2)  # Módulo
print ("5 ** 2 = ", 5 ** 2)  # Potencia
print ("5 // 2 = ", 5 // 2)  # Division redondeada
print("\n")

# Tipos de cadenas
print("\nTipos de cadenas")
cadenaConComilla = "esta es una comilla doble \""
cadenaMultilinea = '''Cadena
 de muchas
 líneas'''
print("%s " % 'cadena')
print("%s %s" % (cadenaConComilla, cadenaMultilinea))
print("Repite 5 " * 5) #Multiplica la cadena n veces
print("Sin salto de ", end="") #Cambia el salto del linea del print por lo que hay en end
print("línea")
print("\n")

print("\nFunción Main")
# Definición de función main
def main():
    print("Dentro del main")
    print("\n")

    # Obtener entrada del teclado
    print("\nEntrada del teclado")
    # Muestra el texo y guarda la entrada del teclado en la variable
    nombre = input('Nombre: ')
    # Se puede utilizar input sin parametros
    print('Hola ', nombre)
    edad = input('Edad: ')
    print("\n")

    # Obtener tipo de dato de una variable
    print("\nTipo de dato")
    print(type(edad))
    print("\n")

    # Convertir a un tipo de dato específico
    print("\nConversión de tipos de dato")
    edad = int(edad)
    print(type(edad))
    edad = float(edad)
    print(type(edad))
    print("\n")

    # Condiciones
    print("\nCondiciones")
    # Checa si la variable es mayor o igual al otro valor
    # En caso que la condicion sea verdadera se ejecutará la parte indentada dentro del if
    if edad >= 18:
        print("Eres mayor de edad")
    # En caso de no cumplise la condicion se efectuara la parte indentata del else
    else:
        print("Eres menor de edad")
    print("\n")

    # Operadores lógicos
    print("\nOperadores lógicos")
    print(True and False)
    print(True or False)
    print(not False)
    print("\n")

# Llamada a función
print("Llamada a función")
main()
print("\n")

print("\nListas")
# Define una lista
numeros = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
# Imprime elementos
print('Primer elemento de la lista', numeros[0])
numeros[0] = 'cero'
print('Primer elemento de la lista', numeros[0])
# Imprime desde el elemento 1 hasta el 3 sin incluirlo
print(numeros[1:3])
print("\n")
