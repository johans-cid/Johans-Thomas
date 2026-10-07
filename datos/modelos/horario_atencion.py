from peewee import BooleanField, ForeignKeyField, Model, DateField, TimeField, AutoField, SQL
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class HorarioAtencion(BaseModel):
    disponibilidad = BooleanField(constraints=[SQL("defecto")], null=True)
    fecha = DateField()
    fk_run_profesional = ForeignKeyField(column_name="fk_run_profesional", field="run", model=Profesional)
    hora_final = TimeField()
    hora_inicio = TimeField()
    id_horario_atencion = AutoField()
    

    class Meta:
        table_name = "horario_atencion"
