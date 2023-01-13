import sqlite3

# Abrir y crear Conexion a la base de sql lite
conexion = sqlite3.connect("Base en SQL lite")

# Crear Puntero
cursor = conexion.cursor()

# Sirve para crear tablas, se debe borrar o comentar dado que si se deja dara error si ya se ejecuto una vez
#cursor.execute("CREATE TABLE Productos (Nombre_articulo VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# Para confirmar un insert es necesario el commit
#cursor.execute("INSERT INTO Productos VALUES('Balon', 15, 'Deportes' )")

"""
#Ingresar varios valores a una tabla desde una lista o tuplas
Productosvarios=[
    ("Camiseta", 10, "Deportes"),
    ("Pelota", 12, "Deportes"),
    ("Resortera", 4, "Jugueteria")
]
#Y para ingresar esos valores se usa la funcion executemany
cursor.executemany("INSERT INTO Productos VALUES (?,?,?)", Productosvarios)"""

# Leer informacion de una tabla
cursor.execute("SELECT * FROM Productos")
# Crear una variable lista para mostrar los datos extraidos de la tabla
valoresextraidos = cursor.fetchall()
for i in valoresextraidos:
    # print(i)
    print("Articulo: ", i[0], " Precio: ", i[1], " Seccion: ", i[2])


conexion.commit()

conexion.close()
