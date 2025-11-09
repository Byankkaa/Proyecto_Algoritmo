import mysql.connector

from mysql.connector import errorcode
cursor = None
cnx = None
def ConectarBase():

   global cnx, cursor
   try:
    cnx = mysql.connector.connect(user="root", password="", host="Localhost", database="holi")
    cursor = cnx.cursor(dictionary=True)
    print('Conexión establecida')
   except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuario o contraseña incorrectos!')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('La base de datos no existe!')
    else:
            print(err)

def ConsultaSelect():
    Consulta = "SELECT * FROM clientes;"
    cursor.execute(Consulta)
    return cursor.fetchall()

#Hasta acá es copypaste de la teoria que tenemos en classroom

