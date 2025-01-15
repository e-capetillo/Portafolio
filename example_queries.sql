-- example_queries.sql

-- Consultar todos los pacientes
SELECT * FROM Pacientes;

-- Consultar todas las citas de un paciente específico
SELECT Citas.fecha, Citas.hora, Medicos.nombre AS nombre_medico, Medicos.apellido AS apellido_medico, Citas.motivo
FROM Citas
JOIN Medicos ON Citas.id_medico = Medicos.id_medico
WHERE Citas.id_paciente = 1;

-- Consultar todos los tratamientos de un paciente específico
SELECT Tratamientos.descripcion, Tratamientos.fecha_inicio, Tratamientos.fecha_fin
FROM Tratamientos
WHERE Tratamientos.id_paciente = 1;

-- Consultar todos los medicamentos
SELECT * FROM Medicamentos;

-- Consultar citas por fecha
SELECT * FROM Citas
WHERE fecha = '2025-01-20';

-- Consultar pacientes por género
SELECT genero, COUNT(*) AS cantidad
FROM Pacientes
GROUP BY genero;

-- Consultar médicos por especialidad
SELECT especialidad, COUNT(*) AS cantidad
FROM Medicos
GROUP BY especialidad;

-- Consultar citas por médico
SELECT Medicos.nombre, Medicos.apellido, COUNT(*) AS cantidad_citas
FROM Citas
JOIN Medicos ON Citas.id_medico = Medicos.id_medico
GROUP BY Medicos.id_medico;

-- Consultar tratamientos activos (fecha_fin en el futuro)
SELECT * FROM Tratamientos
WHERE fecha_fin > CURDATE();

-- Consultar pacientes con más de una cita
SELECT id_paciente, COUNT(*) AS cantidad_citas
FROM Citas
GROUP BY id_paciente
HAVING COUNT(*) > 1;

-- Consultar medicamentos más recetados
SELECT Medicamentos.nombre, COUNT(*) AS cantidad
FROM Tratamientos
JOIN Medicamentos ON Tratamientos.descripcion LIKE CONCAT('%', Medicamentos.nombre, '%')
GROUP BY Medicamentos.id_medicamento
ORDER BY cantidad DESC;

-- Consultar citas en un rango de fechas
SELECT * FROM Citas
WHERE fecha BETWEEN '2025-01-01' AND '2025-01-31';

-- Consultar pacientes por rango de edad
SELECT 
    CASE 
        WHEN TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) < 18 THEN 'Menores de 18'
        WHEN TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) BETWEEN 18 AND 35 THEN '18-35'
        WHEN TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) BETWEEN 36 AND 50 THEN '36-50'
        ELSE 'Mayores de 50'
    END AS rango_edad,
    COUNT(*) AS cantidad
FROM Pacientes
GROUP BY rango_edad;

-- Consultar citas por hora del día
SELECT 
    CASE 
        WHEN HOUR(hora) BETWEEN 0 AND 6 THEN 'Madrugada'
        WHEN HOUR(hora) BETWEEN 7 AND 12 THEN 'Mañana'
        WHEN HOUR(hora) BETWEEN 13 AND 18 THEN 'Tarde'
        ELSE 'Noche'
    END AS periodo,
    COUNT(*) AS cantidad
FROM Citas
GROUP BY periodo;

-- Consultar tratamientos por duración
SELECT id_paciente, descripcion, DATEDIFF(fecha_fin, fecha_inicio) AS duracion_dias
FROM Tratamientos
ORDER BY duracion_dias DESC;

-- Consultar pacientes sin citas
SELECT * FROM Pacientes
WHERE id_paciente NOT IN (SELECT id_paciente FROM Citas);

-- Consultar médicos con más de 10 citas
SELECT Medicos.nombre, Medicos.apellido, COUNT(*) AS cantidad_citas
FROM Citas
JOIN Medicos ON Citas.id_medico = Medicos.id_medico
GROUP BY Medicos.id_medico
HAVING COUNT(*) > 10;

-- Consultar citas por motivo
SELECT motivo, COUNT(*) AS cantidad
FROM Citas
GROUP BY motivo
ORDER BY cantidad DESC;

-- Consultar pacientes por dirección
SELECT direccion, COUNT(*) AS cantidad
FROM Pacientes
GROUP BY direccion
ORDER BY cantidad DESC;

-- Consultar tratamientos por paciente
SELECT Pacientes.nombre, Pacientes.apellido, Tratamientos.descripcion, Tratamientos.fecha_inicio, Tratamientos.fecha_fin
FROM Tratamientos
JOIN Pacientes ON Tratamientos.id_paciente = Pacientes.id_paciente;