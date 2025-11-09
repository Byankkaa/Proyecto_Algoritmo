import mysql.connector

from mysql.connector import errorcode
cursor = None
cnx = None
def ConectarBase():

   global cnx, cursor
   try:
    cnx = mysql.connector.connect(user="root", password="", host="Localhost", database="canchas_futbol")
    cursor = cnx.cursor(dictionary=True)
    print('Conexión establecida')
   except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuario o contraseña incorrectos!')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('La base de datos no existe!')
    else:
            print(err)
ConectarBase()

#Hasta acá es copypaste de la teoria que tenemos en classroom

def Insertar_Clientes(dni,nombre,telefono):
    sql = "INSERT INTO Clientes(dni, nombre, telefono)VALUES( %s, %s, %s)"
    try:
        cursor.execute(sql,(dni,nombre,telefono))
        cnx.commit()
    except Exception as e:
        if e==mysql.connector.errors.DataError:
            print("Error de datos: ", e)
        else:
            print("Ocurrió un error al insertar los datos:", e)
def Insertar_Reservas(id_cliente, id_cancha, id_horario, fecha_reserva, estado_pago):
    sql = "INSERT INTO Reservas(id_cliente, id_cancha, id_horario, fecha_reserva, estado_pago)VALUES( %s,%s, %s, %s, %s)"
    
    try:
        cursor.execute(sql,(id_cliente, id_cancha, id_horario, fecha_reserva, estado_pago))
        cnx.commit()
    except Exception as e:
        if e==mysql.connector.errors.DataError:
            print("Error de datos: ", e)
        else:
            print("Ocurrió un error al insertar los datos:", e)
def Insertar_Pagos_Facturas(id_reserva, monto, metodo_pago, id_pago, fecha_emision, total):
    sql = "INSERT INTO Pagos(id_reserva, monto, metodo_pago)VALUES(%s, %s, %s)"

    try:
        cursor.execute(sql,(id_reserva, monto, metodo_pago))
        cnx.commit()
    except Exception as e:
        if e==mysql.connector.errors.DataError:
            print("Error de datos: ", e)
        else:
            print("Ocurrió un error al insertar los datos:", e)
    sql = "INSERT INTO Facturas( id_pago, fecha_emision, total)VALUES(%s, %s, %s)"

    try:
        cursor.execute(sql,(id_pago, fecha_emision, total))
        cnx.commit()
    except Exception as e:
        if e==mysql.connector.errors.DataError:
            print("Error de datos: ", e)
        else:
            print("Ocurrió un error al insertar los datos:", e)
def Insertar_Canchero(nombre, telefono, dni, sueldo):
    sql = "INSERT INTO Cancheros(nombre, telefono, dni, sueldo)VALUES(%s, %s, %s, %s)"
    try:
        cursor.execute(sql,(nombre, telefono, dni, sueldo))
        cnx.commit()
    except Exception as e:
        if e==mysql.connector.errors.DataError:
            print("Error de datos: ", e)
        else:
            print("Ocurrió un error al insertar los datos:", e)
def Insertar_Mantenimiento(id_cancha, tipo_mantenimiento, costo, estado, fecha):
    sql = "INSERT INTO Mantenimiento_Canchas(id_cancha, tipo_mantenimiento, costo, estado, fecha)VALUES(%s, %s, %s, %s, %s)"
    try:
        cursor.execute(sql,(id_cancha, tipo_mantenimiento, costo, estado, fecha))
        cnx.commit()
    except Exception as e:
        if e==mysql.connector.errors.DataError:
            print("Error de datos: ", e)
        else:
            print("Ocurrió un error al insertar los datos:", e)



def Matriz_Horarios():
    Matriz = [ #Matriz para ver los horarios de la cancha, en una consulta aparte se va a poder saber si esta reservado o no
    ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'],
    ['Mañana', 'Mañana', 'Mañana', 'Mañana', 'Mañana', 'Mañana', 'Mañana'],
    ['Tarde', 'Tarde', 'Tarde', 'Tarde', 'Tarde', 'Tarde', 'Tarde'],
    ['Noche', 'Noche', 'Noche', 'Noche', 'Noche', 'Noche', 'Noche']
    ]
    consulta = " SELECT h.dia_semana, h.tipo_turno FROM Reservas r INNER JOIN Horarios h ON r.id_horario = h.id_horario WHERE r.estado_pago != 'Cancelado';"
    cursor.execute(consulta)

    reservas = cursor.fetchall()
    for i in range(1, len(Matriz)):
        for j in range(len(Matriz[0])):
            dia = Matriz[0][j]
            turno = Matriz[i][0] if i > 0 else None

            for r in reservas:
                if r['dia_semana'] == dia and r['tipo_turno'] == turno:
                    Matriz[i][j] = "Reservado"

    for fila in Matriz:
        print(fila)
    return Matriz




