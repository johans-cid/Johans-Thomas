from typing import Any

from datos.modelos.atencion import Atencion


def Listado_atenciones():
    return list(Atencion.select())


def obtener_atencion(id_atencion: int) -> Atencion | None:
    return Atencion.get_or_none(Atencion.id_atencion == id_atencion)


def crear_atencion(datos: dict[str, Any]) -> Atencion:
    return Atencion.create(**datos)


def actualizar_atencion(id_atencion: int, datos: dict[str, Any]) -> int:
    datos = {k: v for k, v in datos.items() if k != "id_atencion"}
    if not datos:
        return 0
    return Atencion.update(**datos).where(Atencion.id_atencion == id_atencion).execute()


def eliminar_atencion(id_atencion: int) -> int:
    return Atencion.delete().where(Atencion.id_atencion == id_atencion).execute()