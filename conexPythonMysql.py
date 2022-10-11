import mysql.connector

cnx = mysql.connector.connect(user='kikebuc', password='0123',
                              host='192.168.100.106',
                              database='codigoIot')
print('conexión realizada')
cnx.close()
print('conexión cerrada')
