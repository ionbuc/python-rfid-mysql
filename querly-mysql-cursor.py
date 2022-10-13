# Bibliotecas
import mysql.connector

# Conexion
cnx = mysql.connector.connect(user='kikelan', 
                              password='0123', 
                              host='127.0.0.1',
                              database='codigoIot')

# Cursor
cursor = cnx.cursor()

# Query
query = ("SELECT id,nombre,temperatura,fecha FROM clima WHERE id=555;")

# Ejecutar cursor
cursor.execute (query)

res = cursor.fetchall ()

for x in res:
    print (x)

# Cerrar todo
cursor.close()
cnx.close()
