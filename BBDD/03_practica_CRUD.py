import sqlite3
import os
import tkinter as tk
from tkinter import messagebox, Menu, scrolledtext

# ---------------------- FUNCIONES DE LA BBDD ----------------------

def conectar():
    if os.path.exists("Usuarios.db"):
        messagebox.showwarning("Advertencia", "La base de datos ya existe.")
    else:
        conexion = sqlite3.connect("Usuarios.db")
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE Datos_Usuarios (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO TEXT,
                PASSWORD TEXT,
                APELLIDO TEXT,
                DIRECCION TEXT,
                COMENTARIOS TEXT
            )
        ''')
        conexion.commit()
        conexion.close()
        messagebox.showinfo("BBDD", "Base de datos creada con éxito.")

# ---------------------- FUNCIONES CRUD ----------------------

def crear():
    conexion = sqlite3.connect("Usuarios.db")
    cursor = conexion.cursor()
    datos = (nombre.get(), password.get(), apellido.get(), direccion.get(), texto_comentarios.get("1.0", tk.END))
    cursor.execute("INSERT INTO Datos_Usuarios VALUES (NULL, ?, ?, ?, ?, ?)", datos)
    conexion.commit()
    conexion.close()
    messagebox.showinfo("Crear", "Registro insertado con éxito")
    limpiar_campos()

def leer():
    if not id.get().isdigit():
        messagebox.showwarning("Leer", "Por favor, introduce un ID numérico para buscar.")
        return
    conexion = sqlite3.connect("Usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Datos_Usuarios WHERE ID = ?", (id.get(),))
    fila = cursor.fetchone()
    conexion.close()
    if fila:
        id.set(fila[0])
        nombre.set(fila[1])
        password.set(fila[2])
        apellido.set(fila[3])
        direccion.set(fila[4])
        texto_comentarios.delete("1.0", tk.END)
        texto_comentarios.insert(tk.END, fila[5])
    else:
        messagebox.showwarning("Leer", "No se encontró el registro")

def actualizar():
    if not id.get().isdigit():
        messagebox.showwarning("Actualizar", "Por favor, introduce un ID numérico para actualizar.")
        return
    conexion = sqlite3.connect("Usuarios.db")
    cursor = conexion.cursor()
    datos = (nombre.get(), password.get(), apellido.get(), direccion.get(), texto_comentarios.get("1.0", tk.END), id.get())
    cursor.execute("UPDATE Datos_Usuarios SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? WHERE ID=?", datos)
    conexion.commit()
    conexion.close()
    messagebox.showinfo("Actualizar", "Registro actualizado con éxito")
    limpiar_campos()

def borrar():
    if not id.get().isdigit():
        messagebox.showwarning("Eliminar", "Por favor, introduce un ID numérico para borrar.")
        return
    conexion = sqlite3.connect("Usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Datos_Usuarios WHERE ID = ?", (id.get(),))
    conexion.commit()
    conexion.close()
    messagebox.showinfo("Eliminar", "Registro eliminado con éxito")
    limpiar_campos()

# ---------------------- FUNCIONES AUXILIARES ----------------------

def limpiar_campos():
    id.set("")
    nombre.set("")
    password.set("")
    apellido.set("")
    direccion.set("")
    texto_comentarios.delete("1.0", tk.END)

def salir():
    if messagebox.askyesno("Salir", "¿Deseas salir de la aplicación?"):
        root.destroy()

# ---------------------- INTERFAZ GRÁFICA ----------------------

root = tk.Tk()
root.title("Gestor de Usuarios")

# Variables
id = tk.StringVar()
nombre = tk.StringVar()
password = tk.StringVar()
apellido = tk.StringVar()
direccion = tk.StringVar()

# Validación para el campo ID
def validar_id(texto):
    return texto.isdigit() or texto == ""

# Menú superior
barra_menu = Menu(root)
root.config(menu=barra_menu)

# Menú BBDD
menu_bbdd = Menu(barra_menu, tearoff=0)
menu_bbdd.add_command(label="Conectar", command=conectar)
menu_bbdd.add_separator()
menu_bbdd.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="BBDD", menu=menu_bbdd)

# Menú Borrar
menu_borrar = Menu(barra_menu, tearoff=0)
menu_borrar.add_command(label="Borrar Campos", command=limpiar_campos)
barra_menu.add_cascade(label="Borrar", menu=menu_borrar)

# Menú CRUD
menu_crud = Menu(barra_menu, tearoff=0)
menu_crud.add_command(label="Create", command=crear)
menu_crud.add_command(label="Read", command=leer)
menu_crud.add_command(label="Update", command=actualizar)
menu_crud.add_command(label="Delete", command=borrar)
barra_menu.add_cascade(label="CRUD", menu=menu_crud)

# Menú Ayuda
menu_ayuda = Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Licencia", command=lambda: messagebox.showinfo("Licencia", "Aplicación con licencia MIT"))
menu_ayuda.add_command(label="Acerca de...", command=lambda: messagebox.showinfo("Acerca de", "App de gestión de usuarios."))
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# Formulario de entrada
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="ID:").grid(row=0, column=0, sticky="e")
entry_id = tk.Entry(frame, textvariable=id, validate="key")
entry_id['validatecommand'] = (entry_id.register(validar_id), "%P")
entry_id.grid(row=0, column=1)

tk.Label(frame, text="Nombre:").grid(row=1, column=0, sticky="e")
tk.Entry(frame, textvariable=nombre).grid(row=1, column=1)

tk.Label(frame, text="Password:").grid(row=2, column=0, sticky="e")
tk.Entry(frame, textvariable=password, show="*").grid(row=2, column=1)

tk.Label(frame, text="Apellido:").grid(row=3, column=0, sticky="e")
tk.Entry(frame, textvariable=apellido).grid(row=3, column=1)

tk.Label(frame, text="Dirección:").grid(row=4, column=0, sticky="e")
tk.Entry(frame, textvariable=direccion).grid(row=4, column=1)

tk.Label(frame, text="Comentarios:").grid(row=5, column=0, sticky="ne")
texto_comentarios = scrolledtext.ScrolledText(frame, width=30, height=5)
texto_comentarios.grid(row=5, column=1, padx=5, pady=5)

# Botones inferiores
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Create", width=10, command=crear).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Read", width=10, command=leer).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Update", width=10, command=actualizar).grid(row=0, column=2, padx=5)
tk.Button(frame_botones, text="Delete", width=10, command=borrar).grid(row=0, column=3, padx=5)

root.mainloop()
