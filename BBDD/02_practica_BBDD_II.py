import sqlite3

def crear_tabla_y_datos():
    conexion = sqlite3.connect('new_productos.db')
    cursor = conexion.cursor()

    # Crear tabla con clave primaria autoincrementable
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PRODUCTOS (
            ID_ARTICULO INTEGER PRIMARY KEY AUTOINCREMENT,
            CODIGO_ARTICULO TEXT UNIQUE,
            NOMBRE_ARTICULO TEXT,
            PRECIO REAL,
            SECCION TEXT
        )
    ''')

    # Insertar datos de ejemplo solo si la tabla está vacía
    cursor.execute('SELECT COUNT(*) FROM PRODUCTOS')
    if cursor.fetchone()[0] == 0:
        productos = [
            ('A001', 'Camiseta', 19.99, 'Ropa'),
            ('A002', 'Ratón inalámbrico', 25.50, 'Electrónica'),
            ('A003', 'Taza de cerámica', 8.95, 'Hogar'),
            ('A004', 'Libro de Python', 35.00, 'Libros'),
            ('A005', 'Don Quijote de la Mancha', 45.00, 'Libros')
        ]
        for producto in productos:
            try:
                cursor.execute('''
                    INSERT INTO PRODUCTOS (CODIGO_ARTICULO, NOMBRE_ARTICULO, PRECIO, SECCION)
                    VALUES (?, ?, ?, ?)
                ''', producto)
            except sqlite3.IntegrityError:
                pass

    conexion.commit()
    conexion.close()

def mostrar_productos_por_seccion():
    seccion = input("Introduce el nombre de la sección que quieres consultar: ").strip()

    conexion = sqlite3.connect('new_productos.db')
    cursor = conexion.cursor()

    cursor.execute('SELECT ID_ARTICULO, CODIGO_ARTICULO, NOMBRE_ARTICULO, PRECIO, SECCION  FROM PRODUCTOS WHERE SECCION = ?', (seccion,))
    productos = cursor.fetchall()
    print("Productos")

    if productos:
        print(f"\n📦 Productos en la sección '{seccion}':\n")
        for producto in productos:
            print(f"ID: {producto[0]}, Código: {producto[1]}, Nombre: {producto[2]}, Precio: {producto[3]} €")
    else:
        print(f"\n⚠️ No se encontraron productos en la sección '{seccion}'.")

    conexion.close()

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Buscar productos por sección")
        print("2. Salir")
        opcion = input("Elige una opción (1-2): ")

        if opcion == '1':
            mostrar_productos_por_seccion()
        elif opcion == '2':
            print("👋 Saliendo del programa.")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

# Ejecutar
crear_tabla_y_datos()
menu()
