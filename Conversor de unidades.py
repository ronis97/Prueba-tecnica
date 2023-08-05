import tkinter as tk
from tkinter import ttk

  
def convertir_area(valor, unidad_origen, unidad_destino):
    """Funcion que convierte medidas de area entre las cuales estan metros cuadrados "m2", milimetros cuadrados "mm2", 
    centrimetros cuadrados "cm2" y kilometros cuadrados "km2"

    Args:
        valor (float): valor a convertir de unidad_origen a unidad_destino
        unidad_origen (String): unidad inicial de medida
        unidad_destino (_type_): unidad final de medida

    Returns:
        float: Area convertida de acuerdo a la unidad de medida especificada
        String: Valor no valido en caso de presentarse error
    """
    valor = float(valor)
    print(valor, unidad_origen, unidad_destino)
    # Definir factores de conversión
    factores = {
        "m2": 1,
        "mm2": 1000000,
        "cm2": 10000,
        "km2": 0.000001
    }
    
    if unidad_origen in factores and unidad_destino in factores:
        area_destino = valor * (factores[unidad_destino] / factores[unidad_origen])
        print(area_destino)
        return area_destino
    else:
        return "Valor no valido"
    
def convertir_longitud(valor, unidad_origen, unidad_destino):
    """Funcion que convierte medidas de longitud entre las cuales estan milimetros, pulgadas, centimetros y pulgadas

    Args:
        valor (float): valor a convertir de unidad_origen a unidad_destino
        unidad_origen (String): unidad inicial de medida
        unidad_destino (_type_): unidad final de medida

    Returns:
        float: Area convertida de acuerdo a la unidad de medida especificada
        String: Valor no valido en caso de presentarse error_
    """

    # Definir factores de conversión
    factores = {
        "mm": 1,
        "in": 39.3701,
        "cm": 100,
        "ft": 3.28084
    }
    
    if unidad_origen in factores and unidad_destino in factores:
        longitud_destino = valor * (factores[unidad_destino] / factores[unidad_origen])
        return string(longitud_destino)
    else:
        return "Unidad de longitud no válida"

#Falta definir el resto de funciones tipo convertir <<Medida conversion>>, el proceso es similar al representado, usando chatGPT podemos
#crear rapidamente el prototipo de la funcion para ajustarlo a los requerimientos de nuestro programa

def conversion (tipo_medida, tipo_unidad_inicial, valor, tipo_unidad_final):
    """Funcion que se encarga de mapear los distintos tipos de conversion para realizar los calculos solicitados

    Args:
        tipo_medida (String): El tipo de medida que se utilizara: Area, longitud, tiempo, etc.
        tipo_unidad_inicial (String): La unidad de medida inicial que queremos convertir a la unidad de medida final
        valor (float): el valor (cantidad) de la unidad de medida proporcionada incialmente
        tipo_unidad_final (String): La unidad de medida final que esperamos recibir.

    Esta funcion es el equivalente a un metodo en Java por lo tanto no retorna ningun valor, sino que llama a otras funciones que si
    retornan un valor
 
    """
    match tipo_medida:
        case 1:
            convertir_area(valor, tipo_unidad_inicial, tipo_unidad_final)
        
        case 2:
            convertir_longitud(valor, tipo_unidad_inicial,tipo_unidad_final)

        


def mostrar_seleccion():
    """Esta funcion se encarga de generar los "labels" que muestran la informacion solicitada de acuerdo a las solicitudes de cada
    tipo de medida solicitado, es una especie de "muestre la conversion final" al usuario.
    """
    seleccion_label.config(text="Selecciones:\n"
                                 f"Area: {entry1.get()} {lista1_var.get()} es {conversion(1,lista1_var.get(),entry1.get(),lista7_var.get())} {lista7_var.get()}\n"
                                 f"Longitud: {entry2.get()} {entry2.get()} es {conversion(2,lista1_var.get(),entry1.get(),lista7_var.get())} {lista8_var.get()}\n"
                                 f"Volumen: {entry3.get()} {entry3.get()} es {conversion(3,lista1_var.get(),entry1.get(),lista7_var.get())} {lista9_var.get()}\n"
                                 f"Temperatura: {entry4.get()} {entry4.get()} es {conversion(4,lista1_var.get(),entry1.get(),lista7_var.get())} {lista10_var.get()}\n"
                                 f"Tiempo: {entry5.get()} {entry5.get()} es {conversion(5,lista1_var.get(),entry1.get(),lista7_var.get())} {lista11_var.get()}\n"
                                 f"Masa: {entry6.get()} {entry6.get()} es {conversion(6,lista1_var.get(),entry1.get(),lista7_var.get())} {lista12_var.get()}")
                                 

# Crear la ventana
ventana = tk.Tk()
ventana.title("Interfaz con Listas Desplegables y Campos de Entrada")

# Crear listas desplegables y sus variables (Columna 1)
lista1_var = tk.StringVar()
lista2_var = tk.StringVar()
lista3_var = tk.StringVar()
lista4_var = tk.StringVar()
lista5_var = tk.StringVar()
lista6_var = tk.StringVar()

#Crear lista de medidas de Area
Area_medidas = ("m2","mm2","cm2","km2")

#Crear lista de medidas de Longitud
Longitud_medidas = ("mm", "in", "cm", "ft")

#Crear lista de medidas de volumen
Volumen_medidas = ("m3", "bbl", "gal","cm3")

#Crear lista de medidas de Temperatura
Temperatura_medidas = ("C","K","F")

