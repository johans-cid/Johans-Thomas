from typing import Any

from datos.modelos.horario_atencion import HorarioAtencion


def Listado_HorarioAtencion():
    return list(HorarioAtencion.select())


def obtener_horario_atencion(id_horario_atencion: int) -> HorarioAtencion | None:
    return HorarioAtencion.get_or_none(
        HorarioAtencion.id_horario_atencion == id_horario_atencion
    )


def crear_horario_atencion(datos: dict[str, Any]) -> HorarioAtencion:
    return HorarioAtencion.create(**datos)


def actualizar_horario_atencion(id_horario_atencion: int, datos: dict[str, Any]) -> int:
    datos = {k: v for k, v in datos.items() if k != "id_horario_atencion"}
    if not datos:
        return 0
    return HorarioAtencion.update(**datos).where(
        HorarioAtencion.id_horario_atencion == id_horario_atencion
    ).execute()


def eliminar_horario_atencion(id_horario_atencion: int) -> int:
    return HorarioAtencion.delete().where(
        HorarioAtencion.id_horario_atencion == id_horario_atencion
    ).execute()