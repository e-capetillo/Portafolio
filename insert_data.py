import mysql.connector
import random
from datetime import datetime, timedelta

# Conectar a la base de datos MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tu_contraseña*",  # Reemplazar con tu propia contraseña
    database="healthcare"
)
cursor = conn.cursor()

# Limpiar las tablas
print("Limpiando las tablas...")
cursor.execute('DELETE FROM Citas')
cursor.execute('DELETE FROM Tratamientos')
cursor.execute('DELETE FROM Medicamentos')
cursor.execute('DELETE FROM Pacientes')
cursor.execute('DELETE FROM Medicos')
print("Tablas limpiadas.")

# Listas de nombres y apellidos para generar datos
nombres = ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis', 'Carmen', 'Jose', 'Laura', 'Carlos', 'Lucia']
apellidos = ['Garcia', 'Martinez', 'Lopez', 'Gonzalez', 'Rodriguez', 'Fernandez', 'Perez', 'Sanchez', 'Ramirez', 'Torres']
especialidades = ['Cardiología', 'Neurología', 'Pediatría', 'Dermatología', 'Ginecología', 'Psiquiatría']
medicamentos_nombres = ['Paracetamol', 'Ibuprofeno', 'Amoxicilina', 'Loratadina', 'Omeprazol']

# Listas de motivos y tratamientos 
motivos_citas = [
    "Chequeo general", "Dolor de cabeza", "Dolor abdominal", "Fiebre", "Tos persistente",
    "Dolor en el pecho", "Dificultad para respirar", "Revisión postoperatoria", "Control de diabetes",
    "Control de hipertensión"
]
tratamientos_descripciones = [
    "Tratamiento para hipertensión", "Tratamiento para diabetes", "Tratamiento para asma",
    "Tratamiento para alergias", "Tratamiento para infecciones urinarias", "Tratamiento para migrañas",
    "Tratamiento para colesterol alto", "Tratamiento para artritis", "Tratamiento para depresión",
    "Tratamiento para ansiedad"
]

# Función para generar fecha de nacimiento aleatoria
def random_date_of_birth(start_year=1950, end_year=2005):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    return start_date + (end_date - start_date) * random.random()

# Función para generar fecha aleatoria
def random_date(start_date, end_date):
    return start_date + (end_date - start_date) * random.random()

# Función para generar hora aleatoria
def random_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return f"{hour:02}:{minute:02}:{second:02}"

# Generar 18750 registros para cada tabla
num_records = 18750

# Insertar datos en la tabla Pacientes
print("Insertando datos en la tabla Pacientes...")
for i in range(1, num_records + 1):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    cursor.execute('''
    INSERT INTO Pacientes (id_paciente, nombre, apellido, fecha_nacimiento, genero, direccion, telefono, email)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
        i,
        nombre,
        apellido,
        random_date_of_birth().strftime('%Y-%m-%d'),
        random.choice(['Masculino', 'Femenino']),
        f'Calle {random.randint(1, 100)}',
        f'{random.randint(6000000000, 6999999999)}',
        f'{nombre.lower()}.{apellido.lower()}{i}@example.com'
    ))
print("Datos insertados en la tabla Pacientes.")

# Insertar datos en la tabla Medicos
print("Insertando datos en la tabla Medicos...")
for i in range(1, num_records + 1):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    especialidad = random.choice(especialidades)
    cursor.execute('''
    INSERT INTO Medicos (id_medico, nombre, apellido, especialidad, telefono, email)
    VALUES (%s, %s, %s, %s, %s, %s)
    ''', (
        i,
        nombre,
        apellido,
        especialidad,
        f'{random.randint(6000000000, 6999999999)}',
        f'{nombre.lower()}.{apellido.lower()}{i}@example.com'
    ))
print("Datos insertados en la tabla Medicos.")

# Insertar datos en la tabla Citas
print("Insertando datos en la tabla Citas...")
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)
for i in range(1, num_records + 1):
    cursor.execute('''
    INSERT INTO Citas (id_cita, id_paciente, id_medico, fecha, hora, motivo)
    VALUES (%s, %s, %s, %s, %s, %s)
    ''', (
        i,
        random.randint(1, num_records),
        random.randint(1, num_records),
        random_date(start_date, end_date).strftime('%Y-%m-%d'),
        random_time(),
        random.choice(motivos_citas)
    ))
print("Datos insertados en la tabla Citas.")

# Insertar datos en la tabla Tratamientos
print("Insertando datos en la tabla Tratamientos...")
for i in range(1, num_records + 1):
    start_treatment_date = random_date(start_date, end_date)
    end_treatment_date = start_treatment_date + timedelta(days=random.randint(30, 365))
    cursor.execute('''
    INSERT INTO Tratamientos (id_tratamiento, id_paciente, descripcion, fecha_inicio, fecha_fin)
    VALUES (%s, %s, %s, %s, %s)
    ''', (
        i,
        random.randint(1, num_records),
        random.choice(tratamientos_descripciones),
        start_treatment_date.strftime('%Y-%m-%d'),
        end_treatment_date.strftime('%Y-%m-%d')
    ))
print("Datos insertados en la tabla Tratamientos.")

# Insertar datos en la tabla Medicamentos
print("Insertando datos en la tabla Medicamentos...")
for i in range(1, num_records + 1):
    nombre_medicamento = random.choice(medicamentos_nombres)
    cursor.execute('''
    INSERT INTO Medicamentos (id_medicamento, nombre, descripcion, dosis)
    VALUES (%s, %s, %s, %s)
    ''', (
        i,
        nombre_medicamento,
        f'Descripcion del medicamento {nombre_medicamento}',
        f'{random.randint(10, 500)} mg'
    ))
print("Datos insertados en la tabla Medicamentos.")

# Confirmar los cambios
conn.commit()
print("Cambios confirmados.")

# Cerrar la conexión
