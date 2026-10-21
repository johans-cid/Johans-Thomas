from datos.modelos.paciente import Paciente


def listado_pacientes():
    try:
        pacientes = Paciente.select()
        if pacientes:
            return pacientes
    except Exception as error:
        print(f'Error: {error}')


def obtener_paciente(run: str) -> Paciente | None:
    try:
        paciente = Paciente.get(Paciente.run == run)
        if paciente:
            return paciente
    except Exception as error:
        print(f'Error: {error}')


def guardar_paciente(paciente: Paciente):
    try:
        respuesta = paciente.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {paciente.run}')
    except Exception as error:
        print(f'Error: {error}')


def eliminar_paciente(run: str) -> int:
    try:
        return Paciente.delete().where(Paciente.run == run).execute()
    except Exception as error:
        print(f'Error: {error}')
        return 0