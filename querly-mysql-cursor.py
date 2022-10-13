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
query = ("SELECT id,fecha,nombre,texto,rfid FROM rfid WHERE id=1;")

# Ejecutar cursor
cursor.execute (query)

res = cursor.fetchall ()

for x in res:
    print (x)

# Cerrar todo
cursor.close()
cnx.close()
