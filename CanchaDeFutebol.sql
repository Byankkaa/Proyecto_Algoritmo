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

Create table Cancheros(
id_canchero int auto_increment primary key,
dni varchar(8) not null unique,
nombre varchar(100) not null,
Horario varchar(50),
Sueldo decimal(10,2)
);

Insert Into Canchas(tipo,precio_hora,estado)
Values
('Fútbol 5',35000,'Disponible'),
('Fútbol 8',80000,'Disponible'),
('Fútbol 11',150000,'Mantenimiento');

Insert Into Cancheros(nombre,telefono,dni,sueldo)
Values
('Brian Cruz','1134567890','30111222',350000),
('Martina Orlandi','1122233344','28455679',370000);


Insert Into Clientes(nombre,telefono,dni)
Values
('Thiago Viana','1122454312','40865431'),
('Daniela Mansilla','11875432','40986722'),
('Maximiliano Viera','11777332','40232665'),
('Fransisco Gutierrez','11088654','40877682');

Insert Into Horarios(hora_inicio,hora_fin,tipo,dia_semana)
Values
('10:00','11:00','Mañana','Lunes'),
('18:00','19:00','Tarde','Viernes'),
('21:00','22:00','Noche','Sabado'),
('15:00','16:00','Tarde','Domingo');

insert Into Reservas(id_cliente,id_cancha,id_horario,id_recepcionista,fecha_reserva,estado_pago)
Values
(1,1,1,1,'2025-10-20','Pagado'),
(2,2,2,2,'2025-10-21','Pendiente'),
(3,3,3,3,'2025-11-04','Pendiente'),
(4,1,4,1,'2025-10-30','Pagado');

Insert Into Pagos(id_reserva,monto,metodo_pago)
Values
(1,80000,'MercadoPago'),
(4,150000,'Tarjeta');

Insert Into Facturas(id_pago,fecha_emision,total)
Values
(1,'2025-10-20',35000),
(4,'2025-10-30',150000);

Insert Into Mantenimiento_Canchas(id_cancha,tipo_mantenimiento,costo,estado,fecha)
Values
(2,'Cambio de césped',30000,'Finalizado','2025-09-10'),
(3,'Revision de luces',20000,'Pendiente','2025-09-25');





