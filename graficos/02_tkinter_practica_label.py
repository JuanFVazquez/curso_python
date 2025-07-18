import tkinter as tk

import os

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con un Label")
ventana.geometry("600x750")

# Ruta absoluta al directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(script_dir, "imagen.gif")

# Crear un Label con el texto que tú quieras
etiqueta = tk.Label(ventana, text="¡Hola! Esto es un ejemplo con Tkinter.", font=("Helvetica", 12))
etiqueta.pack(pady=40)

# Cargar imagen GIF
imagen = tk.PhotoImage(file=ruta_imagen)

# Etiqueta con imagen
etiqueta_imagen = tk.Label(ventana, image=imagen, bg="white")
etiqueta_imagen.pack(pady=10)

# Mantener referencia a la imagen para que no se elimine
etiqueta_imagen.image = imagen

# Ejecutar el bucle principal
ventana.mainloop()
