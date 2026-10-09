from peewee import Model, CharField, ForeignKeyField
from datos.conexion import conectar
from datos.modelos.persona import Persona

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Paciente(BaseModel):
    prioridad = CharField(max_length=20, null=True)
    run = ForeignKeyField(column_name='run', field='run', model=Persona, primary_key=True)

    class Meta:
        table_name = "paciente"