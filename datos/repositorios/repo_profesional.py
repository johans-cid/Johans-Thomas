from datos.modelos.profesional import Profesional


def listado_profesionales():
    try:
        profesionales = Profesional.select()
        if profesionales:
            return profesionales
    except Exception as error:
        print(f'Error: {error}')


def obtener_profesional(run: str) -> Profesional | None:
    try:
        profesional = Profesional.get(Profesional.run == run)
        if profesional:
            return profesional
    except Exception as error:
        print(f'Error: {error}')


def guardar_profesional(profesional: Profesional):
    try:
        respuesta = profesional.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {profesional.run}')
    except Exception as error:
        print(f'Error: {error}')


def eliminar_profesional(run: str) -> int:
    try:
        return Profesional.delete().where(Profesional.run == run).execute()
    except Exception as error:
        print(f'Error: {error}')
        return 0