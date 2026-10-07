from peewee import AutoField, Model, CharField, IntegerField
from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Direccion(BaseModel):
    id_direccion = AutoField()
    calle = CharField(max_length=100)
    departamento = CharField(max_length=50, null=True)
    numero = IntegerField()

    class Meta:
        table_name = "direccion"
