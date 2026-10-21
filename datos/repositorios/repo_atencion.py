from datos.modelos.atencion import Atencion


def listado_atenciones():
    try:
        atenciones = Atencion.select()
        if atenciones:
            return atenciones
    except Exception as error:
        print(f'Error: {error}')


def obtener_atencion(id_atencion: int) -> Atencion | None:
    try:
        atencion = Atencion.get(Atencion.id_atencion == id_atencion)
        if atencion:
            return atencion
    except Exception as error:
        print(f'Error: {error}')


def guardar_atencion(atencion: Atencion):
    try:
        respuesta = atencion.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {atencion.id_atencion}')
    except Exception as error:
        print(f'Error: {error}')


def eliminar_atencion(id_atencion: int) -> int:
    try:
        return Atencion.delete().where(Atencion.id_atencion == id_atencion).execute()
    except Exception as error:
        print(f'Error: {error}')
        return 0