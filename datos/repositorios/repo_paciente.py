from typing import Any

from datos.modelos.paciente import Paciente


def Listado_pacientes():
    return listar_pacientes()


def listar_pacientes():
    return list(Paciente.select())


def obtener_paciente(run: str) -> Paciente | None:
    return Paciente.get_or_none(Paciente.run == run)


def crear_paciente(datos: dict[str, Any]) -> Paciente:
    return Paciente.create(**datos)


def guardar_paciente(paciente: Paciente) -> int:
    return paciente.save(force_insert=True)


def actualizar_paciente(run: str, datos: dict[str, Any]) -> int:
    datos = {k: v for k, v in datos.items() if k != "run"}
    if not datos:
        return 0
    return Paciente.update(**datos).where(Paciente.run == run).execute()


def eliminar_paciente(run: str) -> int:
    return Paciente.delete().where(Paciente.run == run).execute()