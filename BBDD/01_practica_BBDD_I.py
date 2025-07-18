import sqlite3

# Conectar a la base de datos (se crea si no existe)
conexion = sqlite3.connect('productos.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PRODUCTOS (
        NOMBRE_ARTICULO TEXT,
        PRECIO REAL,
        SECCION TEXT
    )
''')

# Datos de ejemplo
productos = [
    ('Camiseta', 19.99, 'Ropa'),
    ('Smartphone', 299.99, 'Electrónica'),
    ('Libro de cocina', 14.50, 'Libros'),
    ('Auriculares', 49.90, 'Electrónica')
]

cursor.execute('DELETE FROM PRODUCTOS')

# Insertar los registros
cursor.executemany('INSERT INTO PRODUCTOS VALUES (?, ?, ?)', productos)

# Confirmar los cambios
conexion.commit()

# Verificar que se han insertado (opcional: mostrar en consola)
cursor.execute('SELECT * FROM PRODUCTOS')
for fila in cursor.fetchall():
    print(fila)

# Cerrar la conexión
conexion.close()
