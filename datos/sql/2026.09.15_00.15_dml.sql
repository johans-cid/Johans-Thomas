INSERT INTO direccion (calle, numero, departamento)
VALUES ('Avenida Alemania', 0671, 'Depto 302');

INSERT INTO persona (run, nombre, apellido, correo_electronico, telefono, fecha_nacimiento, fk_id_direccion)
VALUES ('21456789-3', 'Camila', 'Fuentes', 'camila.fuentes@gmail.com', '+56987654321', DATE '2004-05-17', NULL);