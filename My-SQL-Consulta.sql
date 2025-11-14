
SELECT
  r.id_reserva, c.nombre AS cliente, ca.tipo AS cancha, h.hora_inicio, h.hora_fin, h.dia_semana,
  r.fecha_reserva, r.estado_pago
FROM Reservas r
Inner JOIN Clientes c ON r.id_cliente = c.id_cliente
Inner JOIN Canchas ca ON r.id_cancha = ca.id_cancha
Inner JOIN Horarios h ON r.id_horario = h.id_horario;


SELECT
  ca.tipo AS cancha,
  SUM(p.monto) AS ingresos_totales
FROM Pagos p
Inner JOIN Reservas r ON p.id_reserva = r.id_reserva
Inner JOIN Canchas ca ON r.id_cancha = ca.id_cancha
GROUP BY ca.tipo;


SELECT tipo, precio_hora
FROM Canchas
WHERE estado = 'Disponible';


SELECT
  r.id_reserva, c.nombre AS cliente, ca.tipo AS cancha, r.fecha_reserva
FROM Reservas r
Inner JOIN Clientes c ON r.id_cliente = c.id_cliente
Inner JOIN Canchas ca ON r.id_cancha = ca.id_cancha
WHERE r.estado_pago = 'Pendiente';


SELECT
  ca.tipo AS cancha, m.tipo_mantenimiento, m.costo, m.estado, m.fecha
FROM Mantenimiento_Canchas m
Inner JOIN Canchas ca ON m.id_cancha = ca.id_cancha
ORDER BY m.fecha DESC;


SELECT tipo, precio_hora, estado
FROM canchas;


SELECT dni, nombre, telefono
FROM Clientes;


SELECT c.id_cancha, c.tipo, COUNT(m.id_cancha) as cantidadMantenimientos, SUM(m.costo) as costoTotal, AVG(m.costo) as promedioPorMantenimiento
FROM mantenimiento_canchas m
INNER JOIN canchas c on m.id_cancha = c.id_cancha
GROUP BY m.id_cancha;


SELECT metodo_pago, count(metodo_pago) as cantidadUsado, SUM(monto) as totalRecaudado
from Pagos
GROUP BY metodo_pago;


SELECT c.id_cancha, cl.nombre as Cliente, h.hora_inicio, h.hora_fin
FROM Reservas r
INNER JOIN canchas c on r.id_cancha = c.id_cancha
INNER JOIN clientes cl on cl.id_cliente = r.id_cliente
INNER JOIN horarios h on h.id_horario = r.id_horario
WHERE h.dia_semana = 'Viernes';
