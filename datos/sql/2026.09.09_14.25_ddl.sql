CREATE DATABASE sistema_turnos_medicos;

USE sistema_turnos_medicos;

CREATE TABLE IF NOT EXISTS direccion(
	id_direccion INT AUTO_INCREMENT,
	calle VARCHAR(100) NOT NULL,
	numero INT NOT NULL,
	departamento VARCHAR(50),

	CONSTRAINT pk_direccion PRIMARY KEY (id_direccion)
);

CREATE TABLE IF NOT EXISTS persona(
	run VARCHAR(12),
	nombre VARCHAR(50) NOT NULL,
	apellido VARCHAR(50) NOT NULL,
	correo_electronico VARCHAR(100),
	telefono VARCHAR(20),
	fecha_nacimiento DATE,
	fk_id_direccion INT,

	CONSTRAINT pk_persona PRIMARY KEY (run),
	CONSTRAINT fk_persona_direccion FOREIGN KEY (fk_id_direccion) REFERENCES direccion(id_direccion)
);

CREATE TABLE IF NOT EXISTS paciente(
	run VARCHAR(12),
	prioridad VARCHAR(20),

	CONSTRAINT pk_paciente PRIMARY KEY (run),
	CONSTRAINT fk_paciente_persona FOREIGN KEY (run) REFERENCES persona(run)
);

CREATE TABLE IF NOT EXISTS profesional(
	run VARCHAR(12),
	especialidad VARCHAR(50),

	CONSTRAINT pk_profesional PRIMARY KEY (run),
	CONSTRAINT fk_profesional_persona FOREIGN KEY (run) REFERENCES persona(run)
);

CREATE TABLE IF NOT EXISTS horario_atencion(
	id_horario_atencion INT AUTO_INCREMENT,
	fecha DATE NOT NULL,
	hora_inicio TIME NOT NULL,
	hora_final TIME NOT NULL,
	disponibilidad BOOLEAN DEFAULT TRUE,
	fk_run_profesional VARCHAR(12) NOT NULL,

	CONSTRAINT pk_horario_atencion PRIMARY KEY (id_horario_atencion),
	CONSTRAINT fk_horario_atencion_profesional FOREIGN KEY (fk_run_profesional) REFERENCES profesional(run)
);

CREATE TABLE IF NOT EXISTS atencion(
	id_atencion INT AUTO_INCREMENT,
	estado VARCHAR(20) NOT NULL,
	fk_id_horario_atencion INT NOT NULL,
	fk_run_paciente VARCHAR(12) NOT NULL,

	CONSTRAINT pk_atencion PRIMARY KEY (id_atencion),
	CONSTRAINT fk_atencion_horario FOREIGN KEY (fk_id_horario_atencion) REFERENCES horario_atencion(id_horario_atencion),
	CONSTRAINT fk_atencion_paciente FOREIGN KEY (fk_run_paciente) REFERENCES paciente(run)
);