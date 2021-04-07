# coding=utf-8
# Importamos el módulo para la interfaz gráfica
import tkinter

# Creación de ventana
# creamos la variable que tendrá la ventana
ventana = tkinter.Tk()

# Definición del tamaño de la ventana
# tamaño de la ventana ancho x alto
ventana.geometry("720x480")

# Define título de la ventana
ventana.title("Hola Python")

# Variable con botón
bottonHola = tkinter.Button(text="Hola")
bottonMundo = tkinter.Button(text="Mundo")

# Agrega el botón en la ventana
bottonHola.pack()
bottonMundo.pack()

# Ejecución del programa con la ventana
ventana.mainloop()
