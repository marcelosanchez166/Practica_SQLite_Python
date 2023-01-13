import sqlite3

# Abrir y crear Conexion a la base de sql lite
conexion = sqlite3.connect("Administrar Productos")

# Crear Puntero
cursor = conexion.cursor()
# Id_producto VARCHAR(5) PRIMARY KEY,

"""Para no permitir que se repita un registro en un campo se usa UNIQUE"""
# cursor.execute('''
#           CREATE TABLE Productos(
#           Id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
#           Nombre_articulo VARCHAR(50) UNIQUE,
#           PRECIO INTEGER,
#           SECCION VARCHAR(20))
#           ''')

# ListaProductos=[
#           ("Camisa",12, "Ropa"),
#           ("Pantalon",16, "Ropa"),
#           ("Headset",34, "Perifericos"),
#           ("Procesador",124, "Hardware"),
#           ("Cubo de rubik",8, "Juguetes")
# ]

# Los signos de preguntas hacen referencia a la cantidad de valores de cada elemento que se crea en la tabla
#cursor.executemany("INSERT INTO Productos VALUES (?,?,?,?)", ListaProductos)

# Se coloca NULL cuando se coloca en autoincremente un id
# cursor.executemany("INSERT INTO Productos VALUES (NULL,?,?,?)", ListaProductos)


"""---------------Crear un CRUD-----------------
create=CREATE, read=SELECT, Update=UPDATE, delete=DELETE"""


"""---------------------Consultar Select--------"""
#cursor.execute("SELECT * FROM  Productos where Id_producto=1")

# Variable para guardar lo extraido de la base con el select
# valoresextraidos=cursor.fetchall()

# for i in valoresextraidos:
#           #print(i)
#           print("Id: ", i[0], " Articulo: ", i[1], " Precio: ",i[2], "Seccion: ", i[3])


"""------------------------Actualizar registros-----------------"""
# cursor.execute("UPDATE Productos SET SECCION='PlayIntelligent' WHERE Id_producto=5 ")

# cursor.execute("SELECT * FROM  Productos where Id_producto=5 ")
# valoresextraidos=cursor.fetchall()

# for i in valoresextraidos:
#           #print(i)
#           print("Id: ", i[0], " Articulo: ", i[1], " Precio: ",i[2], "Seccion: ", i[3])


"""------------------------Eleminar DELETE------------------"""
cursor.execute("DELETE FROM Productos WHERE Id_producto=5")

cursor.execute("SELECT * FROM  Productos ")
valoresextraidos = cursor.fetchall()

for i in valoresextraidos:
    # print(i)
    print("Id: ", i[0], " Articulo: ", i[1],
    " Precio: ", i[2], "Seccion: ", i[3])


conexion.commit()

conexion.close()
