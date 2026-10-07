from datos.modelos.horario_atencion import HorarioAtencion

def Listado_HorarioAtencion():
    Atenciones = HorarioAtencion.select() 
    if Atenciones:
        return Atenciones