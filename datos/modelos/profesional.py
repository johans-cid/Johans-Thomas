from peewee import CharField, ForeignKeyField, Model
from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Profesional(BaseModel):
    especialidad = CharField(max_length=50, null=True)
    run = ForeignKeyField(column_name="run", field="run", model=Persona, primary_key=True )
    

    class Meta:
        table_name = "profesional"
