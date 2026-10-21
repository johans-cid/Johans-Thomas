from datos.modelos.direccion import Direccion


def listado_direcciones():
    try:
        direcciones = Direccion.select()
        if direcciones:
            return direcciones
    except Exception as error:
        print(f'Error: {error}')


def obtener_direccion(id_direccion: int) -> Direccion | None:
    try:
        direccion = Direccion.get(Direccion.id_direccion == id_direccion)
        if direccion:
            return direccion
    except Exception as error:
        print(f'Error: {error}')


def guardar_direccion(direccion: Direccion):
    try:
        respuesta = direccion.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {direccion.id_direccion}')
    except Exception as error:
        print(f'Error: {error}')


def eliminar_direccion(id_direccion: int) -> int:
    try:
        return Direccion.delete().where(Direccion.id_direccion == id_direccion).execute()
    except Exception as error:
        print(f'Error: {error}')
        return 0