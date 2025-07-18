import tkinter as tk
from tkinter import filedialog

# Oculta la ventana principal de Tkinter
root = tk.Tk()
root.withdraw()

# Abre el selector de archivos
file_path = filedialog.askopenfilename(
    title="Selecciona un archivo .txt o .py",
    filetypes=[("Archivos de texto", "*.txt"), ("Archivos de python", "*.py")]
)

# Si el usuario selecciona un archivo
if file_path:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("\n--- Contenido del archivo ---\n")
            print(content)
            print("\n--- Fin del contenido ---\n")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
else:
    print("No se seleccionó ningún archivo.")
