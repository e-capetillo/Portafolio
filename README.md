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
  
## Instrucciones para Ejecutar el Script de Inserción de Datos

1. Asegúrate de tener MySQL instalado y configurado en tu máquina.
2. Clona este repositorio en tu máquina local.
3. Abre el archivo `insert_data.py` y reemplaza `"tu_contraseña"` con la contraseña de tu cuenta de MySQL.
4. Abre una terminal y navega al directorio donde se encuentra el archivo `insert_data.py`.
5. Ejecuta el script con el siguiente comando:
   ```sh
   python insert_data.py

5. **Medicamentos**
   - `id_medicamento` (INT, PRIMARY KEY)
   - `nombre` (VARCHAR)
   - `descripcion` (VARCHAR)
   - `dosis` (VARCHAR)
  
## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de GitHub o por correo electrónico.

---

**Proyecto creado por:** Emily Capetillo López  
**Fecha de Creación:** Enero 2025  
**Correo electrónico:** [emi.capetillo@gmail.com](mailto:emi.capetillo@gmail.com)
