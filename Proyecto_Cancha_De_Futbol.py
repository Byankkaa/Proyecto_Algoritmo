import mysql.connector

from mysql.connector import errorcode
cursor = None
cnx = None
def ConectarBase():

   global cnx, cursor
   try:
    cnx = mysql.connector.connect(user="root", password="", host="Localhost", database="CanchaDeFutebol")
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

def Consulta1():

    Consulta = "SELECT r.id_reserva, c.nombre AS cliente, ca.tipo AS cancha, h.hora_inicio, h.hora_fin, h.dia_semana, r.fecha_reserva, r.estado_pago FROM Reservas r Inner JOIN Clientes c ON r.id_cliente = c.id_cliente Inner JOIN Canchas ca ON r.id_cancha = ca.id_cancha Inner JOIN Horarios h ON r.id_horario = h.id_horario;"
    cursor.execute(Consulta)
    
    return cursor.fetchall()

def Consulta2():

    Consulta="SELECT ca.tipo AS cancha, SUM(p.monto) AS ingresos_totales FROM Pagos p Inner JOIN Reservas r ON p.id_reserva = r.id_reserva Inner JOIN Canchas ca ON r.id_cancha = ca.id_cancha GROUP BY ca.tipo;"
    cursor.execute(Consulta)
    return cursor.fetchall()

def Consulta3():
    respuesta=str(input("Desea buscar en base a otro tipo de estado (SI / NO)? (Si elige no va a ser en base a disponibles): ")).strip()
    if respuesta.lower() == "si":
        estado= str(input("Ingrese el estado de la cancha (Ocupado / Mantenimiento): "))

        Consulta="SELECT tipo, precio_hora FROM Canchas WHERE estado = %s;"
        cursor.execute(Consulta, (estado,))
        return cursor.fetchall()
    else:
        print("Buscando en base a canchas disponibles...")
        Consulta="SELECT tipo, precio_hora FROM Canchas WHERE estado = 'Disponible';"
        cursor.execute(Consulta)
        return cursor.fetchall()

def Consulta4():
    respuesta=str(input("Desea buscar en base a otro estado de pago (SI / NO)? (Si elige la opción NO va a ser en base a Pendiente): "))
    if respuesta.lower() == "si":
        estado_pago= str(input("Ingrese el estado de pago (Pagado / Cancelado): "))

        Consulta="SELECT r.id_reserva, c.nombre AS cliente, ca.tipo AS cancha, r.fecha_reserva FROM Reservas r Inner JOIN Clientes c ON r.id_cliente = c.id_cliente Inner JOIN Canchas ca ON r.id_cancha = ca.id_cancha WHERE r.estado_pago = %s;"
        cursor.execute(Consulta, (estado_pago,))

        return cursor.fetchall()
    else:
        print("Buscando en base a pendientes...")
        Consulta="SELECT r.id_reserva, c.nombre AS cliente, ca.tipo AS cancha, r.fecha_reserva FROM Reservas r Inner JOIN Clientes c ON r.id_cliente = c.id_cliente Inner JOIN Canchas ca ON r.id_cancha = ca.id_cancha WHERE r.estado_pago = 'Pendiente';"
        cursor.execute(Consulta)

        return cursor.fetchall()

def Consulta5():

    Consulta="SELECT ca.tipo AS cancha, m.tipo_mantenimiento, m.costo, m.estado, m.fecha FROM Mantenimiento_Canchas m Inner JOIN Canchas ca ON m.id_cancha = ca.id_cancha ORDER BY m.fecha DESC;"
    cursor.execute(Consulta)

    return cursor.fetchall()

def Consulta6():

    Consulta="SELECT tipo, precio_hora, estado FROM canchas;"
    cursor.execute(Consulta)

    return cursor.fetchall()

def Consulta7():

    Consulta="SELECT dni, nombre, telefono FROM Clientes;"
    cursor.execute(Consulta)

    return cursor.fetchall()