def Menu(): #Esto va ultimo, es el menu principal, pero lo queria hacer ahora para que ya lo tengamos
    print("-----Menu Cancha de Futbol-----")
    print("1. Ver horarios disponibles")
    print("2. Ingresar datos")
    print("3. Consultar datos")
    print("4. Salir")

    sel=int(input("Seleccione una opcion: "))
    if sel == 1:
        Matriz_Horarios()
        Menu()
    elif sel == 2:
        Menu_Ingresar_Datos()
        Menu()
    elif sel == 3:
        print("Consultas no implementadas aun")
        Menu()
    elif sel == 4:
        print("Saliendo del programa...")
        cursor.close()
        cnx.close()
        exit()


def Menu_Ingresar_Datos(): #Menu para ingresar datos
    Matriz = Matriz_Horarios()
    print("-----Menu Ingresar Datos-----")
    print("1. Ingresar Cliente")
    print("2. Ingresar Reserva")
    print("3. Ingresar Pago y su Factura")
    print("4. Ingresar Canchero")
    print("5. Ingresar Mantenimiento")
    print("6. Volver al menu principal")

    sel=int(input("Seleccione una opcion: "))
    if sel == 1:
        dni=input("Ingrese el DNI del cliente: ")
        nombre=input("Ingrese el nombre del cliente: ")
        telefono=input("Ingrese el telefono del cliente: ")
        Insertar_Clientes(dni,nombre,telefono)
        print("Cliente ingresado correctamente")
    elif sel == 2:
        id_cliente=input("Ingrese el ID del cliente: ")
        id_cancha=input("Ingrese el ID de la cancha: ")
        id_horario=input("Ingrese el ID del horario: ")
        fecha_reserva=input("Ingrese la fecha de la reserva (AAAA-MM-DD): ")
        estado_pago=input("Ingrese el estado del pago: ")
        for i in range(1, len(Matriz)):
            for j in range(len(Matriz[0])):
                if Matriz[i][j] == "Reservado":
                    print(f"El horario {Matriz[i][0]} del dia {Matriz[0][j]} ya esta reservado.")
                else:
                    Insertar_Reservas(id_cliente, id_cancha, id_horario, fecha_reserva, estado_pago)
                    print("Reserva ingresada correctamente")
    elif sel == 3:
        id_reserva=input("Ingrese el ID de la reserva: ")
        monto=input("Ingrese el monto del pago: ")
        metodo_pago=input("Ingrese el metodo de pago: ")
        id_pago=input("Ingrese el ID del pago: ")
        fecha_emision=input("Ingrese la fecha de emision de la factura (AAAA-MM-DD): ")
        total=input("Ingrese el total de la factura: ")
        Insertar_Pagos_Facturas(id_reserva, monto, metodo_pago, id_pago, fecha_emision, total)
        print("Pago ingresado correctamente")
    elif sel == 4:
        nombre=input("Ingrese el nombre del canchero: ")
        telefono=input("Ingrese el telefono del canchero: ")
        dni=input("Ingrese el DNI del canchero: ")
        sueldo=input("Ingrese el sueldo del canchero: ")
        Insertar_Canchero(nombre, telefono, dni, sueldo)
        print("Canchero ingresado correctamente")
    elif sel == 5:
        id_cancha=input("Ingrese el ID de la cancha: ")
        tipo_mantenimiento=input("Ingrese el tipo de mantenimiento: ")
        costo=input("Ingrese el costo del mantenimiento: ")
        estado=input("Ingrese el estado del mantenimiento: ")
        fecha=input("Ingrese la fecha del mantenimiento (AAAA-MM-DD): ")
        Insertar_Mantenimiento(id_cancha, tipo_mantenimiento, costo, estado, fecha)
        print("Mantenimiento ingresado correctamente")
    elif sel == 6:
        return
    else:
        print("Opcion no valida, intente de nuevo")
    
Menu()