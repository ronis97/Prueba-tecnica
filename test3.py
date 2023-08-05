import tkinter as tk
from tkinter import ttk

def seleccionar_opcion(event):
    seleccion = combo_var.get()
    mensaje_label.config(text=f"Opción seleccionada: {seleccion}")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Selector de Opciones - Combobox")

# Crear una variable para almacenar la selección
combo_var = tk.StringVar()

# Crear una lista desplegable (Combobox)
combo = ttk.Combobox(ventana, textvariable=combo_var)
combo['values'] = ('Opción 1', 'Opción 2', 'Opción 3')
combo.bind("<<ComboboxSelected>>", seleccionar_opcion)
combo.pack(pady=20)

# Crear una etiqueta para mostrar mensajes
mensaje_label = tk.Label(ventana, text="", font=("Helvetica", 12))
mensaje_label.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
