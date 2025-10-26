Create database if not exists canchas_futbol;
Use canchas_futbol;

Create table Clientes(
id_cliente int auto_increment primary key,
dni varchar(8) not null unique,
nombre varchar(100) not null,
telefono varchar(20)
);

create table Canchas(
id_cancha int auto_increment primary key,
tipo varchar(50) not null,
precio_hora decimal(10,2) not null,
estado ENUM("Disponible","Ocupada","Mantenimiento") Default"Disponible"
);

Create table Recepcionistas(
id_recepcionista int auto_increment primary key,
dni varchar(8) not null unique,
nombre varchar(100) not null,
telefono varchar(20)
);

Create table Reservas(
id_reserva int auto_increment primary key,
id_cliente int not null,
id_cancha int not null,
id_recepcionista int not null,
fecha_reserva date not null,
hora_inicio time not null,
hora_fin time not null,
estado ENUM("Pendiente","Pagada","Cancelada") Default "Pendiente"
);

Create table Pagos(
id_pago int auto_increment primary key,
id_reserva int not null,
monto decimal(10,2) not null,
metodo_pago ENUM("Efectivo","Tarjeta","Transferencia") not null,
fecha_pago datetime default current_timestamp,
foreign key (id_reserva) references Reservas(id_reserva)
);

Create table Facturas(
id_factura int auto_increment primary key,
id_pago int not null,
fecha_emision date not null,
total decimal(10,2) not null,
foreign key(id_pago) references Pagos(id_pago)
);

Create table Horarios(
id_horario int auto_increment primary key,
hora_inicio time not null,
hora_fin time not null,
tipo_turno ENUM("mañana","tarde","noche"),
dia_semana ENUM("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
);

Create table Mantenimiento_Canchas(
Id_Mantenimiento int auto_increment primary key,
id_cancha int not null,
tipo_mantenimiento varchar(100) not null,
costo decimal(10,2),
estado ENUM("Pendiente","Completado") default "Pendiente",
fecha date not null,
foreign key (id_cancha) references Canchas(id_cancha)
);

Create table Supervisores(
id_supervisor int auto_increment primary key,
dni varchar(8) not null unique,
nombre varchar(100) not null,
Horario varchar(50),
Sueldo decimal(10,2)
);