#Crear lista de medidas de Tiempo
Tiempo_medidas = ("d","h","min")

#Crear lista de medidas de Masa
Masa_medidas = ("kg", "g", "mg")


#Generar campos de area
lista1_label = tk.Label(ventana, text="Area:")
lista1_label.grid(row=0, column=0, sticky="e")
entry1_var = tk.StringVar()
entry1 = tk.Entry(ventana, textvariable=entry1_var)
entry1.grid(row=0, column=1, padx=5)
lista1 = ttk.Combobox(ventana, textvariable=lista1_var, values=Area_medidas, state="readonly")
lista1.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")

#Generar campos de longitud
lista2_label = tk.Label(ventana, text="Longitud:")
lista2_label.grid(row=2, column=0, sticky="e")
entry2_var = tk.StringVar()
entry2 = tk.Entry(ventana, textvariable=entry2_var)
entry2.grid(row=2, column=1, padx=5)
lista2 = ttk.Combobox(ventana, textvariable=lista2_var, values=Longitud_medidas, state="readonly")
lista2.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")

#Generar campos de volumen
lista3_label = tk.Label(ventana, text="Volumen:")
lista3_label.grid(row=4, column=0, sticky="e")
entry3_var = tk.StringVar()
entry3 = tk.Entry(ventana, textvariable=entry3_var)
entry3.grid(row=4, column=1, padx=5)
lista3 = ttk.Combobox(ventana, textvariable=lista3_var, values=Volumen_medidas, state="readonly")
lista3.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="w")

#Generar campos de temperatura
lista4_label = tk.Label(ventana, text="Temperatura:")
lista4_label.grid(row=6, column=0, sticky="e")
entry4_var = tk.StringVar()
entry4 = tk.Entry(ventana, textvariable=entry4_var)
entry4.grid(row=6, column=1, padx=5)
lista4 = ttk.Combobox(ventana, textvariable=lista4_var, values=Temperatura_medidas, state="readonly")
lista4.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="w")

#Generar campos de tiempo
lista5_label = tk.Label(ventana, text="Tiempo:")
lista5_label.grid(row=8, column=0, sticky="e")
entry5_var = tk.StringVar()
entry5 = tk.Entry(ventana, textvariable=entry5_var)
entry5.grid(row=8, column=1, padx=5)
lista5 = ttk.Combobox(ventana, textvariable=lista5_var, values=Tiempo_medidas, state="readonly")
lista5.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="w")

#Generar campos de masa
lista6_label = tk.Label(ventana, text="Masa:")
lista6_label.grid(row=10, column=0, sticky="e")
entry6_var = tk.StringVar()
entry6 = tk.Entry(ventana, textvariable=entry6_var)
entry6.grid(row=10, column=1, padx=5)
lista6 = ttk.Combobox(ventana, textvariable=lista6_var, values=Masa_medidas, state="readonly")
lista6.grid(row=11, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Agregar el texto "Convertir a"
convertir_label = tk.Label(ventana, text="Convertir a:")
convertir_label.grid(row=0, column=2, padx=5)

# Crear listas desplegables para la conversión (Columna 2)
lista7_var = tk.StringVar()
lista8_var = tk.StringVar()
lista9_var = tk.StringVar()
lista10_var = tk.StringVar()
lista11_var = tk.StringVar()
lista12_var = tk.StringVar()

#Cada una de las siguientes instrucciones genera las opciones para configurar visualmente la unidad de medida final
lista7 = ttk.Combobox(ventana, textvariable=lista7_var, values=Area_medidas, state="readonly")
lista7.grid(row=1, column=2, padx=5, pady=5, sticky="w")

lista8 = ttk.Combobox(ventana, textvariable=lista8_var, values=Longitud_medidas, state="readonly")
lista8.grid(row=3, column=2, padx=5, pady=5, sticky="w")

lista9 = ttk.Combobox(ventana, textvariable=lista9_var, values=Volumen_medidas, state="readonly")
lista9.grid(row=5, column=2, padx=5, pady=5, sticky="w")

lista10 = ttk.Combobox(ventana, textvariable=lista10_var, values=Temperatura_medidas, state="readonly")
lista10.grid(row=7, column=2, padx=5, pady=5, sticky="w")

lista11 = ttk.Combobox(ventana, textvariable=lista11_var, values=Tiempo_medidas, state="readonly")
lista11.grid(row=9, column=2, padx=5, pady=5, sticky="w")

lista12 = ttk.Combobox(ventana, textvariable=lista12_var, values=Masa_medidas, state="readonly")
lista12.grid(row=11, column=2, padx=5, pady=5, sticky="w")

# Crear un botón para mostrar la selección
mostrar_boton = tk.Button(ventana, text="Mostrar Selección", command=mostrar_seleccion)
mostrar_boton.grid(row=12, column=0, columnspan=3, pady=20)

# Crear una etiqueta para mostrar las selecciones
seleccion_label = tk.Label(ventana, text="", font=("Helvetica", 12))
seleccion_label.grid(row=13, column=0, columnspan=3)

# Espacio entre filas
ventana.grid_rowconfigure(2, minsize=20)
ventana.grid_rowconfigure(4, minsize=20)
ventana.grid_rowconfigure(6, minsize=20)
ventana.grid_rowconfigure(8, minsize=20)
ventana.grid_rowconfigure(10, minsize=20)

# Espacio entre columnas
ventana.grid_columnconfigure(1, minsize=20)
ventana.grid_columnconfigure(2, minsize=20)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()



