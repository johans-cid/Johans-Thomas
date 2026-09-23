import mysql.connector

db = mysql.connector.connect(
    user="admin",
    password="TurnosMedicos2026!",
    host="sistema-turnos-medicos.ce9u4ui4u8m8.us-east-1.rds.amazonaws.com",
    database="sistema_turnos_medicos"
    # puerto: 3306
)

cursor = db.cursor()
cursor.execute("select * from direccion")
result = cursor.fetchall()

for direccion in result:
    print(direccion)

