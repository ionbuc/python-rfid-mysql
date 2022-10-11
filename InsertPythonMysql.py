# Bibliotecas
import mysql.connector

# Conexión
cnx = mysql.connector.connect(user='kikelan', password='0123', host='192.168.100.106', database='codigoIot')
print ("Conexión realizada")
# Cursor
cursor = cnx.cursor()

query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('kike Buchán','Prueba11' ,109876543212);"
print ("Query creado")
# Ejecutar cursor
cursor.execute (query_insert)
print ("Cursor ejecutado")

# Asegurarse de realizar la operacion en BD
cnx.commit()
print ("Query Ok")

# Cerrar
cursor.close()
cnx.close()
