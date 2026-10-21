from typing import Any

from datos.modelos.persona import Persona


def Listado_personas():
    return list(Persona.select())


def obtener_persona(run: str) -> Persona | None:
    return Persona.get_or_none(Persona.run == run)


def crear_persona(datos: dict[str, Any]) -> Persona:
    return Persona.create(**datos)


def actualizar_persona(run: str, datos: dict[str, Any]) -> int:
    datos = {k: v for k, v in datos.items() if k != "run"}
    if not datos:
        return 0
    return Persona.update(**datos).where(Persona.run == run).execute()


def eliminar_persona(run: str) -> int:
    return Persona.delete().where(Persona.run == run).execute()