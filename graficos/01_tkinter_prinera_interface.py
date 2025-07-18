import tkinter as tk
from tkinter import PhotoImage

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Datos")
ventana.geometry("500x600")
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

# Etiqueta y Radiobuttons para Género
tk.Label(formulario, text="Género:").grid(row=4, column=0, sticky="e", padx=(0, 10), pady=5)
genero_var = tk.StringVar(value="Masculino")
genero_frame = tk.Frame(formulario)
genero_frame.grid(row=4, column=1, pady=5, sticky="w")

tk.Radiobutton(genero_frame, text="Masculino", variable=genero_var, value="Masculino").pack(side="left", padx=5)
tk.Radiobutton(genero_frame, text="Femenino", variable=genero_var, value="Femenino").pack(side="left", padx=5)
tk.Radiobutton(genero_frame, text="Otro", variable=genero_var, value="Otro").pack(side="left", padx=5)

# Etiqueta para Comentarios
tk.Label(formulario, text="Comentarios:").grid(row=5, column=0, sticky="ne", padx=(0, 10), pady=5)
comentario_frame = tk.Frame(formulario)
comentario_frame.grid(row=5, column=1, pady=5)
scroll = tk.Scrollbar(comentario_frame)
scroll.pack(side="right", fill="y")

text_comentarios = tk.Text(comentario_frame, width=30, height=5, yscrollcommand=scroll.set)
text_comentarios.pack(side="left")
scroll.config(command=text_comentarios.yview)

# Opción de Vacaciones
tk.Label(formulario, text="Vacaciones:").grid(row=6, column=0, sticky="ne", padx=(0, 10), pady=10)

vacaciones_frame = tk.Frame(formulario)
vacaciones_frame.grid(row=6, column=1, sticky="w")

# Variables para los Checkbuttons
playa_var = tk.BooleanVar()
montana_var = tk.BooleanVar()
rural_var = tk.BooleanVar()

tk.Checkbutton(vacaciones_frame, text="Playa", variable=playa_var).pack(anchor="w")
tk.Checkbutton(vacaciones_frame, text="Montaña", variable=montana_var).pack(anchor="w")
tk.Checkbutton(vacaciones_frame, text="Turismo Rural", variable=rural_var).pack(anchor="w")

# Imagen decorativa
try:
    avion_img = PhotoImage(file="avion.png")
    label_imagen = tk.Label(formulario, image=avion_img, width=40, height=60)
    label_imagen.image = avion_img  # Evitar que la imagen sea eliminada por el recolector
    label_imagen.grid(row=7, column=0, columnspan=2, pady=10)
except Exception as e:
    print(f"No se pudo cargar la imagen: {e}")

# Botón de envío
def enviar():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    direccion = entry_direccion.get()
    password = entry_password.get()
    genero = genero_var.get()
    comentarios = text_comentarios.get("1.0", "end-1c")

    vacaciones = []
    if playa_var.get():
        vacaciones.append("Playa")
    if montana_var.get():
        vacaciones.append("Montaña")
    if rural_var.get():
        vacaciones.append("Turismo Rural")

    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Dirección: {direccion}")
    print(f"Password: {password}")
    print(f"Género: {genero}")
    print(f"Comentarios: {comentarios}")
    print(f"Vacaciones seleccionadas: {', '.join(vacaciones) if vacaciones else 'Ninguna'}")

    # Autocompletado de ejemplo
    entry_nombre.delete(0, tk.END)
    entry_nombre.insert(0, "Juan")
    entry_apellido.delete(0, tk.END)
    entry_apellido.insert(0, "Pérez")

tk.Button(formulario, text="Enviar", command=enviar).grid(row=8, column=0, columnspan=2, pady=15)

ventana.mainloop()
