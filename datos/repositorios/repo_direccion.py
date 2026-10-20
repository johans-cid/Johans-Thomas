from typing import Any

from datos.modelos.direccion import Direccion


def Listado_direcciones():
    return listar_direcciones()


def listar_direcciones():
    return list(Direccion.select())


def obtener_direccion(id_direccion: int) -> Direccion | None:
    return Direccion.get_or_none(Direccion.id_direccion == id_direccion)


def crear_direccion(datos: dict[str, Any]) -> Direccion:
    return Direccion.create(**datos)


def actualizar_direccion(id_direccion: int, datos: dict[str, Any]) -> int:
    datos = {k: v for k, v in datos.items() if k != "id_direccion"}
    if not datos:
        return 0
    return Direccion.update(**datos).where(Direccion.id_direccion == id_direccion).execute()


def eliminar_direccion(id_direccion: int) -> int:
    return Direccion.delete().where(Direccion.id_direccion == id_direccion).execute()