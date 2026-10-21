from typing import Any

from datos.modelos.profesional import Profesional


def Listado_profesionales():
    return list(Profesional.select())


def obtener_profesional(run: str) -> Profesional | None:
    return Profesional.get_or_none(Profesional.run == run)


def crear_profesional(datos: dict[str, Any]) -> Profesional:
    return Profesional.create(**datos)


def actualizar_profesional(run: str, datos: dict[str, Any]) -> int:
    datos = {k: v for k, v in datos.items() if k != "run"}
    if not datos:
        return 0
    return Profesional.update(**datos).where(Profesional.run == run).execute()


def eliminar_profesional(run: str) -> int:
    return Profesional.delete().where(Profesional.run == run).execute()