# Healthcare SQL Project

Este proyecto consiste en una base de datos para gestionar la información de los pacientes en una clínica u hospital. La base de datos almacena información sobre los pacientes, médicos, citas, tratamientos y medicamentos.

## Estructura de la Base de Datos

### Tablas

1. **Pacientes**
   - `id_paciente` (INT, PRIMARY KEY)
   - `nombre` (VARCHAR)
   - `apellido` (VARCHAR)
   - `fecha_nacimiento` (DATE)
   - `genero` (VARCHAR)
   - `direccion` (VARCHAR)
   - `telefono` (VARCHAR)
   - `email` (VARCHAR)

2. **Medicos**
   - `id_medico` (INT, PRIMARY KEY)
   - `nombre` (VARCHAR)
   - `apellido` (VARCHAR)
   - `especialidad` (VARCHAR)
   - `telefono` (VARCHAR)
   - `email` (VARCHAR)

3. **Citas**
   - `id_cita` (INT, PRIMARY KEY)
   - `id_paciente` (INT, FOREIGN KEY)
   - `id_medico` (INT, FOREIGN KEY)
   - `fecha` (DATE)
   - `hora` (TIME)
   - `motivo` (VARCHAR)

4. **Tratamientos**
   - `id_tratamiento` (INT, PRIMARY KEY)
   - `id_paciente` (INT, FOREIGN KEY)
   - `descripcion` (VARCHAR)
   - `fecha_inicio` (DATE)
   - `fecha_fin` (DATE)

5. **Medicamentos**
   - `id_medicamento` (INT, PRIMARY KEY)
   - `nombre` (VARCHAR)
   - `descripcion` (VARCHAR)
   - `dosis` (VARCHAR)
