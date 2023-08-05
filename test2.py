import tkinter as tk
from tkinter import Menu

def abrir_archivo():
    # Aquí podrías agregar el código para abrir un archivo
    mensaje_label.config(text="Archivo abierto")

def guardar_archivo():
    # Aquí podrías agregar el código para guardar un archivo
    mensaje_label.config(text="Archivo guardado")

def salir():
    ventana.quit()

# Crear la ventana
ventana = tk.Tk()
ventana.title("Menú Desplegable en Tkinter")

# Crear un menú
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

# Crear un menú Archivo
menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# Agregar el menú Archivo a la barra de menú
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Crear una etiqueta para mostrar mensajes
mensaje_label = tk.Label(ventana, text="", font=("Helvetica", 12))
mensaje_label.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
