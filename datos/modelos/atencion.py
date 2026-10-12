from peewee import Model, CharField, ForeignKeyField, AutoField
from datos.conexion import conectar
from datos.modelos.paciente import Paciente
from datos.modelos.horario_atencion import HorarioAtencion
base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Atencion(BaseModel):
    estado = CharField(max_length=20)
    fk_id_horario_atencion = ForeignKeyField(column_name='fk_id_horario_atencion', field='id_horario_atencion',model=HorarioAtencion)
    fk_run_paciente = ForeignKeyField(column_name='fk_run_paciente', field='run', model=Paciente)
    id_atencion = AutoField()
    class Meta:
        table_name = "atencion"