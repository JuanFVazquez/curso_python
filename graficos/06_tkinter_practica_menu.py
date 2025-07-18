import tkinter as tk
from tkinter import messagebox

# Funciones de ejemplo
def nuevo_archivo():
    messagebox.showinfo("Nuevo", "Has creado un nuevo archivo.")

def abrir_archivo():
    messagebox.showinfo("Abrir", "Has abierto un archivo.")

def cerrar_documento():
    valor = messagebox.askretrycancel("Retry", "no es posible cerrar el documento bloqueado")
    if valor == False:
        ventana.quit()

def cortar():
    messagebox.showinfo("Cortar", "Has cortado texto.")

def copiar():
    messagebox.showinfo("Copiar", "Has copiado texto.")

def opciones():
    messagebox.showinfo("Opciones", "Opciones de la herramienta.")

def acerca_de():
    messagebox.showinfo("Acerca de", "Aplicación creada con Tkinter.")

def aviso_licencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salir_aplicacion():
    respuesta = messagebox.askquestion("Salir", "Desea salir de la aplicación?")
    if respuesta == "yes":
        ventana.quit()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Menú")
ventana.geometry("400x300")

# Crear barra de menú
barra_menu = tk.Menu(ventana)

# Menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Cerrar", command=cerrar_documento)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir_aplicacion)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Edición
menu_edicion = tk.Menu(barra_menu, tearoff=0)
menu_edicion.add_command(label="Cortar", command=cortar)
menu_edicion.add_command(label="Copiar", command=copiar)
barra_menu.add_cascade(label="Edición", menu=menu_edicion)

# Menú Herramientas
menu_herramientas = tk.Menu(barra_menu, tearoff=0)
menu_herramientas.add_command(label="Opciones", command=opciones)
barra_menu.add_cascade(label="Herramientas", menu=menu_herramientas)

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
menu_ayuda.add_command(label="Licencia", command=aviso_licencia)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# Asociar la barra de menú a la ventana
ventana.config(menu=barra_menu)

# Ejecutar la aplicación
ventana.mainloop()
