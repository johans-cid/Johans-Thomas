from datos.modelos.horario_atencion import HorarioAtencion


def listado_horarios_atencion():
    try:
        horarios = HorarioAtencion.select()
        if horarios:
            return horarios
    except Exception as error:
        print(f'Error: {error}')


def obtener_horario_atencion(id_horario_atencion: int) -> HorarioAtencion | None:
    try:
        horario = HorarioAtencion.get(
            HorarioAtencion.id_horario_atencion == id_horario_atencion
        )
        if horario:
            return horario
    except Exception as error:
        print(f'Error: {error}')


def guardar_horario_atencion(horario: HorarioAtencion):
    try:
        respuesta = horario.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {horario.id_horario_atencion}')
    except Exception as error:
        print(f'Error: {error}')


def eliminar_horario_atencion(id_horario_atencion: int) -> int:
    try:
        return HorarioAtencion.delete().where(
            HorarioAtencion.id_horario_atencion == id_horario_atencion
        ).execute()
    except Exception as error:
        print(f'Error: {error}')
        return 0