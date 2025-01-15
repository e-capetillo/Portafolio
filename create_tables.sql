-- create_tables.sql
CREATE TABLE Pacientes (
    id_paciente INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    fecha_nacimiento DATE,
    genero VARCHAR(10),
    direccion VARCHAR(100),
    telefono VARCHAR(15),
    email VARCHAR(50)
);

CREATE TABLE Medicos (
    id_medico INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    especialidad VARCHAR(50),
    telefono VARCHAR(15),
    email VARCHAR(50)
);

CREATE TABLE Citas (
    id_cita INT PRIMARY KEY,
    id_paciente INT,
    id_medico INT,
    fecha DATE,
    hora TIME,
    motivo VARCHAR(100),
    FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente),
    FOREIGN KEY (id_medico) REFERENCES Medicos(id_medico)
);

CREATE TABLE Tratamientos (
    id_tratamiento INT PRIMARY KEY,
    id_paciente INT,
    descripcion VARCHAR(100),
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);

CREATE TABLE Medicamentos (
    id_medicamento INT PRIMARY KEY,
    nombre VARCHAR(50),
    descripcion VARCHAR(100),
    dosis VARCHAR(50)
);