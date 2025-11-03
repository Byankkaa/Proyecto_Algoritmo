DROP DATABASE IF EXISTS canchas_futbol;
CREATE DATABASE IF NOT EXISTS canchas_futbol;
USE canchas_futbol;

CREATE TABLE Clientes(
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(8) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    telefono INT(10)
);

CREATE TABLE Canchas(
    id_cancha INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    precio_hora DECIMAL(10,2) NOT NULL,
    estado ENUM('Disponible','Ocupada','Mantenimiento') DEFAULT 'Disponible'
);

CREATE TABLE Horarios(
    id_horario INT AUTO_INCREMENT PRIMARY KEY,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    tipo_turno ENUM('Mañana','Tarde','Noche'),
    dia_semana ENUM('Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo')
);

CREATE TABLE Reservas(
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_cancha INT NOT NULL,
    id_horario INT NOT NULL,
    fecha_reserva DATE NOT NULL,
    estado_pago ENUM('Pendiente','Pagado','Cancelado') DEFAULT 'Pendiente',
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_cancha) REFERENCES Canchas(id_cancha),
    FOREIGN KEY (id_horario) REFERENCES Horarios(id_horario)
);

CREATE TABLE Pagos(
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_reserva INT NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    metodo_pago ENUM('Efectivo','Tarjeta','Efectivo','Transferencia') NOT NULL,
    fecha_pago DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_reserva) REFERENCES Reservas(id_reserva)
);

CREATE TABLE Facturas(
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    id_pago INT NOT NULL,
    fecha_emision DATE NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_pago) REFERENCES Pagos(id_pago)
);

CREATE TABLE Mantenimiento_Canchas(
    id_mantenimiento INT AUTO_INCREMENT PRIMARY KEY,
    id_cancha INT NOT NULL,
    tipo_mantenimiento VARCHAR(100) NOT NULL,
    costo DECIMAL(10,2),
    estado ENUM('Pendiente','Completado','Finalizado') DEFAULT 'Pendiente',
    fecha DATE NOT NULL,
    FOREIGN KEY (id_cancha) REFERENCES Canchas(id_cancha)
);

CREATE TABLE Cancheros(
    id_canchero INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(8) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    horario VARCHAR(50),
    sueldo DECIMAL(10,2)
);

INSERT INTO Canchas (tipo, precio_hora, estado) 
VALUES
('Fútbol 5', 35000, 'Disponible'),
('Fútbol 8', 80000, 'Disponible'),
('Fútbol 11', 150000, 'Mantenimiento');

INSERT INTO Cancheros (nombre, telefono, dni, sueldo)
 VALUES
('Brian Cruz', '1134567890', '30111222', 350000),
('Martina Orlandi', '1122233344', '28455679', 370000);

INSERT INTO Clientes (nombre, telefono, dni) 
VALUES
('Thiago Viana', '1122454312', '40865431'),
('Daniela Mansilla', '11875432', '40986722'),
('Maximiliano Viera', '11777332', '40232665'),
('Francisco Gutierrez', '11088654', '40877682');

INSERT INTO Horarios (hora_inicio, hora_fin, tipo_turno, dia_semana) 
VALUES
('10:00', '11:00', 'Mañana', 'Lunes'),
('18:00', '19:00', 'Tarde', 'Viernes'),
('21:00', '22:00', 'Noche', 'Sabado'),
('15:00', '16:00', 'Tarde', 'Domingo');

INSERT INTO Reservas (id_cliente, id_cancha, id_horario, fecha_reserva, estado_pago) 
VALUES
(1, 1, 1, '2025-10-20', 'Pagado'),
(2, 2, 2, '2025-10-21', 'Pendiente'),
(3, 3, 3, '2025-11-04', 'Pendiente'),
(4, 1, 4, '2025-10-30', 'Pagado');

INSERT INTO Pagos (id_reserva, monto, metodo_pago) 
VALUES
(1, 35000, 'MercadoPago'),
(4, 150000, 'Tarjeta');

INSERT INTO Facturas (id_pago, fecha_emision, total)
 VALUES
(1, '2025-10-20', 35000),
(2, '2025-10-30', 150000);

INSERT INTO Mantenimiento_Canchas (id_cancha, tipo_mantenimiento, costo, estado, fecha) 
VALUES
(2, 'Cambio de césped', 30000, 'Finalizado', '2025-09-10'),
(3, 'Revisión de luces', 20000, 'Pendiente', '2025-09-25');
