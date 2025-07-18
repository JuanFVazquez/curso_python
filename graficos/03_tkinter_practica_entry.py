import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Datos")
ventana.geometry("450x420")
ventana.resizable(False, False)

# Crear un Frame para contener el formulario
formulario = tk.Frame(ventana, padx=20, pady=20)
formulario.pack(fill="both", expand=True)

# Etiqueta y Entry para Nombre
tk.Label(formulario, text="Nombre:").grid(row=0, column=0, sticky="e", padx=(0, 10), pady=5)
entry_nombre = tk.Entry(formulario, width=30)
entry_nombre.grid(row=0, column=1, pady=5)

# Etiqueta y Entry para Apellido
tk.Label(formulario, text="Apellido:").grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)
entry_apellido = tk.Entry(formulario, width=30)
entry_apellido.grid(row=1, column=1, pady=5)

# Etiqueta y Entry para Dirección
tk.Label(formulario, text="Dirección:").grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)
entry_direccion = tk.Entry(formulario, width=30)
entry_direccion.grid(row=2, column=1, pady=5)

# Etiqueta y Entry para Password
tk.Label(formulario, text="Password:").grid(row=3, column=0, sticky="e", padx=(0, 10), pady=5)
entry_password = tk.Entry(formulario, width=30, show="*")
entry_password.grid(row=3, column=1, pady=5)

# Etiqueta para Comentarios
tk.Label(formulario, text="Comentarios:").grid(row=4, column=0, sticky="ne", padx=(0, 10), pady=5)

# Frame para Text + Scrollbar
comentario_frame = tk.Frame(formulario)
comentario_frame.grid(row=4, column=1, pady=5)

# Scrollbar
scroll = tk.Scrollbar(comentario_frame)
scroll.pack(side="right", fill="y")

# Campo de texto con scrollbar
text_comentarios = tk.Text(comentario_frame, width=30, height=5, yscrollcommand=scroll.set)
text_comentarios.pack(side="left")

scroll.config(command=text_comentarios.yview)

# Botón de envío
def enviar():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    direccion = entry_direccion.get()
    password = entry_password.get()
    comentarios = text_comentarios.get("1.0", "end-1c")

    # Mostrar datos por consola
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Dirección: {direccion}")
    print(f"Password: {password}")
    print(f"Comentarios: {comentarios}")

    # Escribir automáticamente nombre y apellido
    entry_nombre.delete(0, tk.END)
    entry_nombre.insert(0, "Juan")

    entry_apellido.delete(0, tk.END)
    entry_apellido.insert(0, "Pérez")

tk.Button(formulario, text="Enviar", command=enviar).grid(row=5, column=0, columnspan=2, pady=15)

ventana.mainloop()