def Consulta8():

    Consulta="SELECT c.id_cancha, c.tipo, COUNT(m.id_cancha) as cantidadMantenimientos, SUM(m.costo) as costoTotal, AVG(m.costo) as promedioPorMantenimiento FROM mantenimiento_canchas m INNER JOIN canchas c on m.id_cancha = c.id_cancha GROUP BY m.id_cancha;"
    cursor.execute(Consulta)

    return cursor.fetchall()

def Consulta9():

    Consulta="SELECT metodo_pago, count(metodo_pago) as cantidadUsado, SUM(monto) as totalRecaudado from Pagos GROUP BY metodo_pago;"
    cursor.execute(Consulta)

    return cursor.fetchall()

def Consulta10():
    respuesta=str(input("Desea cambiar el día (SI / NO)? (Si elige la opción NO va a ser en base a Viernes)"))
    if respuesta.lower == "si":
        dia= str(input("Ingrese el día de la semana (Lunes / Martes / Miércoles / Jueves / Sábado / Domingo): "))

        Consulta="SELECT c.id_cancha, cl.nombre as Cliente, h.hora_inicio, h.hora_fin FROM Reservas r INNER JOIN canchas c on r.id_cancha = c.id_cancha INNER JOIN clientes cl on cl.id_cliente = r.id_cliente INNER JOIN horarios h on h.id_horario = r.id_horario WHERE h.dia_semana = %s;"
        cursor.execute(Consulta, (dia,))

        return cursor.fetchall()
    else:
        print("Buscando las reservas de los Viernes...")
        Consulta="SELECT c.id_cancha, cl.nombre as Cliente, h.hora_inicio, h.hora_fin FROM Reservas r INNER JOIN canchas c on r.id_cancha = c.id_cancha INNER JOIN clientes cl on cl.id_cliente = r.id_cliente INNER JOIN horarios h on h.id_horario = r.id_horario WHERE h.dia_semana = 'Viernes';"
        cursor.execute(Consulta, (dia,))

        return cursor.fetchall()

def Consulta11():
    respuesta=str(input("Desea ordenar las canchas por precio o por tipo?: "))
    if respuesta.lower=="precio":
        print("Ordenando las canchas por precio...")
        Consulta="SELECT * FROM Canchas ORDER BY precio_hora ASC;"
        cursor.execute(Consulta)
        return cursor.fetchall()
    else:
        print("Ordenando las canchas por tipo...")
        Consulta="SELECT * FROM Canchas ORDER BY tipo ASC;"
        return cursor.fetchall(Consulta)

def Menu_Consultas():
    while True:
        print("\n========= MENÚ CONSULTAS =========")
        print("1. Muestra todas las reservas junto al cliente, fecha y hora más el estado del pago")
        print("2. Ingresos totales de los distintos tipos de cancha")
        print("3. Muestra el tipo y precio por horas de las canchas")
        print("4. Muestra las reservas, el cliente, el tipo de cancha, la fecha y el estado de pago")
        print("5. Muestra el tipo de cancha, mantenimiento, costo, estado y la fecha de las canchas (en orden descendiente)")
        print("6. Listar canchas")
        print("7. Listar clientes")
        print("8. Estadísticas mantenimiento")
        print("9. Métodos de pago")
        print("10. Reservas por día de la semana")
        print("11. Canchas ordenadas por precio o tipo")
        print("0. Salir")
    
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            print(Consulta1())
        elif opcion == "2":
            print(Consulta2())
        elif opcion == "3":
            print(Consulta3())
        elif opcion == "4":
            print(Consulta4())
        elif opcion == "5":
            print(Consulta5())
        elif opcion == "6":
            print(Consulta6())
        elif opcion == "7":
            print(Consulta7())
        elif opcion == "8":
            print(Consulta8())
        elif opcion == "9":
            print(Consulta9())
        elif opcion == "10":
            print(Consulta10())
        elif opcion =="11":
            print(Consulta11())
        elif opcion == "0":
            print("Saliendo del menú...")
            break
        else:
            print("Opción inválida, intente de nuevo.")


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




def Menu(): 
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
        Menu_Consultas()
        Menu()
    elif sel == 4:
        print("Saliendo del programa...")
        cursor.close()
        cnx.close()
        exit()


def Menu_Ingresar_Datos(): 
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
