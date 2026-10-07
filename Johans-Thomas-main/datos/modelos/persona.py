from peewee import Model, CharField, DateField, ForeignKeyField, BooleanField, SQL
from datos.conexion import conectar
from datos.modelos.direccion import Direccion
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Persona(BaseModel):
    apellido = CharField(max_length=50)
    correo_electronico = CharField(max_length=100, null=True)
    fecha_nacimiento = DateField(null=True)
    fk_id_direccion = ForeignKeyField(column_name="fk_id_direccion", field="id_direccion", model=Direccion, null=True)
    habilitado = BooleanField(constraints=[SQL(defecto)])
    nombre = CharField(max_length=50)
    run = CharField(max_length=12, primary_key=True)
    telefono = CharField(max_length=20, null=True)

    class Meta:
        table_name = "persona"